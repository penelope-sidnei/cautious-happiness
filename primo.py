n=100
for x in range(n):
    for y in range(2,x):
        if x%y ==0:
            break
        else:
            print(x)
            break
