n = int(input('4桁の西暦:'))

if n % 4 == 0 and n % 400 ==0:
    print('閏年です')
elif n % 100 == 0:
    print('平年です')