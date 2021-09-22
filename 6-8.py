n = 9

for i in reversed(range(1,10)):
    print(n,'の段')
    n -= 1
    for j in reversed(range(1,10)):
        print(i,'×',j,'=',i * j)
    print()