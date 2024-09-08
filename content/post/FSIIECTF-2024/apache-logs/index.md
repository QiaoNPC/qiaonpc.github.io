---
title: Apache Logs
description: Analyze the Apache log file to uncover and decode suspicious data.
date: 2024-09-08 00:00:00+0000
categories:
   - FSIIECTF 2024
   - CTF Writeup
tags:
   - Forensics
weight: 1     
---
# Forensics CTF Challenge Writeup

## Challenge Information
- **Name**: Apache Logs
- **Points**: 1
- **Category**: Forensics
- **Objective**: Analyze the Apache log file to uncover and decode suspicious data.

## Solution
1. **Log Analysis**:
   - The provided Apache log file is relatively short.
   - Upon reviewing the logs, identify a URL with **URL-encoded** suspicious data.


      ![Found URL Encoding](<found url encoded.png>)

2. **URL Decoding**:
   - Decode the URL using standard URL decoding techniques to reveal an ASCII representation of letters.


      ![Decode URL Encoding](<decode url encoding.png>)

3. **Conversion**:
   - Convert the ASCII representation into readable text, which reveals the flag.


      ![Flag](flag.png)

## Flag
FSIIECTF{XXXXXXXXXX}
