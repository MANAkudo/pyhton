try:
    num1 = int(input("整数1:"))
    num2 = int(input("整数2:"))

    print(num1,"/",num2,"=",num1 / num2)
except ZeroDivisionError:
    print("0による割り算です!")
finally:
    print("処理終了")