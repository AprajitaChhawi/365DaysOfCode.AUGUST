def pattern(n):
    for i in range(1,n-4):
        for j in range(i+1,n-3):
            print("A",end=" ")
        for k in range(2*i-1):
            print(" ",end=" ")
        for l in range(i+1,n-3):
            print("A",end=" ")
        print()
    for i in range(n-5,0,-1):
        for j in range(i+1,n-3):
            print("A",end=" ")
        for k in range(2*i-1):
            print(" ",end=" ")
        for l in range(i+1,n-3):
            print("A",end=" ")
        print()
pattern(11)
