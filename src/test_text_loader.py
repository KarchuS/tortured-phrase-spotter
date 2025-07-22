import os
import unittest
from text_analyzer import load_text_from_file

class TestTextLoader(unittest.TestCase):
    def setUp(self):
        self.test_txt = 'src/test_text.txt'
        with open(self.test_txt, 'w', encoding='utf-8') as f:
            f.write('This is a test.\nSecond line.')

    def tearDown(self):
        os.remove(self.test_txt)

    def test_load_text(self):
        text = load_text_from_file(self.test_txt)
        self.assertEqual(text, 'This is a test.\nSecond line.')

if __name__ == '__main__':
    unittest.main() 