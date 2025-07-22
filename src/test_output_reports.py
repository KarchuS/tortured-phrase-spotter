import os
import unittest
from run_spotter import save_html_report, save_txt_report

class TestOutputReports(unittest.TestCase):
    def setUp(self):
        self.text = "This is a tortured phrase. And another tortured phrase!"
        self.matches = [
            {'phrase': 'tortured phrase', 'start': 10, 'end': 25},
            {'phrase': 'tortured phrase', 'start': 39, 'end': 54}
        ]
        self.recommendations = {'tortured phrase': 'simple phrase'}
        self.html_path = 'src/test_report.html'
        self.txt_path = 'src/test_report.txt'

    def tearDown(self):
        if os.path.exists(self.html_path):
            os.remove(self.html_path)
        if os.path.exists(self.txt_path):
            os.remove(self.txt_path)

    def test_html_report(self):
        save_html_report(self.text, self.matches, self.recommendations, self.html_path)
        self.assertTrue(os.path.exists(self.html_path))
        with open(self.html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('Text with Red-Highlighted Phrases:', html)
        self.assertIn('<span class="highlight">tortured phrase</span>', html)
        self.assertIn('Detected Phrases Report:', html)
        self.assertIn('Recommendation: <b>simple phrase</b>', html)

    def test_txt_report(self):
        save_txt_report(self.text, self.matches, self.recommendations, self.txt_path)
        self.assertTrue(os.path.exists(self.txt_path))
        with open(self.txt_path, 'r', encoding='utf-8') as f:
            txt = f.read()
        self.assertIn('Text with Red-Highlighted Phrases:', txt)
        self.assertIn('**tortured phrase**', txt)
        self.assertIn('Detected Phrases Report:', txt)
        self.assertIn('Recommendation: simple phrase', txt)

if __name__ == '__main__':
    unittest.main() 