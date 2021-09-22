class aaa:
    def __init__(self,x,y):
        self.value = x
        self.result = y
    
    def keisan(self) -> int:
        sum = 0
        for i in range(self.value,self.result+1):
            #yも含めるなら+1をする
            sum += i

        return sum

class Main:
    def bbb(self) -> None:
        AAA = aaa(100,200)

        all = AAA.keisan()

        print("{}から{}までの合計値は{}です".format(AAA.value,AAA.result,all))  

main = Main()
main.bbb()

