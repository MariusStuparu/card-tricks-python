#!/usr/bin/python

from random import randint
from time import sleep
import sys

from Deck.Deck import Deck


def main():
    if sys.version_info[0] == 3 and sys.version_info[1] >= 1:
        print('The magician')

        """Set up"""
        deckPositions = ['top', 'bottom', 'anywhere']

        deck = Deck()

        """Run"""
        while input('Do you want me to show you a card trick? (y/n) ') == 'y':
            print('Shuffle the deck')
            deck.shuffleDeck()
            print()
            sleep(2)

            randomPos1 = deckPositions[randint(0, 2)]
            print(f'Take one card from {randomPos1}')
            card1 = deck.takeOneCard(fromWhere=randomPos1)
            print()
            sleep(2)

            randomPos2 = deckPositions[randint(0, 2)]
            print(f'Put it back {randomPos2}')
            deck.putCardBack(card1, randomPos2)
            print()
            sleep(2)

            print('Shuffle the deck again')
            deck.shuffleDeck()
            print()
            sleep(2)

            randomPos3 = deckPositions[randint(0, 2)]
            print(f'Take one card from {randomPos3}')
            card2 = deck.takeOneCard(fromWhere=randomPos3)
            print()
            sleep(2)

            print('Is it the same card as before?')
            print(f'First card: {card1.getCardFull()}')
            print(f'Second card: {card2.getCardFull()}')
            print()
            if card1.getCardFull() == card2.getCardFull():
                print('Am I good or what?')
            else:
                print('Look at this note I have written yesterday.')

            deck.putCardBack(card2, randomPos2)
            print()
    else:
        print('Wrong Python version')


if __name__ == '__main__':
    main()
