---
title: IPORTE
description: Exploit a vulnerability to retrieve information about other users, including the flag.
date: 2024-09-08 00:00:00+0000
categories:
   - FSIIECTF 2024
   - CTF Writeup
tags:
   - Web
weight: 1     
---
# IPORTE CTF Challenge Writeup

## Challenge Information
- **Name**: IPORTE
- **Points**: 1
- **Category**: Web
- **Objective**: Exploit a vulnerability to retrieve information about other users, including the flag.

## Solution
To solve the "IPORTE" challenge, follow these steps:

1. **Initial Exploration**:
   - The challenge page provides functionality to register and log in.
   - Register an account to obtain a base64 encoded string.


      ![Register for Account](<register for acc.png>)

2. **Decoding the Base64 String**:
   - Decode the base64 encoded string received after registration.
   - The decoded string reveals your username and the registration date.

3. **Exploiting the Information Retrieval Functionality**:
   - Note that it’s possible to retrieve information about other users by using their base64 encoded strings.
   - You can send a POST request with a base64 encoded string to get details of other users.

4. **Retrieving the Admin Information**:
   - Obtain the base64 encoded string for the admin user.
   - Send a POST request with this encoded string to get the admin's details.


      ![Admin String](<get admin base64 string.png>)

5. **Getting the Flag**:
   - Retrieve the flag from the admin's information or as part of the response to the request.


      ![Flag](flag.png)

