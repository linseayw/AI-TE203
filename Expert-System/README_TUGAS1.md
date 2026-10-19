# Tugas 1 : Sistem Layanan Gangguan Wi-Fi Sederhana Menggunakan NLP Berbasis Kata Kunci dan Expert System berbasis aturan

# Introduction

Program ini merupakan asisten layanan gangguan Wi-Fi berbasis terminal.
Pengguna menyampaikan keluhan dalam bahasa sehari-hari, kemudian program
mengenali gejala melalui pencocokan kata kunci.

Sistem berbasis aturan menentukan cabang bantuan berdasarkan gejala,
informasi gangguan area, dan jumlah perangkat yang terdampak. Pada setiap
langkah yang bukan langkah terakhir, pengguna mengonfirmasi apakah koneksi
sudah dapat digunakan. Jika berhasil, sesi bantuan selesai. Jika belum,
program melanjutkan ke langkah berikutnya.

## NLP Berbasis Kata Kunci

Natural Language Processing (NLP) digunakan secara sederhana untuk
menghubungkan kalimat keluhan dengan kategori gejala.

Fungsi `deteksi()` mengubah teks menjadi huruf kecil, kemudian mencari
kata kunci menggunakan pencocokan substring.

| Kode | Gejala | Contoh Kata Kunci |
| --- | --- | --- |
| A1 | Tidak ada internet | tidak ada internet, internet mati, offline |
| A2 | Internet lambat | lambat, lemot, loading lama |
| A3 | Internet putus-putus | putus-putus, sering putus, hilang timbul |
| B1 | Sinyal lemah | sinyal lemah, jauh dari router |
| B2 | Wi-Fi tidak terdeteksi | tidak muncul, tidak terlihat |
| C1 | Sandi Wi-Fi bermasalah | sandi salah, lupa sandi |
| E1 | Beban perangkat berlebih | banyak perangkat, banyak yang pakai |

Jika beberapa kategori cocok, program mengambil kategori pertama
berdasarkan urutan pada kamus `GEJALA`. Jika tidak ada kecocokan,
fungsi mengembalikan `None`.

NLP ini berbasis aturan dan belum menggunakan model machine learning.

## Aturan Sistem Pakar

Program menggunakan aturan langsung melalui `if-elif-else`.
Aturan menentukan cabang bantuan, bukan memastikan penyebab kerusakan.

| Prioritas | Kondisi | Keputusan |
| --- | --- | --- |
| 1 | Aplikasi layanan menunjukkan gangguan area | Tampilkan informasi gangguan dan akhiri sesi bantuan |
| 2 | Tidak ada gangguan area dan gejala terdeteksi C1 | Pilih cabang pemeriksaan sandi |
| 3 | Semua perangkat terdampak dan gejala A1, A2, atau A3 | Pilih cabang sesuai gejala tersebut |
| 4 | Semua perangkat terdampak, tetapi gejala bukan A1, A2, atau A3 | Gunakan cabang A1 sebagai pilihan bawaan |
| 5 | Tidak semua perangkat terdampak dan gejala B1, B2, atau E1 | Pilih cabang sesuai gejala tersebut |
| 6 | Tidak semua perangkat terdampak, tetapi gejala bukan B1, B2, atau E1 | Gunakan cabang B1 sebagai pilihan bawaan |

Pilihan bawaan merupakan penyederhanaan pada program dan tidak membuktikan
bahwa masalah sebenarnya adalah gangguan internet umum atau sinyal lemah.

### Langkah pada Setiap Cabang

| Cabang | Urutan Bantuan |
| --- | --- |
| A1 | Restart router → Ganti DNS → Eskalasi ke teknisi |
| A2 | Kurangi beban jaringan → Restart router → Ganti DNS → Eskalasi ke teknisi |
| A3 | Restart router → Eskalasi ke teknisi |
| B1 | Perbaiki posisi → Eskalasi ke teknisi |
| B2 | Sambung ulang → Eskalasi ke teknisi |
| C1 | Cek sandi terbaru |
| E1 | Kurangi beban jaringan → Restart router → Eskalasi ke teknisi |

Pada langkah yang bukan langkah terakhir:

- Jawaban `y` atau `ya` menghentikan sesi dengan pesan `Selesai.`
- Jawaban `n` atau `tidak` melanjutkan ke langkah berikutnya.
- Jawaban `q` menghentikan program.

Langkah terakhir ditampilkan tanpa pertanyaan keberhasilan.
Khusus cabang C1, program langsung kembali ke menu setelah memberikan
panduan sandi karena cabang tersebut hanya memiliki satu langkah.

# Requirement & Library
## Kebutuhan Perangkat Lunak

- Python 3.10 atau lebih baru.
- Terminal atau PowerShell.
- VS Code atau editor lain, opsional.
- Git, opsional untuk mengunduh repositori melalui terminal.

## Library

Kode mengimpor `re`, yang merupakan library bawaan Python untuk
pemrosesan pola teks. Namun, pada versi ini `re` belum digunakan;
pencocokan kata kunci menggunakan operator `in`.

Komponen bawaan yang digunakan:

| Komponen | Fungsi |
| --- | --- |
| `dict` | Menyimpan label, kata kunci, dan langkah bantuan |
| `list` dan `tuple` | Menyimpan urutan tindakan |
| `input()` | Menerima masukan pengguna |
| `print()` | Menampilkan panduan |
| `any()` | Memeriksa kecocokan salah satu kata kunci |
| `enumerate()` | Menelusuri langkah beserta indeksnya |

