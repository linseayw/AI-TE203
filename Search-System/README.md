# Search Algorithm (Algoritme Pencarian)

## Deskripsi Umum
**Search Algorithm** (Algoritme Pencarian) adalah prosedur matematis atau langkah-langkah sistematis yang digunakan untuk menemukan data, elemen, atau nilai tertentu di dalam suatu himpunan data (seperti *array*, *list*, *tree*, atau *graph*). 

Efisiensi dari sebuah algoritme pencarian sangat menentukan performa dari suatu aplikasi, terutama saat menangani volume data yang besar.

---

## Klasifikasi Algoritme Pencarian

### 1. Pencarian Data Linier (Sequential & Ordered Search)
Digunakan pada struktur data satu dimensi seperti *array* atau *list*.

* **Linear Search (Pencarian Sekuensial)**
  * **Prinsip Kerja:** Memeriksa setiap elemen data satu per satu dari indeks awal hingga indeks akhir sampai elemen yang dicari ditemukan.
  * **Kompleksitas Waktu:** $O(n)$
  * **Kelebihan:** Sangat mudah diimplementasikan dan dapat digunakan pada data yang acak (tidak terurut).

* **Binary Search (Pencarian Biner)**
  * **Prinsip Kerja:** Menggunakan pendekatan *divide and conquer*. Membagi area pencarian menjadi dua bagian secara berulang pada data yang **sudah terurut**.
  * **Kompleksitas Waktu:** $O(\log n)$
  * **Kelebihan:** Sangat cepat untuk dataset skala besar.

---

### 2. Pencarian Graf dan Pohon (Graph & Tree Search)
Digunakan pada struktur data berupa jaringan (*graph*) atau hierarki (*tree*).

* **Breadth-First Search (BFS)**
  * **Prinsip Kerja:** Menjelajahi simpul (*node*) secara melebar, memeriksa seluruh tetangga pada satu level sebelum beralih ke level berikutnya.
  * **Penggunaan:** Mencari jalur terpendek pada graf tanpa bobot.

* **Depth-First Search (DFS)**
  * **Prinsip Kerja:** Menjelajahi simpul sedalam mungkin ke satu jalur hingga buntu, lalu melakukan *backtracking* untuk memilih jalur lain.
  * **Penggunaan:** Pendeteksian siklus, penelusuran labirin (*maze solving*), dan pengurutan topologis.

* **A* (A-Star) Search**
  * **Prinsip Kerja:** Menggabungkan biaya jalur (*cost*) dan fungsi perkiraan jarak (*heuristic*) untuk menemukan jalur paling efisien.
  * **Penggunaan:** Sistem navigasi GPS dan *pathfinding* pada game/robotika otonom.
    print(f"Elemen ditemukan pada indeks ke-{result}")
else:
    print("Elemen tidak ditemukan")
