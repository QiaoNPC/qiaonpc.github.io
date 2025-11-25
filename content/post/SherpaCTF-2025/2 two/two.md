---
title: 2 - Two
description: Access the Juice Shop instance running on port `42000` and locate the scoreboard to find the flag.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Two - CTF Challenge Writeup

## Challenge Information
- **Name**: Two  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Access the Juice Shop instance running on port `42000` and locate the scoreboard to find the flag.

---

## Solution

- From **User One**, we’re told to check a web app on port **42000** — turns out it’s **OWASP Juice Shop**.


    ![Challenge](two.png)


- I’ve done this before, so it was familiar, but doing it again without internet or GPT made it more fun.
- Checked the source code, looked around, found `/score-board`.


    ![Found score-board endpoint](two_link.png)


- Once you browse to the endpoint, the flag will automatically appear on the top of the screen.


    ![Flag](flag.png)

---

## Flag
`2614339936e8282e2f820f023d4d998a1f95e02a`
