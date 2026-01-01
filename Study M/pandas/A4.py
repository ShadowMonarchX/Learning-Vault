import pandas as p 
 
a = [1,2,3,4]

b = p.Series(a , index = ["x","y","z","k"])
print(b["y"])