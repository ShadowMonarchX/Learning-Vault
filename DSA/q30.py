class Solustion :
    def maxSecond(self,num) :
        n = len(num)
        first = second = float("-inf")
        for i in num:
            if i > first :
                first = i
        for i in num :
            if i > second and first > i :
                second = i
        return second

num = [3,1,2,1,2,4,4,6,6,6]
Solustion = Solustion()
result = Solustion.maxSecond(num)
print(result)