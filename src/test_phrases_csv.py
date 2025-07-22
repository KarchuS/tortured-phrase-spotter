import os
import unittest
from phrases import load_phrases_and_recommendations_from_csv

class TestPhrasesCSV(unittest.TestCase):
    def setUp(self):
        self.test_csv = 'src/test_phrases.csv'
        with open(self.test_csv, 'w', encoding='utf-8') as f:
            f.write('"Tortured Phrase","Recommendation"\n')
            f.write('"tortured phrase","simple phrase"\n')
            f.write('"complex expression","simple expression"\n')
            f.write('"unusual wording","common wording"\n')

    def tearDown(self):
        os.remove(self.test_csv)

    def test_load_phrases_and_recommendations(self):
        phrases, recommendations = load_phrases_and_recommendations_from_csv(self.test_csv)
        self.assertEqual(phrases, ['tortured phrase', 'complex expression', 'unusual wording'])
        self.assertEqual(recommendations, {
            'tortured phrase': 'simple phrase',
            'complex expression': 'simple expression',
            'unusual wording': 'common wording'
        })

if __name__ == '__main__':
    unittest.main() 