# sorting to arrays
thislist = ["apple", "banana", "cherry"]
thislist.sort()
a = str(input("Enter Fruit Name :"))
for i in range(len(thislist)):
    if thislist[i]==a :
        print(thislist[i])
        break
    else :
        print("This Data In no This List ")
        break