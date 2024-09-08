---
title: My First Blog
description: Exploit an SQL injection vulnerability to retrieve admin credentials and obtain the flag.
date: 2024-09-08 00:00:00+0000
categories:
   - FSIIECTF 2024
   - CTF Writeup
tags:
   - Web
weight: 1     
---
# My First Blog CTF Challenge Writeup

## Challenge Information
- **Name**: My First Blog
- **Points**: 1
- **Category**: Web
- **Objective**: Exploit an SQL injection vulnerability to retrieve admin credentials and obtain the flag.

## Solution
To solve the "My First Blog" challenge, follow these steps:

1. **Identifying the Vulnerability**:
   - The challenge hints at an SQL injection vulnerability.
   - Direct use of SQLmap is not possible, so manual enumeration is necessary.

2. **Initial Enumeration**:
   - Perform basic enumeration to identify potential SQL errors and found that it might be an SQLite database


      ![Potential SQLite](<potential sqlite.png>)

3. **SQL Injection Exploration**:
   - Test for SQL injection vulnerabilities by injecting payloads into input fields or URL parameters.
   - Use basic UNION-based SQL injection techniques to determine the number of columns in the SQL queries.


      ![Enumerate Columns](<enumerate the columns.png>)


      ![Found Number of Columns](<found number of columhns.png>)

4. **Finding Tables**:
   - Once the number of columns is identified, proceed with UNION-based queries to list tables.
   - Identify a table named `users`.


      ![Found Table](<find table.png>)

5. **Enumerating Columns**:
   - Enumerate the columns in the `users` table to find useful information.
   - Identify columns such as `id`, `username`, `password`, `email`, and `role`.


      ![Found Columns](<find columns.png>)

6. **Retrieving Admin Credentials**:
   - Extract the credentials of the admin user from the `users` table.
   - Use SQL injection to retrieve and view the admin credentials.

7. **Flag Retrieval**:
   - Submit the retrieved admin credentials as the flag in the format `FSIIECTF{XXXXXXXXXX}`.


      ![Flag](<found flag.png>)

