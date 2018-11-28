import csv
import random

import numpy as np
import pandas as pd

df = pd.read_csv('blogdata.csv', sep="\t", quoting=csv.QUOTE_NONE)#, index_col=False)

# print(df.values)

# df = pd.DataFrame(df)
print(df.corrwith(df, axis=1))

# amount of clusters, speicified by assignment
cluster_amount = 5

words = df.columns.values
blogs = []
words_rand = []

# Get blog names
for word in words:
    if word == 'Blog':
        blogs.append(df[word])
        continue
    maxN = max(df[word])
    minN = min(df[word])
    words_rand.append([word, random.randint(minN, maxN)])

# 5 random cluster points
centroids = random.sample(words_rand, cluster_amount)

# Calculation pearson inbetween blogs using pearson

for word in df:
    if word == 'Blog':
        print(word)
        continue;
    # Clac centroid

