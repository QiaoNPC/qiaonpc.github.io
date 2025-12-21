---
title: 17 - Seventeen
description: Unzip a series of recursively compressed ZIP files, collect password fragments from each layer, and use the final combined password to extract the flag.
date: 2025-11-25 00:00:00+0000
categories:
   - SherpaCTF 2025
   - CTF Writeup
tags:
   - Misc
weight: 1     
---
# Seventeen - CTF Challenge Writeup

## Challenge Information
- **Name**: Seventeen  
- **Category**: Misc  
- **Points**: 10  
- **Objective**: Unzip a series of recursively compressed ZIP files, collect password fragments from each layer, and use the final combined password to extract the flag.

---

## Solution

- From **User Sixteen**, we're presented with a challenge that involves unzipping **layered ZIP files** — a total of **10 layers deep**.
- Each ZIP file is named with a **3-character password**: either all lowercase, all uppercase, or all numbers.
- Without access to GPT, scripting this was difficult, so I ended up doing most of the layers **manually**.
- At each level, the ZIP would extract into another ZIP, and inside each, a **snippet of the final password** was hidden.
- After collecting all the snippets across the 10 layers, I **combined them into a single string**, which served as the password to unlock the **final ZIP file** containing the flag.


    ![Flag](flag.png)

---

## Flag  
`SHERPACTF25{Cr4ck_z1p5_3zpz}`
