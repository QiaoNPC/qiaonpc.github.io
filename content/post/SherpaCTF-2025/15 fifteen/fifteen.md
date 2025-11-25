---
title: Fifteen
description: Interact with a restricted terminal environment and extract the contents of the `flag.txt` file using limited command-line capabilities.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Fifteen - CTF Challenge Writeup

## Challenge Information
- **Name**: Fifteen  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Interact with a restricted terminal environment and extract the contents of the `flag.txt` file using limited command-line capabilities.

---

## Solution

- From **User Fourteen**, we’re dropped into a **restricted terminal**.


    ![Challenge 15](fifteen.png)


- I’ve faced similar setups before, but didn’t take notes — so it took me around **an hour of trial and error** to rediscover the solution.
- In restricted shells where typical tools or flags are disabled, breaking down output is key.
- The command that worked: `grep -o . flag.txt`
- This prints the flag **character by character**, bypassing common output restrictions and filters.


    ![Flag](flag.png)

---

## Flag  
`SHERPACTF25{EZPZ}`
