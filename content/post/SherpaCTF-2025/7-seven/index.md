---
title: 7 - Seven
description: Identify the real IP address of the attacker from the data provided by User Six.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Seven - CTF Challenge Writeup

## Challenge Information
- **Name**: Seven  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Identify the real IP address of the attacker from the data provided by User Six.

---

## Solution

- From **User Six**, the task was to determine the **real IP address** of the attacker.


    ![Challenge seven](seven.png)


- I went with a **brute-force approach**, submitting all possible IPs found in the provided logs/data.
- Eventually, one of them returned a **positive result**.


    ![Brute Force](<brute forcing.png>)


- One important note: the flag format had a quirk — the platform **expected the flag without the '5'** in `SHERPACTF25`.
- So instead of `SHERPACTF25{...}`, the correct format was **`SHERPACTF2{...}`**.

---

## Flag  
`SHERPACTF2{103.17.24.77}`
