print('整数値を３つ入力して下さい')
n = int(input('1つ目の値:'))
c = int(input('2つ目の値:'))
t = int(input('3つ目の値:'))

if n == t == c:
    print("同じ値です")
else:
    print('最大の値は',max(n,t,c),'です')
