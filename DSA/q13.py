def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def sortest(myArray) :
    sz = len(myArray)
    start = 0 
    end = sz - 1
    while(start < end ) :
        myArray[start] , myArray[end] = myArray[end] , myArray[start]
        start += 1
        end -= 1
    return myArray
myArray = [1, 30, 24, 7, 9, 11, 13, 15, 17, 19]

r1 = sortest(myArray)
print(r1)
myTarget = 15
#