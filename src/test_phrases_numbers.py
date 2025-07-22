import os
import unittest
from src.phrases import load_phrases_from_xlsx

class TestPhrasesNumbers(unittest.TestCase):
    def setUp(self):
        # Создаём тестовый xlsx-файл, имитирующий экспорт из Numbers
        from openpyxl import Workbook
        self.test_xlsx = 'src/test_phrases.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(['Фраза'])
        ws.append(['tortured phrase'])
        ws.append(['complex expression'])
        ws.append(['unusual wording'])
        wb.save(self.test_xlsx)

    def tearDown(self):
        os.remove(self.test_xlsx)

    def test_load_phrases(self):
        phrases = load_phrases_from_xlsx(self.test_xlsx)
        self.assertEqual(phrases, ['tortured phrase', 'complex expression', 'unusual wording'])

if __name__ == '__main__':
    unittest.main() 