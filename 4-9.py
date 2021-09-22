print('0~100までの得点を２つ入力してください')
n = int(input('1つ目の得点:'))
t = int(input('2つ目の得点:'))

if n or t >= 80:
    print('合格です')
else:
    print('不合格です')