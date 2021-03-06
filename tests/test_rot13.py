import unittest

from CrypticCreations.ciphers import *


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = Rot13Cipher(text="This is testing spaces!?").encipher()
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = Rot13Cipher(text="This is testing special characters!?.").encipher()
        self.assertIn('!?.', test)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = Rot13Cipher(text="Test.").encipher()
        self.assertEqual(test, 'Grfg.')

    def test_decipher_expected_output(self):
        """
        Confirms plaintext string exists in the bruteforce return list.
        """
        test = Rot13Cipher(text="Uryyb.").decipher()
        self.assertIn(test, "Hello.")


if __name__ == '__main__':
    unittest.main()
