import pandas as pd

x = [2,3,4,5,6,7,8,9]

var = pd.Series(x,index=['a','b','c','d','e','f','g','h'])

print(var)
print(type(var))
print(var[2])
print(var.iloc[2])
