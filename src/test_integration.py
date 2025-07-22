import os
import unittest
from phrases import load_phrases_and_recommendations_from_csv
from text_analyzer import load_text_from_file, find_phrases_in_text
from run_spotter import save_html_report, save_txt_report

class TestIntegrationFullCycle(unittest.TestCase):
    def setUp(self):
        # Создаём тестовый csv-файл с фразами и рекомендациями
        self.csv_path = 'src/test_phrases.csv'
        with open(self.csv_path, 'w', encoding='utf-8') as f:
            f.write('"Tortured Phrase","Recommendation"\n')
            f.write('"tortured phrase","simple phrase"\n')
            f.write('"complex expression","simple expression"\n')
        # Создаём тестовый текстовый файл
        self.text_path = 'src/test_text.txt'
        with open(self.text_path, 'w', encoding='utf-8') as f:
            f.write('This is a tortured phrase. Here is a complex expression.')
        self.html_path = 'src/test_report.html'
        self.txt_path = 'src/test_report.txt'

    def tearDown(self):
        for path in [self.csv_path, self.text_path, self.html_path, self.txt_path]:
            if os.path.exists(path):
                os.remove(path)

    def test_full_cycle(self):
        # Загрузка фраз и рекомендаций
        phrases, recommendations = load_phrases_and_recommendations_from_csv(self.csv_path)
        self.assertEqual(phrases, ['tortured phrase', 'complex expression'])
        self.assertEqual(recommendations['tortured phrase'], 'simple phrase')
        self.assertEqual(recommendations['complex expression'], 'simple expression')
        # Загрузка текста
        text = load_text_from_file(self.text_path)
        self.assertIn('tortured phrase', text)
        # Поиск
        matches = find_phrases_in_text(text, phrases)
        self.assertEqual(len(matches), 2)
        # Генерация отчётов
        save_html_report(text, matches, recommendations, self.html_path)
        save_txt_report(text, matches, recommendations, self.txt_path)
        # Проверка содержимого отчётов
        with open(self.html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('<span class="highlight">tortured phrase</span>', html)
        self.assertIn('<span class="highlight">complex expression</span>', html)
        self.assertIn('Recommendation: <b>simple phrase</b>', html)
        self.assertIn('Recommendation: <b>simple expression</b>', html)
        with open(self.txt_path, 'r', encoding='utf-8') as f:
            txt = f.read()
        self.assertIn('**tortured phrase**', txt)
        self.assertIn('**complex expression**', txt)
        self.assertIn('Recommendation: simple phrase', txt)
        self.assertIn('Recommendation: simple expression', txt)

if __name__ == '__main__':
    unittest.main() 