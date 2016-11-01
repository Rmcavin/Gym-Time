#a test for the common_elements.py

import unittest
from common_elements import Common_Elements

class TestCommonElement(unittest.TestCase):

    def setUp(self):
        self.ce = Common_Elements()

    def test_commonElement_simple(self):
        self.array1 = [1,2]
        self.array2 = [1]
        self.answer = self.ce.find_common_elements(self.array1, self.array2)
        self.assertEqual(self.answer, [1])

    def test_commonElements_simple2(self):
        self.array1 = [3,4]
        self.array2 = [4]
        self.answer = self.ce.find_common_elements(self.array1, self.array2)
        self.assertEqual(self.answer, [4])

    def test_commonElements_none(self):
        self.array1 = [3,4]
        self.array2 = [5]
        self.answer = self.ce.find_common_elements(self.array1, self.array2)
        self.assertEqual(self.answer, [])

    def test_commonElements_unordered(self):
        self.array1 = [3,4]
        self.array2 = [4,3]
        self.answer = self.ce.find_common_elements(self.array1, self.array2)
        self.assertEqual(self.answer, [3, 4])

    def test_commonElements_strings(self):
        self.array1 = ['a','b']
        self.array2 = ['b']
        self.answer = self.ce.find_common_elements(self.array1, self.array2)
        self.assertEqual(self.answer, ['b'])

    def test_commonElements_mixed(self):
        self.array1 = ['b',1,2]
        self.array2 = [1,'b']
        self.answer = self.ce.find_common_elements(self.array1, self.array2)
        self.assertEqual(self.answer, [1,'b'])

if __name__ == '__main__':
    unittest.main()
