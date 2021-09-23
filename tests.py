#!/usr/bin/python

import unittest

from test.test_card import CardTest
from test.test_deck import DeckTest

if __name__ == '__main__':
    testmodules = [
        'test.test_card',
        'test.test_deck'
    ]

    suite = unittest.TestSuite()

    for t in testmodules:
        try:
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner().run(suite)
