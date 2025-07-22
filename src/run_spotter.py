import os
from phrases import load_phrases_and_recommendations_from_csv
from text_analyzer import load_text_from_file, find_phrases_in_text

# Пути к файлам
CSV_PATH = os.path.join(os.path.dirname(__file__), '..', '🤷_tortured.csv')
TEXT_PATH = os.path.join(os.path.dirname(__file__), '..', 'sample.txt')
HTML_REPORT_PATH = os.path.join(os.path.dirname(__file__), '..', 'report.html')
TXT_REPORT_PATH = os.path.join(os.path.dirname(__file__), '..', 'report.txt')

# ANSI-код для красного цвета
RED = '\033[91m'
RESET = '\033[0m'

HTML_STYLE = '<style>.highlight { color: red; font-weight: bold; }</style>'

# --- Выделение для консоли и HTML ---
def highlight_phrases(text, matches):
    matches_sorted = sorted(matches, key=lambda x: x['start'], reverse=True)
    for m in matches_sorted:
        text = (
            text[:m['start']] + RED + text[m['start']:m['end']] + RESET + text[m['end']:]
        )
    return text

def highlight_phrases_html(text, matches):
    matches_sorted = sorted(matches, key=lambda x: x['start'], reverse=True)
    for m in matches_sorted:
        text = (
            text[:m['start']] + '<span class="highlight">' + text[m['start']:m['end']] + '</span>' + text[m['end']:]
        )
    return text

# --- Сохранение TXT-отчёта ---
def save_txt_report(text, matches, recommendations, txt_path):
    lines = []
    lines.append('Text with Red-Highlighted Phrases:')
    # Для txt выделение делаем через ** **
    txt = text
    matches_sorted = sorted(matches, key=lambda x: x['start'], reverse=True)
    for m in matches_sorted:
        txt = txt[:m['start']] + '**' + txt[m['start']:m['end']] + '**' + txt[m['end']:]
    lines.append(txt)
    lines.append('\nDetected Phrases Report:')
    for m in matches:
        phrase = m['phrase']
        rec = recommendations.get(phrase, '(no recommendation)')
        frag = text[m['start']:m['end']]
        lines.append(f'- Detected Phrase: {frag} (position {m["start"]}-{m["end"]})')
        lines.append(f'  Recommendation: {rec}\n')
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'TXT report saved to {txt_path}')

# --- Сохранение HTML-отчёта ---
def save_html_report(text, matches, recommendations, html_path):
    html = ['<html><head><meta charset="utf-8">', HTML_STYLE, '</head><body>']
    html.append('<h2>Text with Red-Highlighted Phrases:</h2>')
    html.append('<pre>' + highlight_phrases_html(text, matches) + '</pre>')
    html.append('<h2>Detected Phrases Report:</h2>')
    html.append('<ul>')
    for m in matches:
        phrase = m['phrase']
        rec = recommendations.get(phrase, '(no recommendation)')
        frag = text[m['start']:m['end']]
        html.append(f'<li>Detected Phrase: <span class="highlight">{frag}</span> (position {m["start"]}-{m["end"]})<br>Recommendation: <b>{rec}</b></li>')
    html.append('</ul>')
    html.append('</body></html>')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html))
    print(f'HTML report saved to {html_path}')

# --- Основной сценарий ---
def main():
    print('Loading phrases and recommendations...')
    phrases, recommendations = load_phrases_and_recommendations_from_csv(CSV_PATH)
    print(f'Loaded {len(phrases)} phrases for search.')

    print('Loading text for analysis...')
    text = load_text_from_file(TEXT_PATH)
    print(f'Text length: {len(text)} characters.')

    print('Searching for phrases...')
    matches = find_phrases_in_text(text, phrases)
    print(f'Found {len(matches)} matches.')

    if not matches:
        print('No phrases from the list found in the text.')
        return

    # Выводим текст с подсветкой
    print('\nText with Red-Highlighted Phrases:')
    print(highlight_phrases(text, matches))

    # Формируем и выводим отчёт
    print('\nDetected Phrases Report:')
    for m in matches:
        phrase = m['phrase']
        rec = recommendations.get(phrase, '(no recommendation)')
        frag = text[m['start']:m['end']]
        print(f'- Detected Phrase: {RED}{frag}{RESET} (position {m["start"]}-{m["end"]})')
        print(f'  Recommendation: {rec}\n')

    # Сохраняем HTML-отчёт
    save_html_report(text, matches, recommendations, HTML_REPORT_PATH)
    # Сохраняем TXT-отчёт
    save_txt_report(text, matches, recommendations, TXT_REPORT_PATH)

if __name__ == '__main__':
    main() 