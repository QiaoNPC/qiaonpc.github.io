---
title: 13 - Thirteen
description: Exploit a vulnerable custom web application that evaluates function names passed via URL parameters without proper validation.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Thirteen - CTF Challenge Writeup

## Challenge Information
- **Name**: Thirteen  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Exploit a vulnerable custom web application that evaluates function names passed via URL parameters without proper validation.

---

## Solution

- From **User Twelve**, we’re given a **custom web app**, different from the usual OWASP Juice Shop challenges.


    ![Challenge 13](thirteen.png)


    ![Challenge 13 2](challenge.png)


- The challenge revolves around passing an **operator** to the application through a query string.
- The vulnerability lies in the fact that the **operator is executed as a function**, without any restrictions or sanitization.
- That means arbitrary functions (like `system`) can be invoked directly.
- A crafted URL like below exploits this: `http://localhost:8081?operator=system&num1=cat`
- The application executes `system('cat flag.txt')`, leaking the flag directly in the response.



    ![Flag](flag.png)

---

## Flag  
`SHERPACTF25{ARRRRRR\_CIIIIII\_EIEIEIE}`
