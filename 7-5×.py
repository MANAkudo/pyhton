n = 0
c = 101
while True:
    n += 1
    if n >= c:
        break
    if n % 3 == 0:
        continue
    print(n)

#完結ver

n = 1

while n <= 100:
    if n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1
