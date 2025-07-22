import os
import unittest

class TestDocumentation(unittest.TestCase):
    def test_readme_exists(self):
        self.assertTrue(os.path.exists('README.md'), 'README.md должен существовать')

    def test_readme_content(self):
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('Установка', content)
        self.assertIn('Запуск', content)
        self.assertIn('Структура проекта', content)
        self.assertIn('🤷_tortured.csv', content)
        self.assertIn('sample.txt', content)
        self.assertIn('report.html', content)
        self.assertIn('report.txt', content)
        self.assertIn('Редактирование списка фраз', content)

if __name__ == '__main__':
    unittest.main() 