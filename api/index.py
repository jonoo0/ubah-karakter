import streamlit as st
import io

char_map = {
    'a': '\u0430',
    'c': '\u0441',
    'e': '\u0435',
    'h': '\u04bb',
    'j': '\u0458',
    # 'n': '\u0578',
    'o': '\u043e',
    'p': '\u0440',
    'y': '\u0443'
}

def ubah_karakter(text):
    return ''.join(char_map.get(char, char) for char in text) 

st.title('Ubah Karakter')

input_text = st.text_area('Masukkan teks yang ingin diubah karakternya')
if st.button('Ubah karakter'):
    modified_text = ubah_karakter(input_text)

    modified_file = io.BytesIO(modified_text.encode('utf-8'))
    modified_file_name = 'hasil_modifikasi.txt'

    st.text_area('Hasil modifikasi', value=modified_text, height=200)

    st.download_button(label='Download hasil modifikasi', 
                       data=modified_file,
                       file_name=modified_file_name, 
                       mime='text/plain')