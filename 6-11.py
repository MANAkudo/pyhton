print('長方形を描写します')
print('2~20までの整数値を入力してください')

n = int(input('行数の入力:'))
t = int(input('列数の入力:'))

if n and t < 2 and n and t > 20:
    print('値が正しくありません')
print()

for i in range(n):
    print()
    for j in range(t):
        print('*' , end='')
print()
