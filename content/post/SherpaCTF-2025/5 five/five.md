---
title: 5 - Five
description: Investigate uploaded files to identify a malicious web shell used by an attacker.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Five - CTF Challenge Writeup

## Challenge Information
- **Name**: Five  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Investigate uploaded files to identify a malicious web shell used by an attacker.

---

## Solution

- From **User Four**, we’re tasked with finding **malicious files** uploaded by an attacker.


    ![Challenge](five.png)


- By grepping for keywords like `"upload"` in the logs or source files, we can trace file upload activity.
- This leads us to a file named **`nusa_shell.php`** — clearly malicious and matches the context of a typical web shell.
- That filename itself is the **flag**.


    ![Flag](grep.png)

---

## Flag
`SHERPACTF25{nusa_shell.php}`
