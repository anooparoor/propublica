#Code to clean the Expands16.txt file and create a training dataset for expenditure classifier
#6539579
import pandas as pd
import numpy as np
import random

filename = "expends16.txt"

n = sum(1 for line in open(filename)) - 1
sample = 100000

print n
skip = sorted(random.sample(xrange(n),n-sample))
df = pd.read_csv(filename, skiprows=skip, quotechar='|')
df.replace(r'\s+', np.nan,regex=True, inplace=True)
df.replace('',np.nan, inplace=True)
df.columns=['cycle','id','transid','crpfilterid','recipcode','pacshort','crprecipname','expcode','amount','date','city','state','zip','cmtelid_ef','candid','type','descrip','pg','elecother','enttype','source']

df_n = df[df.expcode.notnull() & df.descrip.notnull()]
 
print df_n.shape
print df_n.iloc[10]

df_n.to_csv("data.csv")
