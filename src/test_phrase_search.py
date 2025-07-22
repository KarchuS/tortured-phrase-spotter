import unittest
from text_analyzer import find_phrases_in_text

class TestPhraseSearch(unittest.TestCase):
    def setUp(self):
        self.text = "This is a tortured phrase. Another tortured phrase! And a complex expression."
        self.phrases = ["tortured phrase", "complex expression"]

    def test_find_phrases(self):
        matches = find_phrases_in_text(self.text, self.phrases)
        expected = [
            {'phrase': 'tortured phrase', 'start': 10, 'end': 25},
            {'phrase': 'tortured phrase', 'start': 35, 'end': 50},
            {'phrase': 'complex expression', 'start': 58, 'end': 76}
        ]
        self.assertEqual(matches, expected)

    def test_case_insensitive(self):
        text = "Tortured Phrase and tortured phrase."
        matches = find_phrases_in_text(text, ["tortured phrase"])
        expected = [
            {'phrase': 'tortured phrase', 'start': 0, 'end': 15},
            {'phrase': 'tortured phrase', 'start': 20, 'end': 35}
        ]
        self.assertEqual(matches, expected)

    def test_overlap(self):
        text = "tortured phrase phrase"
        matches = find_phrases_in_text(text, ["phrase phrase", "phrase"])
        expected = [
            {'phrase': 'phrase phrase', 'start': 9, 'end': 22},
            {'phrase': 'phrase', 'start': 9, 'end': 15},
            {'phrase': 'phrase', 'start': 16, 'end': 22}
        ]
        self.assertEqual(matches, expected)

if __name__ == '__main__':
    unittest.main() 