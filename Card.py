#!/usr/bin/python

from .constants import CARD_VALUES, CARD_COLOURS


class Card:
    """
    Simple class for standard playing cards
    For simplicity, cards have only numeric values, from 1 to 13
    """
    __value = None
    __colour = None

    def __init__(self, value: int, colour: str):
        try:
            if value in CARD_VALUES:
                self.__value = value
            else:
                raise ValueError(f'Error initializing card: value {value} is invalid. Accepted range is 1..13')

            if colour in CARD_COLOURS:
                self.__colour = colour
            else:
                raise ValueError(f'Error initializing card: value {value} is invalid. Accepted colours are {", ".join(CARD_COLOURS)}')
        except ValueError as vErr:
            print(vErr)
            raise

    def getCardValue(self) -> int:
        """
        Get only the value of the card
        :return: integer
        """
        return self.__value

    def getCardColour(self) -> str:
        """
        Get only the colour of the card, as string
        :return: string
        """
        return self.__colour

    def getCardFull(self) -> str:
        """
        Get the full card information as string
        :return: string
        """
        return f'{self.__value} of {self.__colour}'


if __name__ == '__main__':
    print('This class is a module, it can\'t be called directly.')
