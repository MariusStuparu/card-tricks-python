#!/usr/bin/python

import unittest
from random import randint

from Card.Card import Card
from constants import CARD_VALUES, CARD_COLOURS


class CardTest(unittest.TestCase):
    def setUp(self):
        randValue = randint(0, len(CARD_VALUES) - 1)
        randColour = randint(0, len(CARD_COLOURS) - 1)
        self.value = list(CARD_VALUES)[randValue]
        self.colour = CARD_COLOURS[randColour]
        self.card = Card(self.value, self.colour)

    def test_init(self):
        self.assertIsInstance(self.card, Card)

    def test_get_value(self):
        self.assertEqual(self.card.getCardValue(), self.value)

    def test_get_colour(self):
        self.assertEqual(self.card.getCardColour(), self.colour)

    def test_get_full_card(self):
        assumeText = f'{self.value} of {self.colour}'
        self.assertEqual(self.card.getCardFull(), assumeText)

    def test_init_noargs(self):
        with self.assertRaises(TypeError) as context:
            card = Card()
            self.assertNotIsInstance(card, Card)
            errorText = str(context.exception)
            self.assertTrue(errorText.find('missing 2 required positional arguments'))

    def test_init_wrong_args(self):
        with self.assertRaises(TypeError):
            card1 = Card(0)
            self.assertNotIsInstance(card1, Card)
            card2 = Card(1, 'not')
            self.assertNotIsInstance(card2, Card)
            card3 = Card(20, 'heart')
            self.assertNotIsInstance(card3, Card)
            card4 = Card(None, 'diamond')
            self.assertNotIsInstance(card4, Card)


if __name__ == '__main__':
    unittest.main()
