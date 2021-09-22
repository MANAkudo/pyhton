print('合計点と平均点を求めます')
n = int(input('学生の人数:'))

tnsu = [None] * n

for i in range(n):
    tnsu[i] = int(input('{}番の点数'.format(i + 1)))

sum = 0
for i in range(n):
    sum += tnsu[i]

print('合計は{}点です'.format(sum))
print('平均は{}点です'.format(sum / n))

