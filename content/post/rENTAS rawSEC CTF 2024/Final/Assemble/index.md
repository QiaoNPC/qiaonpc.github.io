---
title: Assemble
description: The objective of the Assemble challenge is to correctly configure the hardware components and troubleshoot any technical issues to display the flag on the LCD.
date: 2024-03-09 00:00:00+0000
categories:
   - rENTAS rawSEC CTF 2024
   - CTF Writeup
tags:
   - Hardware
weight: 1     
---
# Assemble CTF Challenge Writeup

## Challenge Information
- **Name**: Assemble
- **Points**: 500
- **Category**: Hardware
- **Objective**: The objective of the "Assemble" challenge is to correctly configure the hardware components and troubleshoot any technical issues to display the flag on the LCD.

## Solution
To solve the "Assemble" CTF challenge, the following configurations were made:

1. **Wiring Matrix Module to Arduino**:
   - C4 -> 13
   - C3 -> 12
   - C2 -> ~11
   - C1 -> ~10
   - R1 -> ~9
   - R2 -> 8
   - R3 -> 7
   - R4 -> 6

2. **Attach Potentiometer and LCD to Breadboard**:
   - Potentiometer wiring:
     - GND to Blue rail
     - 5V to Red rail
     - I/O - LCD 'VEE'
   - LCD Wiring:
     - VSS to Blue rail
     - VDD to Red rail
     - RS to A0
     - RW to A1
     - E to A2
     - D7 to Blue rail
     - D6 to Red rail
     - D5 to A5
     - D4 to A4
     - D3 to A3

3. **Technical Issues**:
   - Encountered technical issues where the flag would not display on the LCD.
   - Despite the issues, the excons provided the flag as a gesture of completion.
   - You can view it on the video in this directory

        <video controls src="technical issues.mp4" title="Technical Issue"></video>

## Flag
RWSC{XXXXXXXXXX}
