import re

# ------------------------------------------------------------------
# Label gejala untuk ditampilkan ke pengguna
# ------------------------------------------------------------------
LABEL = {
    "A1": "tidak ada internet",
    "A2": "internet lambat",
    "A3": "internet putus-putus",
    "B1": "sinyal lemah",
    "B2": "Wi-Fi tidak terdeteksi",
    "C1": "sandi Wi-Fi bermasalah",
    "E1": "beban perangkat berlebih",
}

# ------------------------------------------------------------------
# Kata kunci untuk mendeteksi gejala dari keluhan pengguna
# ------------------------------------------------------------------
GEJALA = {
    "A1": ["tidak ada internet", "internet mati", "tidak bisa buka",
           "semua situs gagal", "no internet", "offline",
           "tidak konek", "tidak tersambung", "internet hilang"],
    "A2": ["lambat", "lemot", "lelet", "loading lama", "pelan",
           "berat", "ngadat", "susah dibuka"],
    "A3": ["putus-putus", "putus nyambung", "hilang timbul",
           "kadang bisa kadang tidak", "sering putus",
           "sering terputus"],
    "B1": ["sinyal lemah", "sinyal jelek", "jauh dari router",
           "jangkauan", "tidak sampai", "lemah di kamar"],
    "B2": ["tidak terdeteksi", "tidak muncul", "tidak ketemu",
           "tidak terlihat", "hilang dari daftar", "tidak terbaca"],
    "C1": ["sandi salah", "password salah", "tidak tahu sandi",
           "sandi berubah", "ganti sandi", "lupa sandi",
           "tidak bisa masuk", "gagal tersambung"],
    "E1": ["banyak perangkat", "ramai", "penuh", "banyak yang pakai",
           "lemot kalau malam", "lambat kalau ramai"],
}

# ------------------------------------------------------------------
# Alur tiap cabang. Langkah terakhir selalu eskalasi (tanpa prompt).
# ------------------------------------------------------------------
LANGKAH = {
    "A1": [
        ("Restart router",
         "Cabut adaptor daya router, tunggu 30 detik, lalu pasang kembali. "
         "Tunggu 2 menit sampai lampu indikator stabil."),
        ("Ganti DNS",
         "Kemungkinan masalah di DNS. Ikuti panduan di: "
         "https://penyedia.example/panduan/dns"),
        ("Eskalasi ke teknisi",
         "Hubungi CS di 1500-xxx atau buat laporan di aplikasi. "
         "Sampaikan keluhan dan langkah yang sudah dicoba. "
         "Jangan bagikan kata sandi atau OTP."),
    ],
    "A2": [
        ("Kurangi beban jaringan",
         "Putuskan perangkat yang tidak sedang dipakai. "
         "Cek daftar perangkat di aplikasi layanan."),
        ("Restart router",
         "Cabut adaptor daya router, tunggu 30 detik, lalu pasang kembali. "
         "Tunggu 2 menit sampai lampu indikator stabil."),
        ("Ganti DNS",
         "Kemungkinan masalah di DNS. Ikuti panduan di: "
         "https://penyedia.example/panduan/dns"),
        ("Eskalasi ke teknisi",
         "Hubungi CS di 1500-xxx atau buat laporan di aplikasi."),
    ],
    "A3": [
        ("Restart router",
         "Cabut adaptor daya router, tunggu 30 detik, lalu pasang kembali. "
         "Tunggu 2 menit sampai lampu indikator stabil."),
        ("Eskalasi ke teknisi",
         "Hubungi CS di 1500-xxx. Kemungkinan ada masalah pada kabel "
         "atau perangkat di sisi penyedia."),
    ],
    "B1": [
        ("Perbaiki posisi",
         "Pindahkan router ke tempat lebih terbuka, atau dekatkan "
         "perangkat ke router. Hindari dinding tebal dan logam."),
        ("Eskalasi ke teknisi",
         "Hubungi CS di 1500-xxx untuk permintaan perluasan jangkauan."),
    ],
    "B2": [
        ("Sambung ulang",
         "Di perangkat bermasalah: lupakan jaringan Wi-Fi, lalu "
         "sambungkan kembali dengan sandi terbaru."),
        ("Eskalasi ke teknisi",
         "Hubungi CS di 1500-xxx. Kemungkinan masalah pada perangkat "
         "atau pembatasan akun."),
    ],
    "C1": [
        ("Cek sandi terbaru",
         "Buka aplikasi layanan untuk melihat sandi Wi-Fi terbaru. "
         "Jika belum ada, minta reset sandi lewat aplikasi atau CS."),
    ],
    "E1": [
        ("Kurangi beban jaringan",
         "Putuskan perangkat yang tidak sedang dipakai. "
         "Cek daftar perangkat di aplikasi layanan."),
        ("Restart router",
         "Cabut adaptor daya router, tunggu 30 detik, lalu pasang kembali."),
        ("Eskalasi ke teknisi",
         "Hubungi CS di 1500-xxx. Kapasitas router mungkin perlu "
         "ditingkatkan."),
    ],
}


def tanya(pesan):
    while True:
        jawaban = input(pesan + " [y/n/q]: ").strip().lower()
        if jawaban in ("y", "ya"):
            return True
        if jawaban in ("n", "tidak"):
            return False
        if jawaban == "q":
            raise KeyboardInterrupt
        print("Jawab y, n, atau q.")


def deteksi(teks):
    teks = teks.lower()
    for kode, kata in GEJALA.items():
        if any(k in teks for k in kata):
            return kode
    return None
