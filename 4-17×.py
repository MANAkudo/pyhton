print('0~100までの得点を２つ入力してください')
n = int(input('1つ目の得点:'))
t = int(input('2つ目の得点:'))

   
if n == t:  
    print(n)
else:
    print(n if n > t else t)
    print(t if n > t else n)

