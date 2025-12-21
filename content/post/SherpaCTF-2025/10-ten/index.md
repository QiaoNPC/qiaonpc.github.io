---
title: 10 - Ten
description: Exploit a vulnerable login form in OWASP Juice Shop using classic SQL Injection techniques to retrieve the flag.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Ten - CTF Challenge Writeup

## Challenge Information
- **Name**: Ten  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Exploit a vulnerable login form in OWASP Juice Shop using classic SQL Injection techniques to retrieve the flag.

---

## Solution

- From **User Nine**, we’re given another **OWASP Juice Shop** challenge.


    ![Challenge 10](ten.png)


- This one is a **classic** — good old **SQL Injection**.
- The login form is completely unprotected, no WAF, no input sanitization.
- A simple payload like `' OR 1=1 --` bypasses authentication.
- After logging in using that injection, the **flag is revealed** on the resulting page or via the admin panel.


  ![Flag](flag.png)

---

## Flag  
`690fa3247a99d651e0b26f947baf
