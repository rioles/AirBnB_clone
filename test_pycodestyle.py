#!/usr/bin/python3
from pycodestyle import checkCodeStyle
import unittest


class TestCode(unittest.TestCase):
    def testPycodestyle(self):
        "Test the pycodestyle file"
        expected = "Hello guys, i am free from errors"
        received = checkCodeStyle()
        self.assertEqual(expected, received)


if __name__ == '__main__':
    unittest.main()
