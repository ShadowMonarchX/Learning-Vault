class Solustion :
    def maxSecond(self,num) :
        sum1 = 0
        sum2 = 0
        n = len(num)
        for i in range(0,n) :
            sum1 += num[i][i]
            sum2 += num[i][n-i-1]
        return sum1-sum2
 
num = [[1,2,3],[3,4,5],[1,2,3]]
Solustion = Solustion()
result = Solustion.maxSecond(num)
print(result)