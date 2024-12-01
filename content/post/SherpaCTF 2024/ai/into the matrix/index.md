---
title: Into The Matrix
description: The objective of the Into The Matrix challenge is to decode the contents of an NPY file to retrieve the flag.
date: 2024-11-24 00:00:00+0000
categories:
   - SherpaCTF 2024
   - CTF Writeup
tags:
   - AI
weight: 1     
---
# Into The Matrix

## Challenge Information
- **Name**: Into The Matrix  
- **Points**: 100  
- **Category**: AI  
- **Objective**: Decode the contents of an NPY file to retrieve the flag.  

## Solution  

1. **Initial Inspection**:  
   - Given an **NPY file** in CTF, a common format for storing NumPy arrays, the first step is to **visualize** its contents.  

2. **Visualization**:  
   - Loaded the NPY file into Python using NumPy:  
     ```python
      import numpy as np
      import matplotlib.pyplot as plt
      from sklearn.manifold import MDS
      from tqdm import tqdm

      file_path = 'matrix.npy'
      data = np.load(file_path)

      print("Data shape:", data.shape)

      mds = MDS(n_components=2, dissimilarity='precomputed', n_init=4, random_state=42)

      for _ in tqdm(range(2), desc="Performing MDS", total=2):
          pos = mds.fit_transform(data)

      plt.figure(figsize=(10, 10))

      plt.scatter(pos[:, 0], pos[:, 1], c='blue', label='Signal Origins')

      plt.xlabel('MDS Component 1')
      plt.ylabel('MDS Component 2')
      plt.title('MDS Visualization of Distance Matrix')
      plt.legend()

      plt.show()
     ```
   - I wasn't able to figure out what the graph meant, but my teammate **Nem4ros** suggested that it appeared to be **SHCTF24{intro_to_ml}**, but submitting this flag failed.  


      ![Hints of Flag](<hints of flag.png>)

3. **Brute Forcing Variations**:  
   - Since whe know what the the flag approximately look like, we brute forced the flag, including:
     - `SHCTF24{intr0_to_ml}`  
     - `SHCTF24{1ntro_to_ml}`  
     - `SHCTF24{intro_to_ml}`  
     - ...
   - Eventually, one of these variations worked as the valid flag.

## Flag  
- **Flag**: `SHCTF24{XXXXXXXXXX}`  
