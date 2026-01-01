import pandas as p
a = ["a","b","c","d","e"]
b = [1,2,3,4,5]
my = {'cars' : a,
      'passing' : b}
a =p.DataFrame(my)
print(a)
print(a.loc[0,1])


xm = {"d1" : 1,"d2" : 2,"d3" : 3}
z = p.Series(xm)
print(z)