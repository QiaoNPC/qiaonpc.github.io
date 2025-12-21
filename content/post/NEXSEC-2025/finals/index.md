---
title: finals
description: Analyze the finals artifacts to reverse engineer a .NET malware chain, decrypt C2-delivered DLL payloads, and recover the flag.
date: 2025-12-21 00:00:00+0000
categories:
   - NEXSEC-2025
   - CTF Writeup

tags:
   - Reverse Engineering
weight: 1     
---
# finals

## Challenge Information
- **Name**: finals  
- **Points**: 10  
- **Category**: Reverse Engineering  
- **Objective**: Analyze the finals artifacts to reverse engineer a .NET malware chain, decrypt C2-delivered DLL payloads, and recover the flag.

## Solution

### 1. **Finals Format Overview**
- The finals format is new, and there are no flags provided at the start.
- You are given a set of artifacts to analyze for IOCs and related details.
- No questions are provided initially, just the team and the artifact set.
- One hour before the CTF ends, the questions are released.
- It feels like blackbox forensics where you really have to do threat intelligence work.

### 2. **Scope of This Writeup**
- This writeup focuses only on the reverse engineering part because that was the most interesting section.

### 3. **Malware Chain Summary**
- The chain starts with a malicious DOCX file delivered by email.
- Opening the DOCX fetches a macro file from GitHub and runs it.
- The macro constructs `explorer.exe` and places it at `C:\Users\Public\explorer.exe`.

### 4. **Explorer.exe Section: .NET Reactor Protection**
- `Explorer.exe` is a .NET binary intentionally protected by Eziriz .NET Reactor to make reversing harder.
- The main functionality lives in `NetworkDiagnostics.dll`.

### 5. **C2 Address and Crypto Basics**
- The C2 server IP address and port 443 were identified.
- The program uses AES in CBC mode with a hardcoded key and IV, which lets us decrypt parts of its behavior.

   ![Step 5](5.1.png)

### 6. **Port 443 Behavior**
- Port 443 is used for beaconing, tasking (get commands), and reporting results.
- This is encrypted C2 messaging disguised as HTTPS, and the TLS layer means HTTP paths/body are not readable from the PCAP.

### 7. **C2 Endpoints**
- The C2 server exposes several endpoints.
  - `/victim`: Register the user’s unique ID.
  - `/command`: Fetch attacker tasking.
  - `/result`: Send execution output back.
  - `/heart`: Send heartbeat.
  - `/file`: Upload files.

### 8. **Port 7219 Connection**
- Alongside the port 443 traffic, there is a separate connection to port 7219.
- This TCP connection is used to send encrypted DLL payloads.

### 9. **Hardcoded AES Key and IV Names**
- The AES key and IV used to decrypt payloads are hardcoded in the binary as Base64 strings.
  - `ballandchain` holds the AES key (Base64).
  - `anchovies` holds the AES IV (Base64).

   ![Step 9](9.1.png)

   ![Step 9](9.2.png)

### 10. **DLL Transfer Protocol**
- The DLLs are transferred using a simple request/response structure.
- The client sends:
  - 4 bytes: Request payload length.
  - N bytes: How many bytes the client wants to receive.
- The server sends:
  - 4 bytes: Requested payload length.
  - N bytes: Encrypted payload bytes.

### 11. **Payload Decryption and Loading**
- The payload bytes are AES-CBC with PKCS7 padding; after reading N bytes, the client decrypts with the hardcoded AES key/IV and loads the result as a .NET DLL.

### 12. **Payloads on the 7219 Session**
- The 7219 session is used to send two files.
  - `Ertrag.dll`.
  - `Riegel.dll`.

### 13. **Extracting DLLs from the PCAP**
- After dumping the payloads from the PCAP, two DLLs were extracted: 
  - one for exfiltration and one for encrypting files on disk.

