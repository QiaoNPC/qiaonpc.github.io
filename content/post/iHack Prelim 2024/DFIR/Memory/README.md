---
title: Memory
description: The objective of the "Memory" CTF challenge is identify the user that was created based on a memory dump from a Windows system
date: 2024-07-28 00:00:00+0000
categories:
   - ihack-prelim-2024
   - CTF Writeup
tags:
   - Forensics
weight: 1     
---
# Memory CTF Challenge Writeup

## Challenge Information
- **Name**: Memory
- **Points**: 500
- **Category**: DFIR (Digital Forensics and Incident Response)
- **Objective**: Identify the user that was created based on a memory dump from a Windows system.


![Challenge](challenge.png)

## Solution
To solve the "Memory" challenge, follow these steps:

1. **Initial Setup**:
   - We are tasked with finding the user created on a Windows system based on a memory dump.
   - Given the filename suggests a Windows environment, use `memprocfs` to streamline the analysis of the memory dump, avoiding manual extraction with tools like Volatility.

2. **Analyzing Powershell Commands**:
   - Navigate to `/sys/proc/proc-v.txt` within `memprocfs` to locate and review PowerShell commands executed during the memory capture.
   - Search for commands that involve executing base64 encoded strings.


      ![Powershell](powershell.png)

3. **Decoding Base64 Commands**:
   - Identify and extract the base64 encoded strings from the PowerShell commands.
   - Decode the base64 strings to reveal the underlying PowerShell commands.


      ![Decoded Base64](<decoded base64.png>)

4. **Executing and Reversing PowerShell Commands**:
   - Run the decoded PowerShell commands to reveal their functionality.
   - Analyze the output to determine which user was created.


      ![Powershell Executed](<powrshell executed.png>)

5. **Finding the Flag**:
   - With the user information identified from the PowerShell commands, make the flag 


      ![Flag](flalg.png)

6. **Flag**: **ihack24{sysadmin_SYSAdmin}**