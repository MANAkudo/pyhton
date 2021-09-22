class aaa:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def keisan(self) -> int:
        sum = 0
        for i in range(self.x,self.y+1):
            #yも含めるなら+1をする
            sum += i

        return sum

class Main:
    def bbb(self) -> None:
        AAA = aaa(100,200)

        all = AAA.keisan()

        print("{}から{}までの合計値は{}です".format(AAA.x,AAA.y,all))  

main = Main()
main.bbb()