```python
#!/usr/bin/env python3
import struct, ipaddress, pathlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64

PCAP_IN = "FS-pcap.pcap"  # use editcap -F pcap FS-pcap.pcapng FS-pcap.pcap
FLOWS = [
  ("209.97.175.18", 7219, "10.10.111.114", 55311, "artifacts/Ertrag.dll"),
  ("209.97.175.18", 7219, "10.10.111.114", 55339, "artifacts/Riegel.dll"),
]

KEY = base64.b64decode("wWrx+62b7++4exaVvcwZRy3QNnd+KBGuEZcW46Ho6E4=")
IV = base64.b64decode("ERQOOQ4Cz2cyehEUrqfhLA==")

def read_pcap(path):
  with open(path, "rb") as f:
      gh = f.read(24)
      if len(gh) != 24:
          raise SystemExit("Bad pcap header")
      endian = "<" if gh[:4] == b"\xd4\xc3\xb2\xa1" else ">"
      while True:
          hdr = f.read(16)
          if len(hdr) < 16:
              break
          ts_sec, ts_usec, incl_len, orig_len = struct.unpack(endian + "IIII", hdr)
          data = f.read(incl_len)
          yield data

def assemble_flow(src, sport, dst, dport):
  segs = []
  for pkt in read_pcap(PCAP_IN):
      if len(pkt) < 34:
          continue
      eth_type = int.from_bytes(pkt[12:14], "big")
      ip_off = 14
      if eth_type == 0x8100:  # VLAN
          eth_type = int.from_bytes(pkt[16:18], "big")
          ip_off = 18
      if eth_type != 0x0800 or pkt[ip_off + 9] != 6:
          continue
      ihl = (pkt[ip_off] & 0x0F) * 4
      tcp_off = ip_off + ihl
      if len(pkt) < tcp_off + 20:
          continue
      sport2, dport2, seq = struct.unpack("!HHI", pkt[tcp_off:tcp_off + 8])
      off = (pkt[tcp_off + 12] >> 4) * 4
      payload = pkt[tcp_off + off:]
      if not payload:
          continue
      sip = str(ipaddress.IPv4Address(pkt[ip_off + 12:ip_off + 16]))
      dip = str(ipaddress.IPv4Address(pkt[ip_off + 16:ip_off + 20]))
      if (sip, sport2, dip, dport2) == (src, sport, dst, dport):
          segs.append((seq, payload))
  if not segs:
      raise SystemExit("No segments found")
  base = min(s for s, _ in segs)
  end = max(s + len(p) for s, p in segs)
  buf = bytearray(end - base)
  for seq, p in segs:
      off = seq - base
      buf[off:off + len(p)] = p
  return bytes(buf)

def decrypt_module(buf):
  length = int.from_bytes(buf[:4], "little")
  ct = buf[4:4 + length]
  cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV))
  decryptor = cipher.decryptor()
  pt = decryptor.update(ct) + decryptor.finalize()
  unpad = padding.PKCS7(128).unpadder()
  return unpad.update(pt) + unpad.finalize()

def main():
  pathlib.Path("artifacts").mkdir(exist_ok=True)
  for flow in FLOWS:
      src, sport, dst, dport, out_path = flow
      buf = assemble_flow(src, sport, dst, dport)
      dll = decrypt_module(buf)
      pathlib.Path(out_path).write_bytes(dll)
      print(f"Wrote {out_path} ({len(dll)} bytes)")

if __name__ == "__main__":
  main()
```

### 14. **Payload Responsibilities**
- Going through the payloads, `Reigel.dll` handles the ransomware on the FileServer.
- `Ertrag.dll` is responsible for exfiltrating files.

### 15. **Reigel.dll Section: Initial Look**
- Next step was looking into `reigel.dll` itself.

### 16. **Ransomware File Walk and Filters**
- The encryption routine recursively walks a directory and encrypts every file except certain extensions.
  - `.anon` files are already encrypted and skipped.
  - `.dll`, `.exe`, `.ini`, `.elf` are explicitly ignored.

   ![Step 16](16.1.png)

### 17. **Hybrid RSA + AES Scheme**
- The encryption uses hybrid RSA + AES; for each unencrypted file it follows a fixed sequence.
- Generate a fresh AES-256 key.
- Encrypt file bytes using AES-CBC with PKCS7 padding and an all-zero IV (16 bytes).
- Encrypt the AES key using the provided RSA public key with PKCS#1 v1.5 padding.
- Create output bytes = RSA_ENC_AES_KEY + AES_CIPHERTEXT.
- The encrypted AES key sits at the file header and the encrypted file content follows it.
- The file is written with the `.anon` extension.

   ![Step 17](17.1.png)

