import matplotlib as mat
import pandas as pd
import random as rd
import numpy as np

df = pd.read_csv('pokemon_data.csv')
cols = list(df.columns.values)
df2 = df[cols[0:4]+[cols[-1]]+cols[4:12]]

print(df2[:,5])

end = 'end'