Tidak ada library eksternal sehingga tidak diperlukan `pip install`.

Periksa instalasi Python:

```bash
python --version
```

Pada sistem yang menggunakan `python3`:

```bash
python3 --version
```

# How to Run

## 1. Clone atau Download

```bash
git clone https://github.com/linseayw/AI-TE403.git
cd NAMA_REPOSITORI
```

Alternatif: download ZIP repositori, ekstrak, kemudian buka foldernya
melalui **File → Open Folder** di VS Code.

## 2. Buka Terminal

Di VS Code, pilih **Terminal → New Terminal**.

Pastikan terminal berada pada folder yang berisi `main.py`.

## 3. Jalankan Program

```bash
python main.py
```

Alternatif pada macOS/Linux:

```bash
python3 main.py
```

## 4. Gunakan Program

1. Pilih menu `1`.
2. Ketik keluhan Wi-Fi.
3. Jawab pertanyaan tentang gangguan area.
4. Jika tidak ada gangguan area, jawab cakupan perangkat yang terdampak.
5. Ikuti panduan yang diberikan.
6. Jawab apakah koneksi sudah bisa digunakan.
7. Pilih menu `0` untuk keluar atau ketik `q` saat menjawab pertanyaan.

URL `https://penyedia.example/panduan/dns` dan nomor `1500-xxx`
merupakan placeholder. Ganti dengan panduan dan kontak resmi penyedia
sebelum program digunakan sebagai layanan nyata.

# Running & Output

## Contoh 1: Berhasil Setelah Restart Router

```text
Asisten Wi-Fi
Jawab y/n. Ketik q untuk berhenti.

1. Mulai | 0. Keluar: 1
Ceritakan keluhan Wi-Fi Anda: tidak ada internet

Gejala terbaca: tidak ada internet

Buka aplikasi layanan. Ada info gangguan di area Anda? [y/n/q]: n

Apakah semua perangkat di rumah mengalami hal yang sama? [y/n/q]: y

Restart router
Cabut adaptor daya router, tunggu 30 detik, lalu pasang kembali. Tunggu 2 menit sampai lampu indikator stabil.

Sudah bisa digunakan? [y/n/q]: y

Selesai.
```

## Contoh 2: Lanjut ke Langkah Berikutnya

Pada cabang A1, jika restart router belum berhasil:

```text
Sudah bisa digunakan? [y/n/q]: n

Ganti DNS
Kemungkinan masalah di DNS. Ikuti panduan di: https://penyedia.example/panduan/dns

Sudah bisa digunakan? [y/n/q]: n

Eskalasi ke teknisi
Hubungi CS di 1500-xxx atau buat laporan di aplikasi. Sampaikan keluhan dan langkah yang sudah dicoba. Jangan bagikan kata sandi atau OTP.
```

## Contoh 3: Gangguan Area

Jika pengguna menjawab `y` pada pertanyaan gangguan area:

```text
Gangguan area
Ada gangguan dari sisi penyedia. Tunggu sampai layanan pulih. Pantau aplikasi berkala. Tidak perlu tindakan lain.
```

Program kemudian kembali ke menu utama.

# Penjelasan Hasil

Pada contoh pertama:

1. Keluhan “tidak ada internet” cocok dengan kata kunci A1.
2. Pengguna menyatakan tidak ada gangguan area.
3. Pengguna menyatakan semua perangkat terdampak.
4. Aturan memilih cabang A1.
5. Program memberikan tindakan restart router.
6. Pengguna mengonfirmasi koneksi berhasil sehingga sesi selesai.

Pada contoh kedua, jawaban `n` menyebabkan program meneruskan tindakan
dalam daftar cabang A1 hingga eskalasi.

Program tidak menjalankan restart, mengganti DNS, atau mengukur koneksi
secara otomatis. Keberhasilan berdasarkan jawaban pengguna.

## Keterbatasan

- Pencocokan kata kunci belum memahami negasi secara menyeluruh.
  Kalimat “internet tidak lambat” masih dapat terdeteksi sebagai A2.
- Hanya satu kategori gejala dipilih meskipun keluhan memuat beberapa gejala.
- Kata kunci umum dapat menghasilkan kategori yang kurang sesuai.
- Pilihan cabang bawaan belum disertai konfirmasi tambahan.
- Cabang B2 menyarankan melupakan jaringan; tindakan ini belum tentu
  sesuai jika nama jaringan sama sekali tidak terlihat.
- Gangguan internet tidak selalu disebabkan DNS; rekomendasi perubahan
  DNS memerlukan pemeriksaan dan panduan yang sesuai.

Restart hanya dilakukan pada router yang boleh dikelola pengguna,
dengan mempertimbangkan pengguna lain. Restart daya berbeda dari
factory reset; jangan menekan tombol RESET.

# Kesimpulan

Program menggabungkan NLP berbasis kata kunci dan sistem expert berbasis aturan
untuk memberikan panduan awal gangguan Wi-Fi melalui terminal.

Keluhan pengguna menentukan kategori gejala. Informasi gangguan area
dan cakupan perangkat menentukan cabang bantuan. Jawaban keberhasilan
menentukan apakah sesi berhenti atau dilanjutkan.
