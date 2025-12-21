---
title: KeepJohn
description: A writeup of the cryptography challenge KeepJohn from FSIIECTF 2024. The challenge required using Munger to guess passwords.
date: 2024-09-08 00:00:00+0000
categories:
   - FSIIECTF 2024
   - CTF Writeup
tags:
   - Crypto
weight: 1     
---
# Cryptography CTF Challenge Writeup

## Challenge Information
- **Name**: KeepJohn
- **Points**: 1
- **Category**: Cryptography

## Solution
1. Initially, I thought to use **keepass2john** and then crack the password using **John the Ripper**, but none of the passwords in the provided wordlist matched.
   - Even after trying the entire **rockyou** wordlist, it didn’t work.
   
2. Upon re-reading the challenge description, I realized it mentioned **variations of commonly used passwords**. 

3. Remembering John Hammond’s video on a tool that generates variations of passwords, I used **Munge** (a tool designed for this purpose): [Munge GitHub](https://github.com/Th3S3cr3tAg3nt/Munge).
   - Maybe the John in the challenge refers to John Hammond? [John Hammond Video](https://www.youtube.com/watch?v=nNvhK1LUD48&t=608s)

4. I generated a list of passwords using Munge, and this helped me find the correct password.


   ![Found Password](<found password.png>)

5. After opening the **kdbx** file with the found password, I retrieved the flag.


   ![Found Flag](flag.png)

## Flag
FSIIECTF{XXXXXXXXXX}
