def ensyu(num):
    result = num * 2 * 3.14
    return result

def menseki(num):
    result = num * num * 3.14
    return result


n = float(input("半径を入力してください:"))



ensyu_result = ensyu(n)
menseki_result = menseki(n)

print("半径",n,"の円周は","{:3f}".float(ensyu_result))
print("半径",n,"の面積は","{:3f}".float(menseki_result))