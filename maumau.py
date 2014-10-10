#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Card(object):
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def isPlayable(self, other):
        return self.color == other.color or self.value == other.value

    #To be printable in print(card)
    def __str__(self): 
        return '{} {}'.format(self.color, self.value)
    #To be printable in print(listOfCards)
    def __repr__(self):
        return str(self)

class Deck32(list):
    VALUES = ["7","8","9","10","Bube", "Dame", "Koenig", "As"]
    COLORS = ["Karo", "Herz", "Pik", "Kreuz"]
    
    def __init__(self):
        cards = []
        for color in self.COLORS:
            for value in self.VALUES:
                cards.append(Card(color, value))
        
        random.shuffle(cards) #TODO
        list.__init__(self, cards)

class Player(object):

    def __init__(self, name, deck):
        self.name = name
        self.cards = []
        for i in range(6):
            self.cards.append(deck.pop())
    
    def play(self, pile, deck):
        pass
    
    def draw(self, deck):
        self.cards.append(deck.pop())
        
    #def playableCards(self, pile, deck):
    #    pCards = []
    #    for c in self.cards:
    #        if c.isPlayable()

class ComputerPlayer(Player):
    #def __init__(self, name, deck):
    def play(self, pile, deck):
        nbrCards = len(self.cards)
        for c in self.cards:
            if c.isPlayable(pile[len(pile)-1]):
                pile.append(c)
                self.cards.remove(c)
                #print(c, "is played by ", player.name)
                break
        if nbrCards == len(self.cards): #no card was played
            self.draw(deck)
            print("Need to draw.")

class HumanPlayer(Player):
    
    def play(self, pile, deck):
        playableCards = []
        for c in self.cards:
            if c.isPlayable(pile[len(pile)-1]):
                playableCards.append(c)
                
        if (len(playableCards) == 0):
            self.draw(deck)
            print("No card can be played.")
            #print(self.cards[len(self.cards)-1], " is drawn.")
            print("{} is drawn.".format(self.cards[len(self.cards)-1] ))
        else:
        
            print("The pile's top card: {}".format(pile[len(pile)-1]))
            print("Your cards: ")
            print(self.cards)
            print("The following cards are playable: ")
            print(playableCards)
            #TODO: I/O
            cardNumber = input("Select a card by typing its number.")
            c = playableCards[cardNumber]
            pile.append(c)
            self.cards.remove(c)




"""
let the 'Mau Mau Game' begin
"""

deck = Deck32()
print(len(deck))
pile = [deck.pop()]
players = [ComputerPlayer("Computer1", deck),
              ComputerPlayer("Computer2", deck),
              HumanPlayer("Jo", deck)
]

endOfGame = False
while not endOfGame:
    for p in players:
        print(p.name, "'s turn.")
        #If the deck is empty, rebuild the deck
        if len(deck) == 0:
            while (len(pile) > 1):
                deck.append(pile.pop())
            random.shuffle(deck)
            print("New deck.")
        p.play(pile, deck)
        if len(p.cards) == 0:
            endOfGame = True
            print(p.name, "won the game.")
            #print(pile[0])
            break
        
