#!/usr/bin/env python3
import unittest
from bidimensional import generate2d, generate2dOptimised, repeat_alphabet_chatgpt

class TestGenerate2d(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual(generate2d(0, 0), "")
        self.assertEqual(generate2dOptimised(0, 0), "")
        self.assertEqual(repeat_alphabet_chatgpt(0, 0), "")


    def test_single_row(self):
        self.assertEqual(generate2d(1, 5), "abcde")
        self.assertEqual(generate2dOptimised(1, 5), "abcde")
        self.assertEqual(repeat_alphabet_chatgpt(1, 5), "abcde")


    def test_single_column(self):
        self.assertEqual(generate2d(5, 1), "aaaaa")
        self.assertEqual(generate2dOptimised(5, 1), "aaaaa")
        self.assertEqual(repeat_alphabet_chatgpt(5, 1), "aaaaa")



    def test_multiple_rows_and_columns(self):
        self.assertEqual(generate2d(3, 5), "abcdeabcdeabcde")
        self.assertEqual(generate2dOptimised(3, 5), "abcdeabcdeabcde")
        self.assertEqual(repeat_alphabet_chatgpt(3, 5), "abcdeabcdeabcde")

    def test_overflow(self):
        expected = "abcdefghijklmnopqrstuvwxyzabcd"
        self.assertEqual(generate2d(1,30), expected)
        self.assertEqual(generate2dOptimised(1,30), expected)
        self.assertEqual(repeat_alphabet_chatgpt(1,30), expected)
        expected2 = expected + expected
        self.assertEqual(generate2d(2,30), expected2)
        self.assertEqual(generate2dOptimised(2,30), expected2)
        self.assertEqual(repeat_alphabet_chatgpt(2,30), expected2)





if __name__ == '__main__':
    unittest.main()
