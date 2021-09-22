import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
num4 = random.randint(0,9)

print(num1,"+",num2,"×",num3,"-",num4)
t = num1 + num2 * num3 - num4
n = int(input("計算結果は？:"))

if t == n:
    print("正解です！")
else:
    print("不正解です。正解は",t,"です。")