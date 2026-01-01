def Any() :
    for i in range(50000000) :
        yield i
gen = Any()
print(next(gen))

for j in gen :
    print(j)