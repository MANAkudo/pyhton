n = int(input('開始数:'))
t = int(input('終了数:'))
sum = 0
num = 0

for i in range(n,t):
    if i == t:
        break
    sum = n + num
    num += n
    n += 1
print('合計:',sum)