### 18. **Ransom Note Drop**
- After the encryption process, a ransom note is dropped.

   ![Step 18](18.1.png)

### 19. **Vulnerable C2 Section: Endpoint Check**
- Reviewing the C2 endpoints on `209.97.175.18`, only `/victim` is valid and the other endpoints do not exist.

### 20. **Endpoint Brute Force Findings**
- Using `feroxbuster` to brute-force endpoints revealed more routes.
  - `/agent` requires login.
  - `/console` requires a PIN for the Werkzeug console.
  - `/generate` can generate a Flask token.
  - `/keys` requires login.

   ![Step 20](20.1.png)

### 21. **SQL Injection on /victim**
- The `/victim` endpoint appears vulnerable to SQL injection in the `uniqueID` parameter.

   ![Step 21](21.1.png)

### 22. **Dumping the Database**
- Using SQLMap, the database was dumped.

   ![Step 22](22.1.png)

### 23. **Victims Table Agent ID**
- In the `victims` table, the `unique_agentId` column for `itdadmin` has the value `c18dabd3-bd18-453e-ba11-ba51ef1d5120`.

### 24. **Agents Table Keys**
- In the `agents` table, the `agent_uniqueId` is present along with Base64-encoded blobs.
- One blob is the public key and another is the private key.
- After identifying the private key, it can be used to decrypt files and recover what was lost.

### 25. **Decryption Script for .anon Files**
- A decryption script was crafted for all `.anon` files.

