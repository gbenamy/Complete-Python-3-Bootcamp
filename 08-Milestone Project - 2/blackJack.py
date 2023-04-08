import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
paint = {'Hearts':'❤️','Diamonds':'♦️', 'Spades':'♠️', 'Clubs':'♣️'}
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':10}



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
    hand=[]
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
    
    def newHand (self):
        self.hand=[]

    def newCard (self,card):
        self.hand.append(card)
    
    def getHand(self):
        return self.hand
    

p1 = Player("p1",200)

print (p1)
print (p1.getFunds())
p1.increaseFunds(20)
p1.decreaseFunds(3)


def printHand(cards):
    for card in cards:
        if card == '**':
            print('|**|')
        else:
            print(card)


def checkHand(cards):
    val = 0
    hasAce = 0
    for card in cards:
        if card.rank=='A':
            hasAce+=1
        val += values[card.rank]

    if not hasAce:
        return val
    else:
        if val == 20:
            return 21
        if val > 21:
            for instance in range(hasAce):
                val-=9
                if val<=21:
                    return val
        return val




#gameOn = True
#name = input("Please enter your name:")
#chips = input("Please enter the amount of chips:")
#TODO input validation
p1 = Player('tom',200)
d1 = Deck()
d1.shuffle()

p1.newHand()
#p1.newCard(d1.deal_card())
#p1.newCard(d1.deal_card())
#p1.newCard(d1.deal_card())


c1 = Card('Hearts', '2')
c2 = Card('Clubs', 'A')
c3 = Card('Hearts', 'A')

p1.newCard(c1)
p1.newCard(c2)
p1.newCard(c3)


printHand(p1.getHand())
print(checkHand(p1.getHand()))


gameOn=False #testing

while (gameOn):
    pass
   