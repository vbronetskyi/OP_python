"""
The machine test module
"""

import unittest

from machine import TextMachine, VendingMachine


class TestTextMachine(unittest.TestCase):
    """
    The tests for the TextMachine class
    """

    def test_base_functionality(self):
        """
        Test the init for the class
        """
        print("Testing TextMachine class...", end="")
        # Text machines have four main properties:
        # how many text of two type they contain and the price of each type text.
        # A new text machine starts with two texts type.
        tm1 = TextMachine((75, 125), (25, 245))
        self.assertEqual(
            str(tm1),
            "Text Machine:<75 texts; ₴1.25 each>; <25 texts; ₴2.45 each>",
        )
        # When the user inserts money and text type, the machine returns
        # a message about their status and any change they need as a tuple.
        self.assertFalse(tm1.is_empty())
        self.assertEqual(tm1.texts_count(), (75, 25))
        self.assertEqual(tm1.still_owe(), (125, 245))
        self.assertEqual(
            tm1.insert_money((20, "short")), ("Still owe ₴1.05", 20)
        )
        self.assertEqual(tm1.still_owe(), (105, 245))
        self.assertEqual(tm1.texts_count(), (75, 25))
        self.assertEqual(
            tm1.insert_money((5, "short")), ("Still owe ₴1.00", 25)
        )

        # When the user has paid enough money, they get a text and
        # the money owed resets.
        self.assertEqual(tm1.insert_money((100, "short")), ("Got a text!", 125))
        self.assertEqual(tm1.texts_count(), (74, 25))
        self.assertEqual(tm1.still_owe(), (125, 245))
        self.assertEqual(
            str(tm1),
            "Text Machine:<74 texts; ₴1.25 each>; <25 texts; ₴2.45 each>",
        )
        # If the user pays too much money, they get their change back
        # with the text.

        self.assertEqual(
            tm1.insert_money((500, "long")),
            ("Got a text!", 255, "You can buy 1 long text or 2 short text"),
        )
        self.assertEqual(tm1.texts_count(), (74, 24))
        self.assertEqual(tm1.still_owe(), (125, 245))
        self.assertEqual(
            str(tm1),
            "Text Machine:<74 texts; ₴1.25 each>; <24 texts; ₴2.45 each>",
        )

    def test_methods(self):
        """
        Test the additional methods for the machine
        """
        tm2 = TextMachine((1, 120), (0, 245))
        self.assertEqual(str(tm2), "Text Machine:<1 texts; ₴1.20 each>")
        self.assertFalse(tm2.is_empty())
        self.assertEqual(tm2.insert_money((120, "short")), ("Got a text!", 120))
        self.assertEqual(tm2.texts_count(), (0, 0))
        self.assertTrue(tm2.is_empty())
        self.assertEqual(str(tm2), "Text Machine:<0 texts; ₴1.20 each>")

        # Once a machine is empty,
        # it should not accept money until it is restocked.
        self.assertEqual(
            tm2.insert_money((25, "short")), ("Machine is empty", 25)
        )
        self.assertEqual(
            tm2.insert_money((120, "short")), ("Machine is empty", 120)
        )
        self.assertEqual(tm2.still_owe(), (120, 245))
        self.assertIsNone(
            tm2.stock_machine((20, 20))
        )  # Does not return anything
        self.assertEqual(tm2.texts_count(), (20, 20))
        self.assertTrue(tm2.is_empty())
        self.assertEqual(
            str(tm2),
            "Text Machine:<20 texts; ₴1.20 each>; <20 texts; ₴2.45 each>",
        )
        self.assertEqual(
            tm2.insert_money((25, "short")), ("Still owe ₴0.95", 25)
        )
        self.assertEqual(tm2.still_owe(), (95, 245))
        # Imma let this one just be here, dunno what it does
        tm2.stock_machine((20, 0))
        self.assertEqual(tm2.texts_count(), (40, 20))

    def test_dunders(self):
        """
        Test the hidden methods for class
        """
        tm3 = TextMachine((25, 100), (25, 200))
        tm4 = TextMachine((25, 100), (25, 200))
        tm5 = TextMachine((20, 100), (15, 200))
        tm6 = TextMachine((25, 120), (25, 245))
        tm7 = "Text Machine"
