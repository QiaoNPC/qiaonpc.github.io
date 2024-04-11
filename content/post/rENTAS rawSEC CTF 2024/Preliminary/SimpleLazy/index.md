---
title: SimpleLazy
description: The challenge involves exploiting a Local File Inclusion (LFI) vulnerability to retrieve a flag.
date: 2024-03-09 00:00:00+0000
categories:
   - rENTAS rawSEC CTF 2024
   - CTF Writeup
tags:
   - Web
weight: 1     
---
# SimpleLazy CTF Challenge Writeup

## Challenge Information
- **Name**: SimpleLazy
- **Points**: 330
- **Category**: Web
- **Objective**: The challenge involves exploiting a Local File Inclusion (LFI) vulnerability to retrieve a flag.

## Solution
Here's a detailed solution for the SimpleLazy CTF challenge:

1. **Initial Assessment**:
   - Immediately recognized the challenge as having a Local File Inclusion (LFI) vulnerability, particularly with the `page3.php` parameter.
   - Discovered that input was always appended with `.php`, limiting directory traversal options.



      ![Initial Page](<initial page.png>)

2. **Strategy for Exploitation**:
   - Focused on extracting PHP source code from `index.php`, `page1.php`, `page2.php`, and `page3.php`.
   - Utilized `php://filter` to retrieve PHP files in base64 format, allowing for remote file inclusion.



        ![LFI](<part 1.png>)

3. **Exploiting the LFI**:
   - Retrieved the source code of `page3.php` using `php://filter`.
   - Discovered the inclusion of a suspicious file in the PHP source code.



        ![LFI](<part 1 1.png>)

4. **Retrieving the Flag**:
   - Applied the same `php://filter` technique to extract the suspicious file's contents in base64 format.
   - Decoded the contents of the suspicious file to reveal the flag.



        ![LFI](<part 2.png>)


        ![Flag](<part 2 2.png>)

## Conclusion
The SimpleLazy CTF challenge demonstrated the importance of understanding LFI vulnerabilities and using techniques like `php://filter` to retrieve PHP source code and extract hidden files. By exploiting the vulnerability and decoding the suspicious file's contents, the flag was successfully obtained, completing the challenge.