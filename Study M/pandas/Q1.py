import pandas as pd

cse_dict = {
'name':['vishal','kavit','manish','milan','amit','tushar'],
'iq':[100,50,120,80,0,0],
'marks':[80,60,100,70,10,0],
'package':[10,7,14,20,0,0]
}
cse = pd.DataFrame(cse_dict)
cse.set_index('name',inplace=True)
print(cse)
print("*"*50)
print(cse.columns)