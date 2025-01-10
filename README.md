## Cara Menggunakan


### Prasyarat
1. Python 3.10 atau versi lebih tinggi.
2. Instalasi pustaka:
   ```bash
   pip install -r requirements.txt
   ```
3. File `.env` yang memuat API key untuk Google Generative AI.

### Langkah-langkah
1. **Inisialisasi Model**:
   Jalankan sel yang memuat `load_dotenv` untuk memastikan API key tersedia.
2. **Membaca Dokumen**:
   Masukkan path dokumen PDF yang ingin Anda gunakan untuk eksperimen.
3. **Membuat Embedding**:
   Eksekusi sel yang membuat embedding dan menyimpannya untuk retriever.
4. **Menjalankan Chain**:
   Ajukan pertanyaan melalui chain untuk mendapatkan jawaban berbasis dokumen.
