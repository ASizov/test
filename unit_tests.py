import unittest
from main3 import max_substring_with_k_unique

class TestCases(unittest.TestCase):

    def test_case_begin(self):
        self.assertEqual(max_substring_with_k_unique('aadaddabbaba'), 'aadadda')
    
    def test_case_end(self):
        self.assertEqual(max_substring_with_k_unique('aadabbaba'), 'abbaba')
        
    def test_case_mid(self):
        self.assertEqual(max_substring_with_k_unique('aadabddadaaadbbaba'), 'ddadaaad')
        
    def test_short_str(self):
        self.assertEqual(max_substring_with_k_unique('a'), 'a')
        
    def test_empty_str(self):
        self.assertEqual(max_substring_with_k_unique(''), '')
        
    def test_unique_char_less_k(self):
        self.assertEqual(max_substring_with_k_unique('aaaaaaaaaaa'), 'aaaaaaaaaaa')
        
    def test_input_not_str(self):
        self.assertEqual(max_substring_with_k_unique(777), 'string expected')

if __name__ == '__main__':
    unittest.main()