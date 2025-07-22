from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import os
from phrases import load_phrases_and_recommendations_from_csv
from text_analyzer import find_phrases_in_text

app = Flask(__name__)
app.secret_key = 'tortured-phrase-spotter'

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..')
CSV_PATH = os.path.join(UPLOAD_FOLDER, '🤷_tortured.csv')
HTML_REPORT_PATH = os.path.join(UPLOAD_FOLDER, 'report.html')
TXT_REPORT_PATH = os.path.join(UPLOAD_FOLDER, 'report.txt')

# --- Подсветка фраз в HTML ---
def highlight_phrases_html(text, matches):
    matches_sorted = sorted(matches, key=lambda x: x['start'], reverse=True)
    for m in matches_sorted:
        text = (
            text[:m['start']] + '<span class="highlight">' + text[m['start']:m['end']] + '</span>' + text[m['end']:]
        )
    return text

def extract_text_from_pdf(file_stream):
    from PyPDF2 import PdfReader
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    phrases, recommendations = load_phrases_and_recommendations_from_csv(CSV_PATH)
    text = ''
    matches = []
    detected = []
    highlighted = ''
    if request.method == 'POST':
        if 'textfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['textfile']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = file.filename.lower()
        if filename.endswith('.pdf'):
            try:
                text = extract_text_from_pdf(file)
            except Exception as e:
                flash(f'PDF extraction error: {e}')
                return redirect(request.url)
        else:
            text = file.read().decode('utf-8')
        matches = find_phrases_in_text(text, phrases)
        highlighted = highlight_phrases_html(text, matches)
        # Считаем количество для каждой фразы
        phrase_counts = {}
        for m in matches:
            phrase_counts[m['phrase']] = phrase_counts.get(m['phrase'], 0) + 1
        detected = [
            {
                'phrase': p,
                'count': phrase_counts[p],
                'replace': recommendations.get(p, '(no recommendation)')
            }
            for p in phrase_counts
        ]
        # Сохраняем отчёты
        save_html_report(text, matches, recommendations, HTML_REPORT_PATH)
        save_txt_report(text, matches, recommendations, TXT_REPORT_PATH)
    return render_template('index.html', text=text, highlighted=highlighted, detected=detected)

@app.route('/download/<report_type>')
def download_report(report_type):
    if report_type == 'html':
        return send_file(HTML_REPORT_PATH, as_attachment=True)
    elif report_type == 'txt':
        return send_file(TXT_REPORT_PATH, as_attachment=True)
    else:
        return 'Unknown report type', 404

# --- Сохранение отчётов (используем существующую логику) ---
def save_html_report(text, matches, recommendations, html_path):
    html = ['<html><head><meta charset="utf-8">', '<style>.highlight { color: red; font-weight: bold; }</style>', '</head><body>']
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

def save_txt_report(text, matches, recommendations, txt_path):
    lines = []
    lines.append('Text with Red-Highlighted Phrases:')
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

if __name__ == '__main__':
    app.run(debug=True) 