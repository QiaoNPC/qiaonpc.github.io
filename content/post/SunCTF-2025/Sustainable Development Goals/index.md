---
title: Sustainable Development Goals
description: The objective of this challenge is to analyze a memory dump to identify post-exploitation artifacts, uncover suspicious process behavior, decrypt and execute in-memory payloads, and extract the attacker’s intended shellcode or flag.
date: 2025-08-31 00:00:00+0000
categories:
   - SunCTF 2025
   - CTF Writeup
tags:
   - Forensics
weight: 1     
---
# Sustainable Development Goals - CTF Challenge Writeup

## Challenge Information
- **Name**: Sustainable Development Goals  
- **Points**: 10  
- **Category**: Forensics  
- **Objective**: Analyze a memory dump to identify post-exploitation artifacts, uncover suspicious process behavior, decrypt and execute in-memory payloads, and extract the attacker’s intended shellcode or flag.

---

## Solution

### 1. **Choosing a Tool: memprocfs vs Volatility**
- Given a **memory dump**, analysed it using memprocfs. 
- I chose to begin analysis with **memprocfs** instead of Volatility due to its speed and usability.
  - **memprocfs** offers real-time mounting of the memory image as a virtual file system, allowing quick browsing of processes, network connections, files, registry, environment variables, and even PowerShell history.
  - **Volatility** was later used for **more niche plugins** and **precise data extraction** (e.g., environment variables).
  - **memprocfs** is fast so I can quickly get an overview on what I should be doing to get flag. 

---

### 2. **Suspicious Process Discovery**
- During enumeration of running processes, one stood out:
  - An instance of `svchost.exe` executing from an **unusual path**:  
    `C:\Users\sunwaylobster\Pictures\svchost.exe`
- Red flags:
  - **`svchost.exe` is a legitimate Windows binary**, but typically only runs from `System32`, not `Pictures`.
  - It was **spawned by `explorer.exe`**, suggesting user-level execution.
  - Tracing the parent chain revealed it **originated from `WINWORD.EXE`** — a classic phishing vector (e.g., Word document macro).


    ![Sus Process](<1. sus process.png>)

---

### 3. **Analyzing the Malicious svchost**
- Dumped and inspected the `svchost.exe` binary.
- It was **not the real Windows svchost**, but rather **custom malicious code**.
- Behavior analysis showed it:
  - Decodes a payload intended for **process injection**
  - Uses **AES encryption** to protect the shellcode
  - Retrieves the **IV and AES key from environment variables**

---

### 4. **Extracting Environment Variables**
- Used **Volatility** to extract the environment variables of the malicious `svchost` process.
- Retrieved the **AES key and IV**, enabling decryption of the embedded payload.


    ![Extracted Envars](<2. Extracted envars.png>)

---

### 5. **Decrypting and Executing the Shellcode**
- Decrypted the encoded payload using the extracted key and IV.
- Result: a **valid shellcode blob**
- Executed the shellcode in a controlled environment (emulator or debugger) to observe behavior.
- Upon execution, the shellcode revealed the **flag**.


    ![Decrypted](<3. decrypted.png>)


    ![Flag](<4. flag.png>)

---

## Flag
The flag for this challenge is:  
`sunctf25{sh3lly_1n_my_b3lly}`
