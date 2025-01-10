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

Berikut adalah langkah-langkah untuk mengambil API Google Gemini dan penggunaannya dengan file `.env`:

---

## Langkah Mengambil API Google Gemini dan Penggunaan `.env`

### 1. **Mendaftar dan Mengakses API Google Gemini**
   1. **Daftar ke Google Cloud**:
      - Masuk ke [Google Cloud Console](https://console.cloud.google.com/).
      - Jika belum memiliki akun, daftarkan akun baru menggunakan email Anda.

   2. **Aktifkan API Google Generative AI**:
      - Navigasikan ke menu **API & Services** > **Library**.
      - Cari **Generative AI API** dan klik **Enable**.

   3. **Buat Proyek Baru** (Jika belum ada):
      - Di Google Cloud Console, klik **Select Project** > **New Project**.
      - Beri nama proyek Anda dan klik **Create**.

   4. **Buat Credential API Key**:
      - Pergi ke **API & Services** > **Credentials**.
      - Klik **Create Credentials** > **API Key**.
      - Salin **API Key** yang telah dibuat.

---

### 2. **Menggunakan File `.env` untuk Menyimpan API Key**
   File `.env` digunakan untuk menyimpan variabel sensitif seperti API Key agar tidak ditulis langsung di dalam kode.

   #### a. Buat File `.env`
   - Di direktori proyek Anda, buat file bernama `.env`.

   #### b. Tambahkan API Key ke `.env`
   - Tambahkan baris berikut di file `.env`:
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```
     Gantilah `your_api_key_here` dengan API Key yang Anda salin dari Google Cloud.

### 5. **Keamanan API Key**
   - Jangan pernah membagikan file `.env` atau API Key di repositori publik.
   - Tambahkan `.env` ke file `.gitignore` untuk mencegahnya ter-upload ke Git:
     ```plaintext
     .env
     ```
