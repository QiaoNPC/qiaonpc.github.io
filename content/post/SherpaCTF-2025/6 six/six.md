---
title: Six
description: Interact with a newly added OWASP Juice Shop AI-based feature and identify how to retrieve a hidden flag through it.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Six - CTF Challenge Writeup

## Challenge Information
- **Name**: Six  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Interact with a newly added OWASP Juice Shop AI-based feature and identify how to retrieve a hidden flag through it.

---

## Solution

- From **User Five**, we're given another **OWASP Juice Shop** challenge.


    ![Challenge Six](six.png)


- This one felt different — it’s a **newer challenge**, likely introduced after **AI pentesting features** were added to the platform.
- Spent quite a bit of time stuck, expecting a typical `flag` to be revealed.
- Turns out, this challenge doesn't deal with flags directly — instead, it uses a **coupon bot**.
- After repeatedly interacting with the bot and specifically **asking for a coupon** multiple times, the **flag was finally returned**.


    ![Asking for Coupon](image.png)


    ![Flag](flag.png)

    
---

## Flag  
`9dd704b4c48bd310dd3187971a344c179213562d`
