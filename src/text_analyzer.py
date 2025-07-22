# Модуль для анализа текста

def load_text_from_file(filepath):
    """
    Загружает текст из txt-файла с указанным путем.
    Возвращает содержимое файла как строку.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def find_phrases_in_text(text, phrases):
    """
    Ищет все вхождения заданных фраз в тексте (без учёта регистра, с учётом пересечений).
    Возвращает список словарей: {'phrase': str, 'start': int, 'end': int} (позиции по оригинальному тексту)
    """
    import re
    matches = []
    for phrase in phrases:
        pattern = re.escape(phrase)
        for m in re.finditer(pattern, text, re.IGNORECASE):
            matches.append({
                'phrase': phrase,
                'start': m.start(),
                'end': m.end()
            })
    matches.sort(key=lambda x: x['start'])
    return matches 