# Simple Multi-Agent System dengan Google Gemini

Sistem multi-agent sederhana untuk tugas mata kuliah, dibangun dengan **Praval Framework** dan **Google Gemini Free Tier**. Dua agen — **Researcher** dan **Writer** — bekerja berurutan untuk menghasilkan artikel ringkas dari sebuah topik.

---

## Fitur

- Sepenuhnya gratis (Gemini Free Tier, tanpa kartu kredit)
- Dua agen dengan komunikasi via `broadcast()`
- Output otomatis disimpan ke `hasil_tugas.txt`
- Dependensi minimal: `praval` + `google-generativeai`

---

## Arsitektur

```
initial_data (type: "research_request")
         │
         ▼
   [researcher]  ← responds_to: ["research_request"]
         │ broadcast(type: "research_complete")
         ▼
    [writer]    ← responds_to: ["research_complete"]
         │
       done → hasil_tugas.txt
```

Agen tidak saling mengenal — mereka hanya bereaksi terhadap tipe pesan. Menambah agen baru cukup mendeklarasikan `@agent` baru tanpa mengubah agen lama.

---

## Persyaratan

- Python 3.9+
- Akun Google (untuk API key gratis)
- Koneksi internet

Dependensi:
```bash
pip install praval google-generativeai
```

---

## Instalasi

**1. Clone & masuk ke folder**
```bash
git clone https://github.com/your-username/simple-multi-agent-gemini.git
cd simple-multi-agent-gemini
```

**2. (Disarankan) Virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
```

**3. Install dependensi**
```bash
pip install -r requirements.txt
```

**4. Dapatkan API key gratis**
- Buka https://aistudio.google.com/apikey
- Login dengan akun Google
- Klik **Create API key** → salin

**5. Set environment variable** (di terminal yang sama dengan tempat menjalankan skrip)

```bash
# Linux / macOS
export GEMINI_API_KEY="api-key-kamu"

# Windows PowerShell
$env:GEMINI_API_KEY = "api-key-kamu"
```

---

## Cara Menjalankan

```bash
python tugas_multi_agent.py
```

Output yang diharapkan:

```
=======================================================
 Sistem Multi-Agent Tugas Mata Kuliah (Gemini Gratis)
=======================================================
 Model  : gemini-2.0-flash
 Topik  : sejarah kopi di Indonesia

[Researcher] Mulai meneliti: sejarah kopi di Indonesia
[Researcher] Fakta yang ditemukan:
1. ...
2. ...
3. ...

[Writer] Menerima hasil riset tentang: sejarah kopi di Indonesia

[Writer] Artikel yang dihasilkan:
----------------------------------------
Sejarah kopi di Indonesia berakar pada era kolonial Belanda...
----------------------------------------

[Writer] Hasil disimpan ke: hasil_tugas.txt

[Sistem] Semua agen selesai diproses.
```

---

## Kustomisasi

**Ganti topik** — edit konstanta di atas file:
```python
TOPIC = "dampak AI pada pendidikan"
```

**Ganti model** — edit `MODEL_NAME`:
```python
MODEL_NAME = "gemini-1.5-flash"   # fallback jika model utama tidak tersedia
```

**Tambah agen ketiga (Editor)** — deklarasikan `@agent` baru dengan `responds_to=["draft_ready"]`, lalu ubah Writer agar broadcast `type: "draft_ready"` dan pass agen baru ke `start_agents(...)`.

---

## Troubleshooting

| Error | Solusi |
|---|---|
| `GEMINI_API_KEY belum di-set` | Set ulang di terminal yang sama |
| `400 API key not valid` | Buat key baru di AI Studio |
| `404 model not found` | Ganti `MODEL_NAME` ke `gemini-1.5-flash` |
| `429 Resource exhausted` | Rate limit free tier — tunggu 1–2 menit |
| `ModuleNotFoundError: praval` | Jalankan `pip install praval` |

---

## Catatan Keamanan

- **Jangan commit API key** ke Git/GitHub.
- Jika key bocor, segera cabut di https://aistudio.google.com/apikey.
- Free tier Google dapat memakai prompt untuk meningkatkan produk — jangan kirim data sensitif.

---

## Struktur Proyek

```
simple-multi-agent-gemini/
├── tugas_multi_agent.py    # Skrip utama
├── README.md
├── requirements.txt
└── hasil_tugas.txt         # Output (generated)
```

---

## Lisensi

MIT License — bebas digunakan untuk keperluan edukatif.
