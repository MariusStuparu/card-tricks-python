#!/usr/bin/python

from random import shuffle, randrange

from constants import CARD_VALUES, CARD_COLOURS
from Card.Card import Card


class Deck:
    """
    Simple deck of cards class
    """

    def __init__(self, shuffleAtStart: bool = False):
        self.__deck: list[Card] = []

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

    def countDeck(self) -> int:
        """
        Count how many cards are in the deck
        :return: int
        """
        return len(self.__deck)

    def shuffleDeck(self):
        """
        Shuffle the deck
        """
        shuffle(self.__deck)

    def takeOneCard(self, fromWhere: str = 'top') -> Card:
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

            return self.__deck.pop(index)
        else:
            print('There are no more cards in deck')

    def putCardBack(self, cardInHand: Card, where: str = 'anywhere'):
        """
        Put the card back in the deck
        :param cardInHand
        :param where: ['top', 'bottom', 'anywhere']
        """
        if cardInHand:
            if where == 'top':
                index = len(self.__deck)
            elif where == 'bottom':
                index = 0
            else:
                index = randrange(0, len(self.__deck)+1)

            try:
                if not self.__deck.count(cardInHand):
                    self.__deck.insert(index, cardInHand)
                else:
                    raise IndexError('That card is already in the deck.')
            except IndexError as iErr:
                print(iErr)
        else:
            print('Your hands are empty, silly!')


if __name__ == '__main__':
    print('This class is a module, it can\'t be called directly.')
