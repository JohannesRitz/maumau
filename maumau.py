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
        return '{} of {}'.format(self.value, self.color)
    #To be printable in print(listOfCards)
    def __repr__(self):
        return str(self)

class Deck32(list):
    VALUES = ["7","8","9","10","Jack", "Queen", "King", "Ace"]
    COLORS = ["diamonds", "hearts", "spades", "clubs"]
    
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
    
    def play(self, pile, deck, game):
        pass
    
    def draw(self, pile, deck):
        #If the deck is empty, rebuild the deck
        if len(deck) == 0:
            while (len(pile) > 1):
                deck.append(pile.pop())
            random.shuffle(deck)
            print("New deck.")
        self.cards.append(deck.pop())
        
    def playCard(self, card, pile):
        pile.append(card)
        self.cards.remove(card)
        

class ComputerPlayer(Player):

    def play(self, pile, deck, game):
        nbrCards = len(self.cards)
        for c in self.cards:
            if c.isPlayable(pile[len(pile)-1]):
                self.playCard(c, pile)
                game.effectActive = (c.value == "8")
                #print(c, "is played by ", player.name)
                break
        if nbrCards == len(self.cards): #no card was played
            self.draw(pile, deck)
            print("Need to draw.")

class HumanPlayer(Player):
    
    def play(self, pile, deck, game):
        playableCards = []
        for c in self.cards:
            if c.isPlayable(pile[len(pile)-1]):
                playableCards.append(c)
                
        if (len(playableCards) == 0):
            self.draw(pile, deck)
            print("No card can be played.")
            #print(self.cards[len(self.cards)-1], " is drawn.")
            print("{} is drawn.".format(self.cards[len(self.cards)-1] ))
            try:
                input("Press Enter to continue. ")
            except SyntaxError:
                pass
        else:
        
            print("The pile's top card: {}".format(pile[len(pile)-1]))
            print("Your cards: ")
            print(self.cards)
            print("The following cards are playable: ")
            print(playableCards)
            cardNumber = input("Select a card by typing its number. ")
            c = playableCards[cardNumber]
            game.effectActive = (c.value == "8")
            self.playCard(c, pile)

class Game:
    effectActive = False
    endOfGame = False
    def __init__(self):
        effectActive = False
        endOfGame = False


"""
let the 'Mau Mau Game' begin
"""
#nbrPlayers = input("Enter the number of players. ")
#check: is nbrPlayers a number in the right range?
#nbrHumans = input("How many humans are playing? ")
#TODO: increase the deck size according to player numbers

deck = Deck32()
pile = [deck.pop()]
players = [ComputerPlayer("Computer1", deck),
              ComputerPlayer("Computer2", deck),
              HumanPlayer("Jo", deck)
]
random.shuffle(players)

game = Game()
while not game.endOfGame:
    for p in players:
        #Must the player pause due to an 8?
        print("{}'s turn.".format(p.name))
        if game.effectActive and pile[len(pile)-1].value == "8":
            game.effectActive = False
            print('{} must pause.'.format(p.name)) 
            continue
        p.play(pile, deck, game)
        if len(p.cards) == 0:
            game.endOfGame = True
            print("{} won the game.".format(p.name))
            #print(pile[0])
            break
        
