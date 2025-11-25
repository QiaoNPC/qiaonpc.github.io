---
title: Three
description: Decode the hidden flag from a seemingly normal message given by User Two.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Three - CTF Challenge Writeup

## Challenge Information
- **Name**: Three  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Decode the hidden flag from a seemingly normal message given by User Two.

---

## Solution

- From **User Two**, we’re given a regular-looking message, but the flag is **encoded**.


    ![Challenge](three.png)


- Just by eyeballing it, the pattern looked like **ROT13** — common and easy to test manually.
- Decoded it by counting through the letters manually, and got the flag.


    ![Flag](flag.jpg)

---

## Flag
`SHERPACTF25{Gh0st_in_Th3_W1r3s}`
