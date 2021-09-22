print('hello world')

print('あいうえお')

print('a', 'bc')
print('d', 'e')

print('1|2|3,4,5')

print('あいうえお')
print('かきくけこ')



capital = '東京'
prefecture = 47

print('日本の首都は',capital)
print('都道府県数は',prefecture)

print('12 + 34 =',12 + 34)

print('98 - 76 =',98 - 76)

print('23 × 45 =',23*45)

print('56 ÷ 14 =',56/14)

print('66 // 9 =',66//9)

print('7 % 3 =',7%3)

print(6*5/2)

print((5+8)*6/2)

print(3*3*3.14)

print('abc',end='')
print('xyz')

a = input('文字列1:')
b = input('文字列2:')
print(a,b,sep='')

print(1+2)
print(7+7/7+7)
print(7+7*7/7+7)
print(7+(7+7*7/7+7))
print(1+2//3-4%5**2)
print(100=="100")

num1 = int(input())
num2 = int(input())
sum = (num1+num2)
print(str(sum))

print('四角形の面積を求めます')
vertical = int(input('縦の長さ:'))
horizontal = int(input('横の長さ'))
area = (vertical*horizontal)
print('四角形の面積:'+ str(area))

print('三角形の面積を求めます')
bottom = int(input('底辺の長さ:'))
height = int(input('高さ:'))
area = (bottom*height/2)
print('三角形の面積:'+str(area))

print('円の面積を求めます')
herf = int(input('半径:'))
PI = 3.14159
area = (herf*herf*PI)
print('円の面積'+str(area))

print('台形の面積を求めます')
upper = int(input('上底の長さ:'))
bottom = int(input('下底の長さ:'))
height = int(input('高さ:'))
area = ((upper+bottom)*height/2)
print('台形の面積'+str(area))

print('税込価格を求めます')
price = int(input('定価:'))
tax = int(input('消費税率:'))
total = (price*(tax/100+1))
print('税込価格'+str(total))

print('BMI値を求めます')
height = int(input('身長(cm):'))
weight = int(input('体重(kg):'))
m = (height*0.01)
bmi = (weight/(m*m))
print('BMI値:'+str(bmi))

humberger = int(input('ハンバーガー:'))
syeik = int(input('シェイク:'))
coke = int(input('コーラ:'))
total2 = (humberger+syeik+coke)
print = ('合計額(税抜):'+str(total2))
tax2 = ((total2*1.1)-total2)
print('消費税:'+str(tax2))
tip = (total2*0.16)
print('チップ:'+str(tip))
all2 = (total2+tax2+tip)
print('合計金額(税込):'+str(all2))











