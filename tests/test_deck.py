import unittest

from Deck.Deck import Deck
from constants import CARD_VALUES, CARD_COLOURS


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def tearDown(self):
        self.deck = None

    def test_init(self):
        self.assertIsInstance(self.deck, Deck)

    def test_take_card_from_top(self):
        card = self.deck.takeOneCard(fromWhere='top')
        self.assertEqual(card.getCardValue(), 13)
        self.assertEqual(card.getCardColour(), 'club')
        self.deck.putCardBack(card, 'top')

    def test_take_card_from_bottom(self):
        card = self.deck.takeOneCard(fromWhere='bottom')
        self.assertEqual(card.getCardValue(), 1)
        self.assertEqual(card.getCardColour(), 'heart')

    def test_init_shuffle(self):
        deck2 = Deck(shuffleAtStart=True)
        card1 = deck2.takeOneCard(fromWhere='top')
        card2 = deck2.takeOneCard(fromWhere='top')
        valueTest = card1.getCardValue() != card2.getCardValue()
        colourTest = card1.getCardColour() != card2.getCardColour()
        self.assertTrue(valueTest or colourTest)

    def test_get_one_cardd(self):
        card = self.deck.takeOneCard(fromWhere='anywhere')
        self.assertTrue(card.getCardValue() in list(CARD_VALUES))
        self.assertTrue(card.getCardColour() in list(CARD_COLOURS))

    def test_count_deck(self):
        self.assertEqual(self.deck.countDeck(), 52)
        self.deck.takeOneCard(fromWhere='anywhere')
        self.assertEqual(self.deck.countDeck(), 51)

    def test_put_card_back(self):
        self.assertEqual(self.deck.countDeck(), 52)
        card = self.deck.takeOneCard(fromWhere='anywhere')
        self.assertEqual(self.deck.countDeck(), 51)
        self.deck.putCardBack(card)
        self.assertEqual(self.deck.countDeck(), 52)


if __name__ == '__main__':
    unittest.main()
