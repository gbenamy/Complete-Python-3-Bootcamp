import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
paint = {'Hearts':'❤️','Diamonds':'♦️', 'Spades':'♠️', 'Clubs':'♣️'}
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
            '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}



class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '|' + self.rank + paint[self.suit] +'|'
    


c1 = Card('Hearts', '5')
temp = print (c1)
print (temp)


class Deck:

    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()
    


d1 = Deck()
d1.shuffle()

for i in range(5):
    print(d1.deal_card())