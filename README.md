# Kicau Mania AI Overlay (Gesture Controlled)

Proyek ini adalah implementasi filter webcam interaktif menggunakan kecerdasan buatan (AI) untuk mendeteksi gestur tangan. Aplikasi akan memunculkan video overlay dan memutar audio secara otomatis saat pengguna melakukan gestur ayunan tangan.

## Deskripsi Teknis
Aplikasi ini menggunakan MediaPipe Tasks API untuk melakukan pelacakan telapak tangan (Hand Tracking) secara real-time. Logika program telah dioptimalkan untuk menyinkronkan framerate video dengan durasi audio asli untuk memastikan pemutaran yang mulus dan presisi.

## Persyaratan Sistem
Untuk memastikan kompatibilitas pustaka MediaPipe dan OpenCV, disarankan menggunakan versi Python berikut:
- **Python 3.11** (Sangat Disarankan)
- **Python 3.12**
- **Penting:** Saat ini Python 3.14 belum didukung secara penuh oleh MediaPipe dan akan menyebabkan error pada modul pengenalan tangan.

## Instalasi dan Penggunaan

### Cara Cepat (Khusus macOS)
1. Buka direktori proyek ini melalui Finder.
2. Jalankan file `Buka_Kicau_Mania.command` dengan klik kanan dan pilih Open.
3. Script akan melakukan konfigurasi virtual environment, mengunduh library yang diperlukan, dan mengunduh model AI MediaPipe secara otomatis.

Catatan: Berikan izin akses kamera pada aplikasi Terminal melalui System Settings > Privacy & Security > Camera jika aplikasi gagal mengakses webcam.

### Instalasi Manual (Windows/Linux/macOS)
Jika Anda ingin melakukan konfigurasi manual melalui terminal:
1. Buat virtual environment: `python3 -m venv venv`
2. Aktifkan venv:
   - Mac/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. Install dependensi: `pip install -r requirements.txt`
4. Jalankan aplikasi: `python main.py`

## Panduan Gestur
Program ini menggunakan deteksi ayunan tangan (swipe) untuk memicu aksi:
1. Posisikan telapak tangan terlihat jelas di depan kamera.
2. Lakukan gerakan ayunan dari arah kanan ke kiri secara lebar.
3. Video dan audio akan diputar satu kali hingga durasi berakhir.
4. Selama video berlangsung, program akan mengabaikan input gestur lain hingga pemutaran selesai.

## Struktur Direktori
- `assets/`: Menyimpan file media (video, audio) dan file model AI (`hand_landmarker.task`).
- `main.py`: Kode logika utama aplikasi menggunakan MediaPipe Tasks API.
- `Buka_Kicau_Mania.command`: Script otomasi untuk pengguna macOS.
- `requirements.txt`: Daftar dependensi pustaka Python.

---
Proyek ini dikembangkan untuk tujuan eksperimen Computer Vision dan interaksi manusia-komputer.
