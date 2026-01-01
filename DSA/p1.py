import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columns_data = ["student_id","age"]
    out = pd.DataFarme(student_data,columns=columns_data)
    return out

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
result = createDataframe(student_data)
print(result)