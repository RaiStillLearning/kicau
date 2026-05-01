#!/bin/bash
# Pindah ke direktori tempat script ini berada
cd "$(dirname "$0")"

echo "------------------------------------------------"
echo "🚀 Memulai Kicau Mania AI Overlay..."
echo "------------------------------------------------"

# Cek apakah venv sudah ada dan sudah terinstall library-nya
if [ ! -f "venv/.installed" ]; then
    echo "🔧 Setup lingkungan Python terdeteksi belum lengkap!"
    echo "📦 Mengunduh pustaka (ini butuh waktu beberapa saat)..."
    
    # Mencari Python yang stabil (MediaPipe butuh 3.11 atau 3.12 agar lancar)
    if command -v python3.11 &>/dev/null; then
        STABLE_PY="python3.11"
    elif command -v python3.12 &>/dev/null; then
        STABLE_PY="python3.12"
    else
        STABLE_PY="python3"
    fi
    
    echo "🐍 Menggunakan $STABLE_PY untuk membuat lingkungan..."
    
    # Buat venv jika belum ada
    if [ ! -d "venv" ]; then
        $STABLE_PY -m venv venv
    fi
    
    # Install requirements dan pastikan berhasil
    echo "📦 Mengunduh pustaka (ini butuh waktu beberapa saat)..."
    ./venv/bin/pip install --upgrade pip --no-cache-dir
    
    if ./venv/bin/pip install -r requirements.txt --no-cache-dir; then
        # Verifikasi sebentar apakah import berhasil
        if ./venv/bin/python3 -c "import cv2; import mediapipe" &>/dev/null; then
            touch venv/.installed
            echo "✅ Setup selesai!"
        else
            echo "❌ Setup selesai tapi pustaka tidak terbaca. Mencoba perbaikan..."
            ./venv/bin/pip install mediapipe --force-reinstall --no-cache-dir
            touch venv/.installed
        fi
    else
        echo "❌ Gagal mengunduh pustaka. Periksa koneksi internet Anda."
        read -p "Tekan Enter untuk keluar..."
        exit 1
    fi
fi

# Cek apakah file model MediaPipe sudah ada
MODEL_FILE="assets/hand_landmarker.task"
if [ ! -f "$MODEL_FILE" ]; then
    echo "📦 Mengunduh model AI MediaPipe (ini butuh waktu sejenak)..."
    mkdir -p assets
    curl -L -o "$MODEL_FILE" https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
fi

# Jalankan aplikasi menggunakan python dari venv secara langsung
echo "🚀 Jalankan aplikasi..."
./venv/bin/python3 main.py

# Tunggu user tekan enter jika terjadi error supaya terminal tidak langsung tutup
if [ $? -ne 0 ]; then
    echo "⚠️ Terjadi kesalahan saat menjalankan aplikasi."
    read -p "Tekan Enter untuk keluar..."
fi