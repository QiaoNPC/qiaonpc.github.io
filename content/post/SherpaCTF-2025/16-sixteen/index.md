---
title: 16 - Sixteen
description: Log in as admin via SQL Injection and delete all 5-star feedback entries to retrieve the flag.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Sixteen - CTF Challenge Writeup

## Challenge Information
- **Name**: Sixteen  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Log in as admin via SQL Injection and delete all 5-star feedback entries to retrieve the flag.

---

## Solution

- From **User Fifteen**, the challenge is to remove all **five-star feedbacks** from the system.


    ![Challenge 16](sixteen.png)


- To do that, we first need **admin access**, which can be achieved using **SQL Injection** on the login form.
- After gaining access, navigate to the **feedback section** of the OWASP Juice Shop dashboard.
- Manually identify and **delete all entries with a 5-star rating**.
- Once all high-rated feedbacks are cleared, the challenge marks as complete and the **flag is revealed**.


    ![Flag](flag.png)

---

## Flag  
`78231b75c0b2180b7e964dcbb1ab3c3f58639f2e`
