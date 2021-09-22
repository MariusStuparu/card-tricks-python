#!/usr/bin/python

from random import shuffle, randrange
from typing import Optional

from .constants import CARD_VALUES, CARD_COLOURS
from .Card import Card


class Deck:
    """
    Simple deck of cards class
    """
    __deck: list[Card] = []
    __cardInHand: Optional[Card] = None

    def __init__(self, shuffleAtStart: bool = False):
        try:
            for col in CARD_COLOURS:
                for val in CARD_VALUES:
                    newCard = Card(val, col)
                    self.__deck.append(newCard)

            if len(self.__deck) != 52:
                """I wish I could write 42 here..."""
                raise ValueError('Deck is not full!')
        except ValueError as vErr:
            print('Error generating the deck of cards:')
            print(vErr)
        else:
            if shuffleAtStart:
                self.shuffleDeck()

    def shuffleDeck(self):
        """
        Shuffle the deck
        """
        shuffle(self.__deck)

    def takeOneCard(self, fromWhere: str = 'top'):
        """
        Take one card from the deck. Don't show it.
        :param fromWhere: ['top', 'bottom', 'anywhere']
        """
        if len(self.__deck) >= 1:
            if fromWhere == 'top':
                index = -1
            elif fromWhere == 'bottom':
                index = 0
            else:
                index = randrange(1, len(self.__deck))

            self.__cardInHand = self.__deck.pop(index)
        else:
            print('There are no more cards in deck')

    def showCard(self):
        """
        Show the card in hand
        """
        if self.__cardInHand:
            print(f'You have: {self.__cardInHand.getCardFull()}')
        else:
            print('Your hands are empty, silly!')

    def putCardBack(self, where: str = 'anywhere'):
        """
        Put the card back in the deck
        :param where: ['top', 'bottom', 'anywhere']
        """
        if self.__cardInHand:
            if where == 'top':
                index = len(self.__deck)
            elif where == 'bottom':
                index = 0
            else:
                index = randrange(0, len(self.__deck)+1)

            self.__deck.insert(index, self.__cardInHand)
            self.__cardInHand = None
        else:
            print('Your hands are empty, silly!')


if __name__ == '__main__':
    print('This class is a module, it can\'t be called directly.')
