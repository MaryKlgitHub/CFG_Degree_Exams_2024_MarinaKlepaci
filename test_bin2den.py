import unittest
from alt_exam_python import bin2den, Bin2DenException

class TestBin2Den(unittest.TestCase):

    def test_bin(self):
        # Test valid binary string
        s = "10101"
        self.assertEqual(bin2den(s), 21)

    def test_numbers(self):
        # Test binary string with non-binary characters
        s = '101012'
        self.assertRaises(Bin2DenException, bin2den, s)

    def test_letters(self):
        # Test binary string with non-binary characters
        s = '10101a'
        self.assertRaises(Bin2DenException, bin2den, s)

    def test_empty_string(self):
        # Test empty string input
        s = ''
        self.assertRaises(Bin2DenException, bin2den, s)

if __name__== '__main__':
    unittest.main()
