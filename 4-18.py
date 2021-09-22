n = int(input('0~100までの国語の得点を入力してください'))

if n >= 80:
    t = int(input('0~100までの英語の得点を入力してください'))
else:
    c = int(input('0~100までの数学の得点を入力してください'))

if t or c >= 80:
    print('合格です')
else:
    print('不合格です') 