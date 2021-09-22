n = int(input('0~100までの得点を入力してください'))

if n == 100:
    print('満点合格です')
elif n <= 100 and n >= 60:
    print('合格です')
else:
    print('不合格です')