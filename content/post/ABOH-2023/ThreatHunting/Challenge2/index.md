---
title: Threat Hunting Challenge 2 
description: Threat Hunting Challenge 2 CTF challenge is to identify the SHA256 hash value of the executable responsible for exfiltrating data within a given context.encryption.
date: 2023-12-02 00:00:00+0000
categories:
   - ABOH 2023
   - CTF Writeup
tags:
   - Forensics
weight: 1     
---
# Threat Hunting: Challenge 2 - CTF Challenge Writeup

## Challenge Information
- **Name**: Threat Hunting: Challenge 2
- **Objective**: The objective of the "Threat Hunting: Challenge 2" CTF challenge is to identify the SHA256 hash value of the executable responsible for exfiltrating data within a given context.

## Solution
To successfully tackle the "Threat Hunting: Challenge 2" challenge, I followed these steps:

1. **Challenge Context**:
   - This challenge is part of a series in the threat hunting category and requires identifying the SHA256 hash value of the executable responsible for data exfiltration.
   - It is recommended to solve Challenge 1 before looking into Challenge 2 and Challenge 3
   - However, you can solve Challenge 2 and Challenge 3 in any order

2. **Identifying Suspicious Executables**:
   - On further inspection from the first challenge, I discovered a total three suspicious files including the one from the first challenge.  
   - I dumped the two executables onto VirusTotal and HybridAnalysis, whilst analysed the powershell script myself.
   - The powershell script showed symptoms of reading files and encrypting it and I am suspecting that this is the file they are looking for, but not 100% certain. 


      ![Executables](<three executable.png>)

      ![Powershell Script](<powershell script.png>)

3. **Approach to Finding SHA256 Hash**:
   - A common misconception might lead one to use `Get-FileHash` to find the hash value. However, in challenges like these, this method may not yield the expected results. 
   - This difference in hash values can be due to various factors and is further explained in this [Stack Overflow thread](https://stackoverflow.com/questions/29946221/hash-value-md5-and-sha256-of-file-is-coming-different-when-file-is-from-system32).

4. **Using Hasher Tool**:
   - To accurately acquire the SHA256 hash value of the suspicious files, I utilized the Hasher tool available at [Eric Zimmerman's website](https://ericzimmerman.github.io/#!index.md).

5. **Determining Executable's SHA256 Hash**:
   - Since there were only three suspicious files discovered, and I am not so sure about my discovery, I will be calculating the SHA256 hash value for each of them using the Hasher tool and submitting as a flag. 

6. **Final Flag Discovery**:
   - Among the calculated SHA256 hash values, one matched the expected format of the flag: `ABOH{hash_value}`.
   - At the time of writing this writeup, I have forgotten which one was the flag. Im sorry.

      ![Hash Value](<sha256 value.png>)

The resolution of the "Threat Hunting: Challenge 2" involved identifying potentially malicious executables and determining their SHA256 hash values using the Hasher tool to extract the flag.

## Flag
The flag for this challenge is: `ABOH{hash_value}`.

This writeup illustrates the process of identifying the SHA256 hash value of a potentially malicious executable in the "Threat Hunting: Challenge 2" CTF challenge. For further inquiries or clarifications, feel free to ask.
