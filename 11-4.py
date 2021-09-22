import random

class Coincase:
    def __init__(self) -> None:
        self.coins = {1:0,5:0,10:0,50:0,100:0,500:0}

    def add_coin(self,type:int,count:int) -> None:
        self.coins[type] += count

    def get_coin_count(self,type:int) -> int:
        return self.coins[type]

    def get_amount(self) -> int:
        total = 0

        for type,count in self.coins.items():
            total += type * count

            return total
coincase = Coincase()
