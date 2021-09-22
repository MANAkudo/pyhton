n = 10

for i in reversed(range(1,10)):
    n -= 1
    if n % 2!= 0:
        print(n,'の段')
    for j in reversed(range(1,10)):
        if i % 2 != 0:
            print(i,'×',j,'=',i * j)
    print()