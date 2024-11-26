---
title: Oren
description: The objective of the "Oren" challenge is to exploit the target machine and retrieve the flag.
date: 2024-11-24 00:00:00+0000
categories:
   - SherpaCTF 2024
   - CTF Writeup
tags:
   - Boot2Root
weight: 1     
---
# Oren

## Challenge Information
- **Name**: Oren  
- **Points**: 100  
- **Category**: Boot2Root  
- **Objective**: Exploit the target machine and retrieve the flag.  

## Solution  

1. **Initial Connection**:  
   - Connected the local challenge machine to NAT and used **netdiscover** to identify its IP address.  

      ![Netdiscover](netdiscover.png)

2. **Enumeration**:  
   - Scanned the machine using **nmap**:  
     - Found that we are attacking a **Windows machine**.


      ![nmap](nmap.png)

   - Explored the web application on port `8080`:
     - Discovered `admin.php`, `phpinfo.php`, and `index.php` using **feroxbuster**.
     - Attempted **SQL injection** on `admin.php` using **sqlmap**, but it failed.


      ![Feroxbuster](web-enum.png)


      ![index page](index_php.png) 

      
      ![admin page](admin_php.png) 

      
      ![phpinfo](phpinfo_php.png)

3. **Kerberos Enumeration**:  
   - Re-scanned using **nmap** for potential users.  
   - Found usernames but failed to crack them via password spraying or brute-forcing the login page.


      ![Users](kerberoastable.png)

4. **Exploit Development**:  
   - Found PHP version `8.1.25` from `phpinfo.php`.
   - Searched for related exploits but none of the existing POCs worked.  
   - The challenge hint suggested focusing on the title **Oren**, which led to discovering an exploit for **PHP 8.1.25 "orange"**.


      ![Orange](<php orange.png>)


      ![POC Orange](<php orange poc.png>)

5. **Gaining Access**:  
   - Used the **PHP 8.1.25 orange exploit** to gain access as the `webadmin` user.  

6. **Privilege Escalation**:  
   - Enumerated the box and discovered files related to the flag.  
   - Found a **PowerShell script** that, when executed, revealed the password for `user.zip`.  
   - Unzipped the archive to retrieve the flag.


      ![Files related to flag](<files related to flag.png>)

      ![PS1 Script](<ps1 script.png>)

      ![Running PS1 script](<running ps1 script.png>)

      ![Flag](flag.png)

## Flag  
- **Flag**: `SHCTF24{XXXXXXXXXX}`  
