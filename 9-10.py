import math
def bmi(kg,cm):
    result = kg / (cm*0.01)*(cm*0.01)
    return result

def weight(cm):
    result2 = (cm*0.01)*(cm*0.01)*22
    return result2

higt = float(input("身長(cm)を入力してください:"))
wei = float(input("体重(kg)を入力してください"))

bmi_result = bmi(higt,wei)
weight_result = weight(higt)

print("BMI値は",math.floor(bmi_result),"です")
print("適正体重は",math.floor(weight_result),"kgです")
