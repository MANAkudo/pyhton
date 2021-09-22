def all(num):
    tatal = 0

    for i in range(len(num)):
        cum = num[i]

        if type(cum) is int:
            tatal += cum
    return tatal

youso = [4,10,679,3994,6789,19324]

tatal = all(youso)


print("合計値 =",tatal)