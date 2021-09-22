print('合計点と平均点を求めます')
print('注:"End"で終了')

n = 0
tnsu = []

while True:
    s = int(input('{}番の点数'.format(n + 1)))
    if s == 'End':
        break
    tnsu.append(int(s))
    n += 1

total = sum(tnsu)

print('合計は{}点です'.format(total))
print('平均は{}点です'.format(total / n))

