import os
import unittest

class TestProjectStructure(unittest.TestCase):
    def test_main_modules_exist(self):
        # Проверяем, что основной модуль для работы с фразами существует
        self.assertTrue(os.path.exists('src/phrases.py'), 'phrases.py должен существовать')
        # Проверяем, что основной модуль для анализа текста существует
        self.assertTrue(os.path.exists('src/text_analyzer.py'), 'text_analyzer.py должен существовать')

    def test_phrases_storage_exists(self):
        # Проверяем, что файл для хранения фраз существует (или будет создан)
        self.assertTrue(os.path.exists('src/phrases.txt') or os.path.exists('src/phrases.json'),
                        'Должен существовать файл phrases.txt или phrases.json для хранения фраз')

if __name__ == '__main__':
    unittest.main() 