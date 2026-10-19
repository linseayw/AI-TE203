import re

# ------------------------------------------------------------------
# Label gejala untuk ditampilkan ke user
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
           "sering terputus", "putus"],
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
    # Membersihkan spasi berlebih dan mengubah menjadi lowercase
    teks = " ".join(teks.lower().split())

    for kode, kata_kunci_list in GEJALA.items():
        for kata in kata_kunci_list:
            # Menggunakan regex untuk mencocokkan kata secara fleksibel
            pola = rf"\b{re.escape(kata)}\b"
            if re.search(pola, teks):
                return kode
    return None

def bantu():
    keluhan = input("Ceritakan keluhan Wi-Fi Anda: ").strip()
    gejala = deteksi(keluhan)

    print()

    # Menampilkan hasil deteksi gejala
    if gejala:
        print("Gejala terbaca:", LABEL[gejala])
    else:
        print("Gejala tidak spesifik, kami akan menganalisis lebih lanjut.")

    # Triage 1: cek gangguan area lewat aplikasi
    if gejala != "C1":
        print()
        if tanya("Buka aplikasi layanan. Ada info gangguan di area Anda?"):
            print()
            print("Gangguan area")
            print("Ada gangguan dari sisi penyedia. Tunggu sampai layanan pulih. "
                  "Pantau aplikasi berkala. Tidak perlu tindakan lain.")
            return

    # Menentukan cabang langsung dari deteksi gejala
    if gejala:
        cabang = gejala
    else:
        # Triage 2: hanya bertanya jika gejala tidak terdeteksi
        print()
        semua = tanya(
            "Apakah semua perangkat di rumah mengalami hal yang sama?"
        )
        cabang = "A1" if semua else "B1"

    # Menjalankan langkah penanganan sesuai cabang
    langkah_list = LANGKAH[cabang]

    for i, (judul, pesan) in enumerate(langkah_list):
        print()
        print(judul)
        print(pesan)

        terakhir = (i == len(langkah_list) - 1)

        # Langkah terakhir selalu eskalasi tanpa prompt
        if terakhir:
            return

        if tanya("\nSudah bisa digunakan?"):
            print()
            print("Selesai.")
            return


def main():
    print("Asisten Wi-Fi")
    print("Jawab y/n. Ketik q untuk berhenti.")
    while True:
        print()
        pilihan = input("1. Mulai | 0. Keluar: ").strip()
        if pilihan == "0":
            print("Program selesai.")
            return
        if pilihan == "1":
            bantu()
        else:
            print("Pilih 1 atau 0.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nDihentikan.")
