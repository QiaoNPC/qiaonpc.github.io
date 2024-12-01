---
title: X
description: The objective of the X challenge is to analyze and reverse engineer the application to retrieve the flag.
date: 2024-11-24 00:00:00+0000
categories:
   - SherpaCTF 2024
   - CTF Writeup
tags:
   - Reverse Engineering
weight: 1     
---
# X

## Challenge Information
- **Name**: X  
- **Points**: 100  
- **Category**: Reverse  
- **Objective**: Analyze and reverse engineer the application to retrieve the flag.  

## Solution  

1. **Initial Analysis**:   
   - Use tools such as Ghidra, IDA Pro, or Radare2 to analyze the code.  
   - Upon analysing the application, it performs **XOR operations** on a specific variable. 

    ![XOR Operation](<xor operation.png>)

    ![Encoded Flag](<encoded flag.png>)

2. **Reversing the XOR**:  
   - Since XOR is a reversible operation (`XOR` is its own inverse):  
   - Apply the same XOR key to the modified value to retrieve the original data (flag).  


    ```python
    xor_values = [
        (0x6B, 56),  
        (0x75, 61),  
        (0x65, 38),  
        (0x68, 60),  
        (0x74, 50),  
        (0x69, 91),  
        (0x6F, 91),  
        (0x77, 12),  
    ]

    aBcb4ce08a36317 = "bcb4ce08a3/6317b67`d8`d58e6e1e`b"

    decoded_first_part = []
    for xor_val, expected in xor_values:
        decoded_first_part.append(chr(expected ^ xor_val)) 

    decoded_second_part = []
    for char in aBcb4ce08a36317:
        decoded_second_part.append(chr(ord(char) + 1)) 

    full_string = ''.join(decoded_first_part) + ''.join(decoded_second_part)

    print(f"Full String: {full_string}"+"}")
    ```

## Flag  
- **Flag**: `SHCTF24{cdc5df19b407428c78ae9ae69f7f2fac}`  