```python
import os
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES

# ============================================================
# RSA PRIVATE KEY (PKCS#8)
# ============================================================
PRIVATE_KEY_PEM = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDkO46CUMQh5w19
RevmIeIuR52joaq5h/YQS6q3dwiUbpNZtPc7aUyt5krDYDTqNA7Gcb21mTebMAdk
2HxadEPhUe1wEDPoWKWrkR59nqjPzewVuIVzLof5IZteeSM03ULRZuGTsm45fF4y
HxiHPUmuIucmeg5GcUBbgvz1alHzehWeZESILQ2T+fVEfmP/oDQ/c2upwY32CwST
7XaJsroYwNJ+Vsk83x94tZKHiYo85ZlOOUT0f3ECYoFBnraOrmeJLQ42TJFbUjrG
In76YWH30vXy2AYFw61yFEBTMjCbBLB62dkkXJF/4uMcJWJUygH/cTfUCnuhfmvn
hXCfbBRfAgMBAAECggEAAyQms/h0mprZfq3lr0csG8L0knn5JZCPfG3uLZQ/0/sp
oARzmqe6XHJc+Q9r6wVIZsbN+5/eOg6RK3wnSf9rp8A+6lnuvPXrYc8fgk8at7F3
3FyryYgMawthXg2AxIt/De7CkAvWpIfnq/ztk37ucq0cTVVEuQd6AUhuPtp1wkoX
Nl07SdFRo3HP2vWTWlWMa/rKVk7BuDWQIVGeg8b2vfEVHZ6GZ1Tnj5KH2QvpKnba
sXarCxZXTuCxVOXMattrKKfQbsOAKeSFKcd1wlKdQe+T+k+CfbNfC8DpVv5xTqBA
98jjiMf51dd0sXnZO+3sCCTuq8QuqDhdWeajzpK7AQKBgQDsyk1OGHVt42nszE6k
ErHqeOI5Ruj8waMoAepgGq7y2RUp67ETEfkkWxLHeKC/YuL0QnxdWr5F83TH3L8z
s30Y8m+OJifKiwDyL55wdeL2n+eMERY91YO+JYJDBnpaNGRXBsJlLlm/9igQQdHO
Tt9pQADZ124pzODfw7eYUSEOHwKBgQD2v4dzlZNzMrSPWI+XFPn+akR6KcXT6R1n
9Nmys9h9xIuSPHhLfok0T4+ojY8MBbZBDZ8+hFwErm6EJz+idRDynLU+nzRoMTAP
vYFZgYy6p7fItQ9Rx0caHprC3GO+QdruKTSYYf/OLxxNw3e0cN6wAHFFYWf6TTrm
4oeKw6OxwQKBgQDaSLgw+Q0vywf32nPYfr9ythNd18eqUdtVY0arZ43Fo2cGKRco
zFXPNQG/zqzpIYC0yaGZ8bAcDg2mvRGp2JnG6J77/KKL7c5mdI1rgNFEpy4uCgZl
5DG5lRxbK1qZU1j4fOuxmKP1+Tb/nZ2KwVzkyrK+HwGYGR1oSiUyjf+Z4wKBgFQE
NS/TD2jbLAXfJs1PtCu/rV9XV+fm6T9bbMDfYei5ArkhY+h4xmkMaiL/SGTUkREn
fUCBOv/REQpofs9nQwUI/OG8vdB4ZyAE68U5SlzH/NkXZYb37qrjHtkYx9GhhNUx
LJpyS/K9scp8swa6o+iTzf3Mw+XDZDn3iiViphtBAoGAcgCNpMWSmHMUsToDkJOJ
wzJq2bWnJ5fJoX360D9vRQyU58D4176X92+ljyeoYcGUMMgI7zz6Aff9T1/3dvaY
lezJa0jmLZ7cUWERmuyPopLChbJitt+caUqwbHMKiR0c2yLe5XaQK0qToEQCtI+S
JS3owTjTHA3h8bbSF7cKHg4=
-----END PRIVATE KEY-----"""

# ============================================================
# ROOT DIRECTORY
# ============================================================
ROOT_DIR = r"C:\Users\Jeremy Phang Kah Chu\Downloads\Documents"

# ============================================================
# CRYPTO SETUP
# ============================================================
rsa_key = RSA.import_key(PRIVATE_KEY_PEM)
rsa_cipher = PKCS1_v1_5.new(rsa_key)

recovered = 0
failed = 0

# ============================================================
# WALK + DECRYPT
# ============================================================
for root, _, files in os.walk(ROOT_DIR):
    for name in files:
        if not name.endswith(".anon"):
            continue

        anon_path = os.path.join(root, name)
        out_path = anon_path[:-5]  # Remove .anon extension

        try:
            with open(anon_path, "rb") as f:
                data = f.read()

            # The file structure is:
            # [256 bytes RSA-encrypted AES key] + [remaining bytes: AES-encrypted file]
            rsa_blob = data[:256]
            aes_blob = data[256:]

            # RSA decrypt the AES key (returns raw 32-byte AES key)
            aes_key = rsa_cipher.decrypt(rsa_blob, None)
            if not aes_key or len(aes_key) != 32:
                raise ValueError(f"RSA decryption failed or invalid key length: {len(aes_key) if aes_key else 0} bytes")

            # AES decryption with zero IV and CBC mode
            iv = bytes(16)  # Zero IV (16 bytes for AES)
            cipher = AES.new(aes_key, AES.MODE_CBC, iv)
            plaintext = cipher.decrypt(aes_blob)

            # Remove PKCS7 padding
            padding_length = plaintext[-1]
            if padding_length > 16 or padding_length < 1:
                raise ValueError(f"Invalid padding length: {padding_length}")
            plaintext = plaintext[:-padding_length]

            # Calculate SHA256 hash of decrypted content
            sha256_hash = hashlib.sha256(plaintext).hexdigest()

            # Write decrypted file
            with open(out_path, "wb") as f:
                f.write(plaintext)

            print(f"[+] Decrypted: {os.path.basename(out_path)}")
            print(f"    SHA256: {sha256_hash}")
            print(f"    Path: {out_path}")
            print()
            recovered += 1

        except Exception as e:
            print(f"[!] Failed: {os.path.basename(anon_path)} ({e})")
            print(f"    Path: {anon_path}")
            print()
            failed += 1

# ============================================================
# SUMMARY
# ============================================================
print("\n=== SUMMARY ===")
print(f"Recovered : {recovered}")
print(f"Failed    : {failed}")
```

   ![Step 25](25.1.png)
