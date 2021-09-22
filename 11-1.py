import math
class Circle:
    PI = 3.1415

    def aaa(self,hankei):
        ensyuu = hankei * 2 * Circle.PI
        return math.floor(ensyuu * 10 **3) / (10 **3)
    
    def  area(self,hankei):
        res = hankei ** 2 * Circle.PI
        return math.floor(res * 10 **3) / (10 ** 3)

class Main:

    def execute(self):
        circle = Circle()
        hankei = int(input("半径を整数値で入力:"))
        aaa_a = circle.aaa(hankei)

        area_a = circle.area(hankei)

        print("円周の長さは{}です".format(aaa_a))
        print("円の面積は{}です".format(area_a))

main = Main()
main.execute()