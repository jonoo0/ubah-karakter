from flask import Flask, request, render_template, send_file
import io

app = Flask(__name__)

tabel_konversi = {
    'a': '\u0430',
    'c': '\u0441',
    'e': '\u0435',
    'h': '\u04bb',
    'j': '\u0458',
    'o': '\u043e',
    'p': '\u0440',
    'y': '\u0443'
}

def ubah_karakter(teks):
    return ''.join(tabel_konversi.get(huruf, huruf) for huruf in teks)

@app.route('/', methods=['GET', 'POST'])
def index():
    teks_diubah = None
    if request.method == 'POST':
        teks_masuk = request.form['input_text']
        teks_diubah = ubah_karakter(teks=teks_masuk)

        #simpan teks ke file txt
        file_teks_diubah = io.BytesIO(teks_diubah.encode('utf-8'))
        file_teks_diubah.seek(0)
        return render_template('index.html', teks_diubah=teks_diubah, as_attachment=True)
    
    return render_template('index.html', teks_diubah=teks_diubah, as_attachment=False)

@app.route('/download')
def download():
    teks_diubah = request.args.get('teks_diubah', '')
    file_teks_diubah = io.BytesIO(teks_diubah.encode('utf-8'))
    file_teks_diubah.seek(0)
    return send_file(file_teks_diubah, as_attachment=True, download_name='teks_diubah.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)