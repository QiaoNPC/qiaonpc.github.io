---
title: AI 2
description: The objective of the AI 2 challenge is to exploit an LLM's behavior to retrieve the flag.
date: 2024-11-11 00:00:00+0000
categories:
   - PWC HackADay 2024
   - CTF Writeup
tags:
   - AI
weight: 1     
---
# AI 2

## Challenge Information
- **Name**: AI 2  
- **Points**: 150  
- **Category**: AI  
- **Objective**: Manipulate an LLM capable of executing APIs to retrieve the flag.  

## Solution  

1. **Challenge Overview**:  
   - Unlike the first challenge, this LLM can execute **API calls**.  
   - We thought the goal was to leverage this functionality to extract the flag.  

2. **Failed Attempts**:  
   - We initially attempted to manipulate the API calls through various payloads:  
     - **JSON Injection**:  
       - Payload: `{"weather":"true","secret":"true"}`  
     - **SSRF Attempt**:  
       - Payload: `http://localhost/secret`  
   - These attempts failed.  

3. **Successful Approach**:  
   - I applied the **dual-task prompt** concept used in the previous challenge:  
     - By presenting two tasks sequentially, I exploited the LLM's tendency to complete the second task when it fails the first.  
     - This strategy prompted the LLM to reveal the flag indirectly while executing API logic.  


   ![Flag](image.png)