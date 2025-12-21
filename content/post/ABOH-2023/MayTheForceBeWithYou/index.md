---
title: May The Force Be With You
description: The objective of the May The Force Be With You CTF challenge is to decipher a hidden flag encoded within a given script using reverse engineering techniques.
date: 2023-12-02 00:00:00+0000
categories:
   - ABOH 2023
   - CTF Writeup
tags:
   - Cryptography
weight: 1     
---
# May The Force Be With You - CTF Challenge Writeup

## Challenge Information
- **Name**: May The Force Be With You
- **Objective**: The objective of the "May The Force Be With You" CTF challenge is to decipher a hidden flag encoded within a given script using reverse engineering techniques.

## Solution
To solve the "May The Force Be With You" challenge and obtain the flag, I followed the below steps:

1. **Understanding the Challenge Objective**:
   - The challenge required decoding a hidden flag from a provided script using reverse engineering methods.

2. **Initial Approach**:
   - Due to personal constraints and limited expertise in mathematics, I opted to use HackerGPT, a tool specialized in reversing scripts, to decode the hidden flag.
   - Though using automated tools can be considered disrespectful to the challenge creator, it was necessary due to my limitations and time constraints during the competition.

3. **Script Analysis**:
   - Utilizing the script below, I executed it to unveil the hidden flag.
   - Unfortunately, due to my lack of proficiency in deciphering the script manually, I had to rely on HackerGPT to assist me in understanding the logic and unveiling the flag.


      ```python
      from Crypto.Cipher import AES
      from Crypto.Util.Padding import unpad
      from Crypto.Protocol.KDF import PBKDF2
      import textwrap

      def decrypt_file(encrypted_file_path, password):
          with open(encrypted_file_path, 'rb') as file:
              ciphertext_iv = file.read()

          iv = ciphertext_iv[-AES.block_size:]
          ciphertext = ciphertext_iv[:-AES.block_size]

          passwd = textwrap.dedent(password)[:-1]
          salt = b'salt123'
          key = PBKDF2(passwd.encode(), salt, dkLen=16)

          cipher = AES.new(key, AES.MODE_CBC, iv)
          plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

          return plaintext

      password = "ni5h2h?Yrq8Do?n+|6a;pKbZkv%}O~tV"
      encrypted_file_path = "./flag.txt.enc"
      plaintext = decrypt_file(encrypted_file_path, password)

      print(plaintext.decode())
      ```

4. **Flag Extraction**:
   - Upon executing the script, the decoded flag was revealed as `ABOH23{A3S_Rul35_tH3_F0rc3}`.

The resolution of this challenge involved leveraging reverse engineering tools like HackerGPT to decode the hidden flag from the provided script. While I regret not being able to decode it manually due to personal limitations, I acknowledge the importance of understanding the underlying concepts for future challenges.

## Flag
The flag for this challenge is: `ABOH23{A3S_Rul35_tH3_F0rc3}`.

This writeup serves as a demonstration of utilizing reverse engineering tools to decode the hidden flag in the "May The Force Be With You" CTF challenge. If you have any further inquiries or need additional clarification, please feel free to ask.
