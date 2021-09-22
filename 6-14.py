n = int(input("入力値:"))
cum = True

for i in range(2,n):
    if n % i == 0:
        print(str(n),"は素数ではありません")
        cum = False
        break

if cum:
    print(str(n),"は素数です")
