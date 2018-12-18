## Author: Sridhar Chowdhary  Created on: 18-DEC-2018
## M.Tech AI, CVR college of Engineering
## Under the guidance of Dr. R. Ponnusamy

## This program simulates the behaviour of modal based agent.
## The agent buys paper based on the price of the paper and paper stock available on a given day.
## List price contains price of the paper on a given day


price=[100,120,180,200,150,110,50,70,90,100,150,160,100,120,70,100,120]
stock=[500]
        
class paper_buying_agent:
    def __init__(self):
        self.stockmax=2000
        self.stockmin=200
        self.pricemax=160
        self.extrapurchase=500
        self.normalpurchase=100
        self.big_discount=40
        self.days=len(price)
    def startagent(self):
        for day in range(1,self.days):
            used = random.randint(100,200)
            stock.append(stock[day-1]-used)
            if stock[day] <= self.stockmin:
                stock[day]=stock[day]+self.extrapurchase
            elif price[day] <= self.pricemax:
                if price[day-1]-price[day]>=self.big_discount: 
                    stock[day]=stock[day]+self.extrapurchase
                else:
                    stock[day]=stock[day]+self.normalpurchase
                    
            if stock[day] > self.stockmax:
                stock[day]=self.stockmax
            
        print("Price---Stock")
        for i in range(self.days):
            print(price[i],'---',stock[i])
                


p1 = paper_buying_agent()
p1.startagent()
