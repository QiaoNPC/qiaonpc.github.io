---
title: 18 - Eighteen
description: Log in as a specific user (Jim) in OWASP Juice Shop using SQL Injection to retrieve the flag.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Eighteen - CTF Challenge Writeup

## Challenge Information
- **Name**: Eighteen  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Log in as a specific user (Jim) in OWASP Juice Shop using SQL Injection to retrieve the flag.

---

## Solution

- From **User Seventeen**, we’re given another **OWASP Juice Shop** challenge. This time, the task is to **log in as Jim**.


    ![Challenge 18](eighteen.png)


- Actually, we had already done something similar earlier when logging in as admin to delete five-star ratings.
- The first step is to **find Jim's email**, which is typically:`jim@juice-sh.op`


    ![Jim's Email](<jim email.png>)


- Then, use a **basic SQL injection** payload to bypass the password check: `jim@juice-sh.op'--`
- This logs us in as Jim, and once authenticated, the **flag becomes accessible** — either via the profile page or shown directly.


    ![Flag](flag.png)

---

## Flag  
`de0806c1e34a5783b4b1672fa4eed440a9912378`
