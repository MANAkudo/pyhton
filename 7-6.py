n = 0
sum = 0
t = 0

while True:
    n = int(input('整数を入力:'))
    if n == 0:
        break
    sum += n
    t += 1
print('合計値:',sum)
print('平均値:',sum % t+1)
    
