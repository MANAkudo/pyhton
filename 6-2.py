n = 100
sum = 0
i = 1

for i in range(n):
    if n <= 100:
        break
    sum += i
    i += 1
print('合計は',sum,'です')

n = 1
c = 100
t = 0
while n <= c:
    #t=t+nと同じ
    t += n
    n += 1
print('合計:',t)