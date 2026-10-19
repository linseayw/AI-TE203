# Pencarian Angka Menggunakan Binary Search Rekursif

## Introduction

Program ini menerapkan **Binary Search (pencarian biner) secara rekursif** untuk memeriksa apakah suatu angka terdapat dalam daftar terurut.

Program membuat 10 angka acak yang berbeda, mengurutkannya dari kecil ke besar, kemudian memilih angka target secara acak. Fungsi `binladen()` melakukan pencarian dan mengembalikan:

- `True` jika angka ditemukan.
- `False` jika angka tidak ditemukan.

Nama `binladen` merupakan nama fungsi dalam kode; algoritma yang digunakan adalah **Binary Search**, bukan BFS.

### Cara Kerja Algoritma

1. Periksa batas pencarian. Jika `start > stop`, ruang pencarian sudah kosong dan fungsi mengembalikan `False`.
2. Tentukan indeks tengah dengan `middle = (start + stop) // 2`.
3. Jika nilai tengah sama dengan target, kembalikan `True`.
4. Jika nilai tengah lebih besar daripada target, cari secara rekursif pada bagian kiri.
5. Jika nilai tengah lebih kecil daripada target, cari secara rekursif pada bagian kanan.

Setiap pemanggilan rekursif memperkecil ruang pencarian sekitar setengahnya. **Daftar harus sudah terurut** agar algoritma dapat menentukan bagian yang perlu diperiksa.

### Parameter Fungsi

```python
binladen(element, collection, start, stop)
```

| Parameter | Keterangan |
| --- | --- |
| `element` | Angka yang dicari. |
| `collection` | Daftar angka yang sudah diurutkan menaik. |
| `start` | Indeks awal pencarian, bersifat inklusif. |
| `stop` | Indeks akhir pencarian, bersifat inklusif. |

Pemanggilan awal menggunakan indeks `0` sampai `len(collection) - 1`.

### Pembentukan Data

```python
binladen_wanted_list = sorted(random.sample(range(1, 100), 10))
wanted = random.randint(1, 100)
```

- `range(1, 100)` menyediakan bilangan 1–99; angka 100 tidak termasuk.
- `random.sample(..., 10)` mengambil 10 angka berbeda tanpa pengulangan.
- `sorted()` mengurutkan daftar secara menaik.
- `random.randint(1, 100)` memilih target dari 1–100, termasuk kedua batasnya.

**Catatan:** jika target adalah 100, hasil selalu `False` karena angka 100 tidak mungkin ada dalam daftar.

## Requirement

### Perangkat Lunak

- Python 3.
- Terminal, Command Prompt, atau PowerShell.
- Editor kode seperti VS Code, opsional.

### Library dan Komponen

Program hanya menggunakan modul bawaan Python, sehingga **tidak diperlukan instalasi library melalui `pip`**.

| Komponen | Fungsi |
| --- | --- |
| `random` | Modul untuk menghasilkan data acak. |
| `random.sample()` | Mengambil 10 angka unik dari rentang yang tersedia. |
| `random.randint()` | Memilih angka target secara acak. |
| `range()` | Menyediakan rentang bilangan. |
| `sorted()` | Mengurutkan daftar angka. |
| `len()` | Menghitung jumlah elemen daftar. |
| `print()` | Menampilkan target, daftar, dan hasil pencarian. |

Periksa instalasi Python:

```bash
python --version
```

Jika sistem menggunakan perintah `python3`:

```bash
python3 --version
```

## How to Run

1. Simpan kode program yang diberikan ke dalam file bernama `main.py`.
2. Buka folder tempat file tersebut disimpan. Jika menggunakan VS Code, pilih **File → Open Folder**.
3. Buka terminal. Pada VS Code, pilih **Terminal → New Terminal**.
4. Pastikan terminal berada pada folder yang berisi `main.py`.
5. Jalankan:

```bash
python main.py
```

Jika sistem menggunakan `python3`:

```bash
python3 main.py
```

Program langsung menghasilkan data, menjalankan pencarian, menampilkan hasil, lalu selesai. **Tidak ada input yang perlu diketik oleh pengguna.** Jalankan ulang perintah untuk melakukan percobaan berikutnya.

## Running dan Output

Contoh di bawah merupakan ilustrasi keluaran yang mungkin muncul, bukan hasil yang selalu sama. Daftar dan target dibangkitkan secara acak sehingga dapat berubah pada setiap eksekusi.

### Contoh 1: Angka Ditemukan

```text
binladen is searching for 42 in [5, 12, 18, 27, 35, 42, 56, 68, 79, 91]
True
```

Penjelasan proses:

| Tahap | Batas indeks | Indeks tengah | Nilai tengah | Keputusan |
| --- | --- | --- | --- | --- |
| 1 | 0–9 | 4 | 35 | Target 42 lebih besar; cari ke kanan. |
| 2 | 5–9 | 7 | 68 | Target 42 lebih kecil; cari ke kiri. |
| 3 | 5–6 | 5 | 42 | Target ditemukan; kembalikan `True`. |

Tabel ini menjelaskan proses internal. Program asli hanya mencetak dua baris keluaran dan tidak menampilkan setiap tahap pencarian.

### Contoh 2: Angka Tidak Ditemukan

```text
binladen is searching for 50 in [5, 12, 18, 27, 35, 42, 56, 68, 79, 91]
False
```

Angka 50 tidak terdapat dalam daftar. Pencarian mempersempit batas hingga `start > stop`, kemudian mengembalikan `False`.

### Contoh 3: Target di Luar Rentang Data

```text
binladen is searching for 100 in [5, 12, 18, 27, 35, 42, 56, 68, 79, 91]
False
```

Target 100 tidak ditemukan karena daftar hanya mengambil angka dari 1–99.

### Arti Keluaran

| Keluaran | Arti |
| --- | --- |
| Baris pertama | Menampilkan angka target dan daftar terurut yang diperiksa. |
| `True` | Target terdapat dalam daftar. |
| `False` | Target tidak terdapat dalam daftar. |

Fungsi hanya mengembalikan status ditemukan atau tidak ditemukan, bukan indeks posisi target.

### Kompleksitas Pencarian

Untuk daftar berisi `n` elemen:

- Waktu pencarian kasus terburuk: **O(log n)**.
- Waktu pencarian kasus terbaik: **O(1)**, jika target langsung ditemukan pada posisi tengah.
- Ruang tambahan kasus terburuk: **O(log n)** untuk tumpukan pemanggilan rekursif.

Kompleksitas tersebut khusus untuk fungsi pencarian. Pengurutan awal dengan `sorted()` memiliki kompleksitas waktu kasus terburuk **O(n log n)**.

