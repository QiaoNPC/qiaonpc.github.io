---
title: 9 - Nine
description: Analyze forensic artifacts to determine the real name of the threat actor based on their Telegram activity and archived file data.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Nine - CTF Challenge Writeup

## Challenge Information
- **Name**: Nine  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Analyze forensic artifacts to determine the real name of the threat actor based on their Telegram activity and archived file data.

---

## Solution

- From **User Eight**, we're given a **forensic artifact** similar to a previous challenge, but this time the goal is to find the **real name of the attacker**.


    ![Challenge Nine](nine.png)


- Opening `telegram_profile.txt`, we can view the user's **old usernames**, one of which resembles a **last name**.


    ![Last Name](<part 1.png>)


- Separately, in `nu5a-archiv3.txt`, another potential name appears — likely the **first name**. Both names start with **R**, which supports this link.


    ![First Name](<part 2.png>)

    
- Combining the two gives us the full name: **`RADITYA_PRATAMA`**.

---

## Flag  
`SHERPACTF25{RADITYA_PRATAMA}`
