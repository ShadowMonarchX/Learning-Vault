import pandas as pd
import numpy as np

x = pd.read_csv("data.csv")
print("hello 1")
print(x)
print("hello 2")
print(x.head())
print("hello 3")
z = pd.DataFrame(x)
print(z)
print("hello 4")
q = x[x['Year'].astype(str).str.startswith('2021')]
print(q)
print("hello 5")
print(z.loc[[10,150]])
print()

