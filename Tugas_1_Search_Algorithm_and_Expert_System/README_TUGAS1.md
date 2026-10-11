# Tugas 1 : Sistem Layanan Gangguan Wi-Fi Sederhana Menggunakan Algoritma BFS dan NLP Berbasis Kata Kunci 

**Mata Kuliah:** AI (Kecerdasan Buatan)  
**Kelas:** TE403  
**Kelompok:** 4

# Introduction

Program ini menggabungkan dua pendekatan kecerdasan buatan:

1. **Expert System:** memeriksa gejala laptop menggunakan aturan
   `if-elif-else` untuk memberikan dugaan masalah dan rekomendasi layanan.
2. **Search Algorithm:** menggunakan Breadth-First Search (BFS) untuk
   mencari rute menuju lokasi layanan yang direkomendasikan.

Pengguna menjawab pertanyaan melalui terminal. Hasil sistem pakar
menentukan tujuan pencarian BFS sehingga kedua pendekatan saling terhubung.

## Aturan Sistem Pakar

| Aturan | Kondisi | Tujuan Layanan |
| --- | --- | --- |
| R1 | Laptop tidak menyala | Pusat Servis |
| R2 | Laptop menyala dan panas berlebihan | Pusat Servis |
| R3 | Laptop menyala, tidak panas, tetapi lambat | Lab Komputer |
| R4 | Laptop menyala, tidak panas, dan tidak lambat | Tidak diperlukan |

Aturan diperiksa dari R1 hingga R4. Jika beberapa gejala muncul bersamaan,
aturan dengan prioritas lebih tinggi digunakan.

Implementasi ini merupakan sistem berbasis aturan langsung, tanpa
forward chaining bertingkat. Hasilnya merupakan dugaan awal untuk latihan.

## Pencarian BFS

BFS menelusuri lokasi menggunakan antrean. Lokasi yang sudah ditemukan
ditandai agar tidak diperiksa berulang kali.

Peta menggunakan graf dua arah tanpa bobot. Karena itu, rute BFS memiliki
jumlah sisi paling sedikit, bukan berdasarkan jarak fisik atau waktu tempuh.

# Requirement & Library

## Kebutuhan

- Python 3.10 atau lebih baru.
- Terminal atau terminal bawaan VS Code.
- Git, jika mengunduh menggunakan `git clone`.

## Library

| Library/Komponen | Kegunaan | Instalasi |
| --- | --- | --- |
| `collections.deque` | Antrean BFS | Bawaan Python |
| `dict`, `list`, `set` | Peta, jalur, dan penanda simpul | Bawaan Python |
| `input`, `print` | Interaksi terminal | Bawaan Python |

Jika Python belum terpasang, unduh dari:
https://www.python.org/downloads/

Periksa instalasi:

```bash
python --version
```

Pada sistem yang menggunakan `python3`:

```bash
python3 --version
```

# How to Run

## 1. Download Repositori

Download ZIP, ekstrak, lalu buka folder proyek melalui
**File → Open Folder** di VS Code.

## 2. Periksa Berkas

Pastikan folder proyek berisi:

- `main.py`: kode program.
- `README.md`: dokumentasi.

## 3. Buka Terminal

Di VS Code, pilih **Terminal → New Terminal**.

Pastikan terminal berada pada folder yang berisi `main.py`.

## 4. Jalankan Program

```bash
python main.py
```

Alternatif pada macOS/Linux:

```bash
python3 main.py
```

## 5. Gunakan Menu

1. Ketik `1` untuk memeriksa gejala laptop.
2. Jawab pertanyaan dengan `y` untuk ya atau `n` untuk tidak.
3. Baca aturan yang aktif dan rekomendasi.
4. Pilih lokasi awal jika diperlukan pencarian rute.
5. Program menampilkan rute BFS dan jumlah langkah.
6. Ketik `0` pada menu utama untuk keluar.

# Running & Output

## Contoh Interaksi

```text
=== SISTEM PAKAR LAPTOP DAN PENCARIAN RUTE ===
1. Periksa gejala dan cari rute layanan
0. Keluar
Pilih menu: 1
Apakah laptop bisa menyala? (y/n): y
Apakah laptop panas berlebihan saat digunakan? (y/n): n
Apakah laptop berjalan lambat saat digunakan? (y/n): y

Aturan aktif: R3: laptop menyala, tidak panas, tetapi lambat
Hasil: Perlu pemeriksaan aplikasi dan penggunaan sumber daya.

Lokasi awal:
1. Gerbang
2. Perpustakaan
3. Kantin
4. Lab Komputer
5. Pusat Servis
Pilih nomor lokasi: 1
Tujuan layanan: Lab Komputer
Rute BFS: Gerbang -> Perpustakaan -> Lab Komputer
Jumlah langkah: 2
```

## Penjelasan Hasil

- Fakta masukan memenuhi aturan R3.
- Sistem pakar menentukan Lab Komputer sebagai tujuan layanan.
- BFS mencari jalur dari Gerbang menuju Lab Komputer.
- Jalur yang ditemukan memiliki dua langkah.

Jika lokasi awal sama dengan tujuan, jumlah langkah adalah nol.
Jika tidak ada indikasi masalah dari gejala yang ditanyakan, program
tidak meminta lokasi awal dan tidak menjalankan pencarian rute.

## Kesimpulan

Program menunjukkan bahwa keputusan sistem pakar dapat menjadi masukan
bagi algoritma pencarian. Sistem pakar menentukan tujuan layanan,
sedangkan BFS menentukan jalur menuju tujuan tersebut.
