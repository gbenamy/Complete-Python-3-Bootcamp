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
c2 = Card('Clubs', '6')
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
    #TODO need to check if there are cards to deal, if not, need a new deck


d1 = Deck()
d1.shuffle()

for i in range(5):
    print(d1.deal_card())



class Player:
    def __init__(self,name,chips):
        self.name = name
        self.chips = chips
    
    def __str__(self):
        return f'Player {self.name} has {self.chips}$'
    
    def increaseFunds(self,num):
        self.chips+=num
    
    def decreaseFunds(self,num):
        self.chips-=num

    def getFunds(self):
        return int(self.chips)
    

p1 = Player("p1",200)

print (p1)
print (p1.getFunds())
p1.increaseFunds(20)
p1.decreaseFunds(3)


def printHand(c1,c2):
    if c1 == '**':
        print('|**|')
    else:
        print(c1)
    print(c2)


printHand('**',c2)


gameOn = True
name = input("Please enter your name:")
chips = input("Please enter the amount of chips:")
#TODO input validation
p1 = Player(name,chips)
d1 = Deck()
d1.shuffle()
p1_c1=d1.deal_card()
dealer_c1=d1.deal_card()
p1_c2=d1.deal_card()
dealer_c2=d1.deal_card()

print(dealer_c2)

while (gameOn):
    p1c1=

   