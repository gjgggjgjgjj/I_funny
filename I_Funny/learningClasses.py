'''
def Wallet():
    o = Object()
    Wallet.__init__(o)
    return
    
    
def Pencil(num_leads):
    o = Objects()
    Pencil.__init__(o, num_leads)
    return o
'''
#self is the "selves" object
class Wallet:
    
    def __init__(self):
        self.cash = 0.0
        self.cards = []
        
    def total_cash(self):
        return self.cash
    
    def insert_cash(self, more_cash):
        self.cash += more_cash
        
        
        
w = Wallet()
print(w.total_cash())
w.insert_cash()