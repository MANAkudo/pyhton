n = 0
t = 1
sum = 0

while True:
    if sum >= 1000:
        break
    sum = n + t
    print(sum,end='')
    n = t + sum
    print(n,end='')
    t = sum + n
    print(t,end='')
