from nltk.stem.porter import PorterStemmer
import pandas as pd
import numpy as np

stemmer = PorterStemmer()

df = pd.read_csv("dataset.csv")

df['Descrip'] = df['Descrip'].apply(lambda x: stemmer.stem(x.lower())) 

df.to_csv("stem_dataset.csv")
print stemmer.stem("beautiful")



