from flask import Flask, request, render_template, send_file
import io

app = Flask(__name__)

char_map = {
    'a': '\u0430',
    'c': '\u0441',
    'e': '\u0435',
    'h': '\u04bb',
    'j': '\u0458',
    'o': '\u043e',
    'p': '\u0440',
    'y': '\u0443'
}

def ubah_karakter(kalimat):
    return ''.join(char_map.get(c, c) for c in kalimat)

@app.route('/', methods=['GET', 'POST'])
def index():
    kalimat_diubah = None
    if request.method == 'POST':
        input_kalimat = request.form['input_kalimat']
        kalimat_diubah = ubah_karakter(input_kalimat)
        kalimat_diubah = io.BytesIO(kalimat_diubah.encode('utf-8'))
        return send_file(kalimat_diubah, 
                         as_attachment=True, 
                         download_name='kalimat_diubah.txt', 
                         mimetype='text/plain')
    
    return render_template('index.html', kalimat_diubah=kalimat_diubah)