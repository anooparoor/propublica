#Code to clean the Expands16.txt file and create a training dataset for expenditure classifier
#6539579
import pandas as pd
import numpy as np
import random

filename = "expends16.txt"

n = sum(1 for line in open(filename)) - 1
sample = 10000

print n

skip = sorted(random.sample(xrange(n),n-sample))
df = pd.read_csv(filename, skiprows=skip, quotechar='|')
df.replace(r'\s+', np.nan,regex=True, inplace=True)
df.replace('',np.nan, inplace=True) 
print df.shape
print df.iloc[10]

df.to_csv("data.csv")
