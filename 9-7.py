def hantei(num,cum):

    resuit = False

    for i in range(len(num)):
        ttt = num[i]

        if cum == ttt:
            resuit == True
            break
    return resuit

n = int(input("整数を入力してください:"))

nums = [4,10,59,679,1991,3994,6789,19324]

resuit = hantei(nums,n)

if resuit:
    print(n,"配列に含まれています")
else:
    print(n,"配列に含まれていません")


