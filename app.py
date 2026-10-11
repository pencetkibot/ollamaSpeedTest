import requests
import json

# ================= KONFIGURASI =================
# Ganti dengan IP PC Server Ollama Anda dan model yang terinstal di sana
SERVER_IP = "127.0.0.1"  # <--- Ganti dengan IP lokal PC server Ollama
PORT = "11434"
NAMA_MODEL = "qwen2.5-coder:7b"       # <--- Ganti dengan model yang ingin diuji

PROMPT_UJI = "Jelaskan secara singkat apa itu kecerdasan buatan dalam 3 paragraf."
# ===============================================

url = f"http://{SERVER_IP}:{PORT}/api/generate"
payload = {
    "model": NAMA_MODEL,
    "prompt": PROMPT_UJI,
    "stream": False # Mengambil hasil akhir langsung beserta statistiknya
}

print(f"Mengirim permintaan ke {url} menggunakan model '{NAMA_MODEL}'...")

try:
    response = requests.post(url, json=payload, timeout=60)
    
    if response.status_code == 200:
        data = response.json()
        
        # Mengambil data metrik durasi (Ollama mengirimkannya dalam satuan nanosecond)
        # 1 detik = 1.000.000.000 nanosecond
        eval_count = data.get("eval_count", 0)  # Jumlah token output
        eval_duration_ns = data.get("eval_duration", 0) # Waktu pembuatan output
        
        prompt_eval_count = data.get("prompt_eval_count", 0) # Jumlah token input
        prompt_eval_duration_ns = data.get("prompt_eval_duration", 0) # Waktu pemrosesan input
        
        load_duration_ns = data.get("load_duration", 0) # Waktu memuat model ke RAM/VRAM

        # Konversi ke detik
        eval_duration_sec = eval_duration_ns / 1e9
        prompt_eval_duration_sec = prompt_eval_duration_ns / 1e9
        load_duration_sec = load_duration_ns / 1e9
        
        # Hitung Token per Second
        tokens_per_second = eval_count / eval_duration_sec if eval_duration_sec > 0 else 0
        prompt_tokens_per_second = prompt_eval_count / prompt_eval_duration_sec if prompt_eval_duration_sec > 0 else 0

        # Tampilkan Hasil Performa
        print("\n=== HASIL RESPONS ===")
        print(data.get("response", ""))
        
        print("\n=== METRIK PERFORMA OLLAMA ===")
        print(f"⏱️  Waktu Load Model       : {load_duration_sec:.2f} detik")
        print(f"📥 Input Prompt           : {prompt_eval_count} token ({prompt_tokens_per_second:.2f} t/s)")
        print(f"📤 Output Hasil           : {eval_count} token dalam {eval_duration_sec:.2f} detik")
        print(f"⚡ Kecepatan Generasi LLM : {tokens_per_second:.2f} tokens/second")
        print("==============================")
        
    else:
        print(f"❌ Gagal terhubung ke Ollama. Status Code: {response.status_code}")
        print(response.text)

except requests.exceptions.ConnectionError:
    print(f"❌ Koneksi gagal! Periksa apakah IP {SERVER_IP} sudah benar dan Ollama sudah berjalan.")
except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")