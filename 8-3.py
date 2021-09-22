num = []
cum = []

for i in range(10):
    sum = int(input(str(i+1) + "件目:整数を入力"))

    if sum % 2 == 0:
        num.append(sum)
    else:
        cum.append(sum)

print("偶数値配列 =　[",num,"]")
print("奇数値配列 =　[",cum,"]")
