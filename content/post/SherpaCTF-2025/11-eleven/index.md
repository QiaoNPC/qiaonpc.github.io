---
title: 11 - Eleven
description: Access and manipulate a custom Rubik’s Cube web challenge under restricted user sessions to retrieve the flag.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Eleven - CTF Challenge Writeup

## Challenge Information
- **Name**: Eleven  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Access and manipulate a custom Rubik’s Cube web challenge under restricted user sessions to retrieve the flag.

---

## Solution

- From **User Ten**, we’re given a **custom web challenge**.


    ![Challenge 11](eleven.png)


- At first, I couldn’t open the `Rubiks.html` file due to **permission issues**.
- After **45 minutes of debugging**, I realized I had been `su`-ing through multiple users — causing nested shells under **User Zero’s terminal**.
- Because of that, although I was technically **User Ten**, the permission context was messed up.
- To fix this, I **logged out completely** and logged in directly as **User Ten**. That allowed me to open **Firefox** and view the HTML page.


    ![Challenge 11](<login as eleven.png>)


- The challenge was a **Rubik’s Cube simulation**. As someone who can solve a cube physically, I considered solving it directly.
  - But the page didn’t allow turning multiple layers, and I couldn’t mentally map 1-layer operations.
  - So instead, I chose the **easier way**: modifying the **source code** to force the check function to always **return true**.


    ![Src Code Modification](<src code modification.png>)

- This trick worked — and the flag was revealed.


    ![Flag](flag.png)

---

## Flag  
`RUBIKSCUBEMASTA`
