---
title: Linux Memory Usage
description: The objective of the Linux Memory Usage CTF challenge is to efficiently manage and process memory usage data for different processes based on given inputs.
date: 2023-12-17 00:00:00+0000
categories:
   - Student Wargames 2023
   - CTF Writeup
tags:
   - Leet Code
weight: 1     
---
# Linux Memory Usage - CTF Challenge Writeup

## Challenge Information
- **Name**: Linux Memory Usage
- **Category**: PPC / Leet Code
- **Objective**: The objective of the "Linux Memory Usage" CTF challenge is to efficiently manage and process memory usage data for different processes based on given inputs.

## Solution
Encountering a Leet Code challenge within a CTF was an interesting experience. Here's how I tackled it:

1. **Understanding Inputs**:
   - This was my first encounter with a Leet Code style challenge in a CTF context, very very fun.
   - The problem consisted of three types of inputs:
     1. Variables N and Q: Representing the number of processes and queries.
     2. Processes' Data: Including process id, parent process id, and memory usage.
     3. Queries: Containing necessary information for further analysis.

2. **Memory Mapping**:
   - Utilizing the received inputs, I structured the memory by creating a dictionary.
   - The dictionary's key-value pairs were organized to represent parent processes and their corresponding children processes, facilitating efficient data retrieval.

3. **Handling Queries**:
   - Processing queries involved reading and parsing the data structure I coded to provide the desired output efficiently.


      ![Flag](flag.png)


      ```python
      from collections import defaultdict

      def calculate_memory_usage(p, q):
          children = defaultdict(list)
          memory = {}

          for a, b, c in p:
              memory[a] = c
              if b != 0:
                  children[b].append(a)

          memo = {}
          results = []

          for query in q:
              stack = [query]
              total_memory = 0

              while stack:
                  current_pid = stack.pop()
                  if current_pid in memo:
                      total_memory += memo[current_pid]
                      continue

                  total_memory += memory[current_pid]
                  children_list = children[current_pid]

                  for child in children_list:
                      stack.append(child)

              results.append(total_memory)
              memo[query] = total_memory

          return results

      N, Q = map(int, input().split())
      p = [list(map(int, input().split())) for _ in range(N)]
      q = [int(input()) for _ in range(Q)]

      results = calculate_memory_usage(p, q)
      for result in results:
          print(result)
      ```

## Flag
The flag for this challenge is: `wgmy{XXXXXXXXXX}`.

This writeup demonstrates the process of efficiently managing and processing memory usage data in the "Linux Memory Usage" CTF challenge using appropriate data structures and systematic query handling. For any further inquiries or clarifications, feel free to ask.
