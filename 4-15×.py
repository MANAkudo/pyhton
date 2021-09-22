print('0~100までの値を2つ入力してください')
n = int(input('1つ目の値:'))
t = int(input('2つ目の値:'))

if n == t:
    print('同じ値です')
else:
    print("大きいほうの値は",n if n > t else t,"です",sep="")