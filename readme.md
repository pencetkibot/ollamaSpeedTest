# Proyek Ollama LLM Tester

## Overview

Proyek ini adalah aplikasi sederhana yang digunakan untuk menguji model bahasa besar (LLM) Ollama. Aplikasi ini mengirim permintaan ke server Ollama dengan prompt tertentu dan menampilkan hasil respons beserta metrik performa.

## Penginstalan

Untuk menginstal proyek ini, ikuti langkah-langkah berikut:

1. Klone repositori ini ke komputer lokal Anda:

   ```bash
   git clone https://github.com/pencetkibot/ollamaSpeedTest
   ```

2. Instal dependensi Python:
   ```bash
   pip install -r requirements.txt
   ```

## Penggunaan

Untuk menjalankan aplikasi, jalankan perintah berikut:

```bash
python app.py
```

Aplikasi akan mengirim permintaan ke server Ollama dengan prompt yang telah ditentukan dan menampilkan hasil respons beserta metrik performa.

## Konfigurasi

Anda dapat mengubah beberapa parameter dalam file `app.py` untuk menyesuaikan pengujian:

- `SERVER_IP`: Alamat IP server Ollama.
- `PORT`: Port yang digunakan oleh server Ollama.
- `NAMA_MODEL`: Nama model LLM yang akan digunakan.
- `PROMPT_UJI`: Prompt yang akan dikirim ke server Ollama untuk menghasilkan respons.

## Kontribusi

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
