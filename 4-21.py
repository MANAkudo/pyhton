n = int(input('国語:'))
c = int(input('数学:'))
t = int(input('英語:'))

if n+c+t >= 230:
    print('合格')
elif n+c+t <= 230 and n+c+t >= 210 and n >= 85 or c >= 85 or t >=85:
    print('合格')
else:
    print('補欠合格')