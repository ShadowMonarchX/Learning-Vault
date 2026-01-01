class Solustion :
    def arrQuestion(self,arr):
        n = len(arr)
        new_arr = []
        for i in range(-1,-n-1,-1):
            new_arr.append(arr[i])
        return new_arr
            
            
arr = [1,4,3,2]
Solustion = Solustion()
result = Solustion.arrQuestion(arr)
print(result)