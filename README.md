# 🐱 Kicau Mania AI Overlay (Gesture Mode)

Proyek filter webcam interaktif berbasis AI yang lagi viral! Aplikasi ini memunculkan video "Kucing Joget" dan memutar musik **Kicau Mania** secara otomatis hanya dengan menggunakan gestur ayunan (swipe) tangan kamu.

## ✨ Fitur Utama
- **One-Shot Sync**: Video dan audio berjalan selaras secara otomatis sampai selesai.
- **AI Hand Tracking**: Deteksi telapak tangan yang presisi menggunakan MediaPipe.
- **Swipe Gesture**: Ayunkan tangan ke **Kiri** untuk memulai aksi!
- **Auto-Fix Black Screen**: Menghindari bug layar hitam pada Mac.

## 🚀 Cara Menjalankan dari Awal (Quick Start)

### Untuk Pengguna Mac (Paling Cepat):
1. **Download & Ekstrak** folder proyek ini.
2. Buka folder di **Finder**.
3. Klik kanan file **`Buka_Kicau_Mania.command`** dan pilih **Open**.
4. Tunggu terminal melakukan instalasi otomatis sampai kamera terbuka. Selesai!

> **Catatan:** Jika kamera tidak terbuka, berikan izin akses kamera untuk **Terminal** di *System Settings > Privacy & Security > Camera*.

### Untuk Pengguna Windows:
1. Buka **Command Prompt** atau **PowerShell** di folder proyek.
2. Buat Virtual Environment: `python -m venv venv`
3. Aktifkan venv: `venv\Scripts\activate`
4. Install library: `pip install -r requirements.txt`
5. Jalankan: `python main.py`

## ✋ Cara Menggunakan di Depan Kamera
1. Pastikan wajah dan tangan kamu terlihat di kamera.
2. **Ayunkan telapak tangan** kamu dari arah kanan ke kiri (seperti menyapu layar) secara lebar dan cepat.
3. Video kucing akan muncul di samping wajahmu dan musik akan berputar otomatis sampai durasi video habis.

## 📂 Struktur Proyek
- `assets/`: Tempat file video (`cat_dance.mp4`) dan musik (`kicau_mania.mp3`).
- `main.py`: Kode utama aplikasi.
- `Buka_Kicau_Mania.command`: Script otomatis sekali klik untuk Mac.
- `requirements.txt`: Daftar library yang dibutuhkan (OpenCV, MediaPipe, Pygame).

---
*Dibuat untuk tujuan edukasi dan hiburan. Selamat mencoba!*
