---
title: iamspeed
description: The objective of the iamspeed challenge is to analyze the Python-compiled executable to retrieve and decode the flag.
date: 2024-11-24 00:00:00+0000
categories:
   - SherpaCTF 2024
   - CTF Writeup
tags:
   - Reverse Engineering
weight: 1     
---
# iamspeed

## Challenge Information
- **Name**: iamspeed  
- **Points**: 100  
- **Category**: Reverse  
- **Objective**: Analyze the Python-compiled executable to retrieve and decode the flag.  

## Solution  

1. **Initial Enumeration**:  
   - Upon inspecting the executable, it was identified as a **Python-compiled executable** based on the presence of Python-related artifacts.  


      ![Initial Enumeration](<initial enumeration.png>)

2. **Decompiling the Executable**:  
   - **Tools Used**:  
     - **PyInstaller Extractor** (`pyinstxtractor`) to extract the `.pyc` file.  
     - **PyCDC** to decompile the `.pyc` file into readable Python source code.  


     ![Pyinstractor](pyinstractor.png) 

     ![PYCDC](pycdc.png)

3. **Analyzing the Decompiled Script**:  
   - My teammate, **Nem4ros** then ran the script and found hints of **hidden HTTPS link**.  
   - He then modified the script to print the extracted link directly.  

      ![Hints of HTTP](<found hints of http.png>)


      ![HTTP Link](<http link.png>)

4. **Accessing the Link**:  
   - The link pointed to a Google document containing **encoded text**.  


      ![Get Another Code](<get another code.png>)

5. **Decoding the Text**:  
   - Attempts to decode the text with standard methods like **hex decoding** failed.  
   - The text was successfully decoded using the **original script** to process the encoded data.  


      ![Flag](flag.png)

## Flag  
- **Flag**: `SHCTF24{XXXXXXXXXX}`  
