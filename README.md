# 🌿 AnakSehat AI — Analisis Stunting Balita Usia 0–24 Bulan

Proyek ini berisi analisis data stunting balita menggunakan dataset AnakSehat AI. Terdiri dari notebook eksplorasi data dan dashboard interaktif berbasis Streamlit.

🔗 **Live Dashboard:** [https://dashboard-data-anaksehat.streamlit.app/](https://dashboard-data-anaksehat.streamlit.app/)

---

## 📁 Struktur Folder

```
dashboard_anaksehat/
│
├── dashboard_anaksehat.py          # Aplikasi dashboard Streamlit
├── data_final_AnakSehat.csv        # Dataset final (sudah melalui proses cleaning & feature engineering)
├── notebook.ipynb                  # Notebook analisis lengkap
├── Data_Dictionary_AnakSehat.docx  # Dokumentasi kolom dataset
└── README.md                       # File ini
```

---

## 📊 Dataset

| Informasi | Detail |
|---|---|
| **Nama** | AnakSehat AI - Stunting Detection Dataset |
| **File** | `data_final_AnakSehat.csv` |
| **Jumlah Baris Awal** | 100.000 baris |
| **Jumlah Baris Bersih** | 92.692 baris (7.308 duplikat dihapus) |
| **Jumlah Kolom** | 19 kolom |
| **Rentang Usia** | 0 – 24 bulan |
| **Standar Referensi** | WHO Child Growth Standards |

### Kolom Dataset

| Kolom | Tipe | Keterangan |
|---|---|---|
| `jenis_kelamin` | object | Jenis kelamin balita: Laki-laki / Perempuan |
| `umur_bulan` | int | Usia balita dalam satuan bulan (0–24) |
| `tinggi_cm` | float | Tinggi badan balita dalam sentimeter |
| `berat_kg` | float | Berat badan balita dalam kilogram |
| `stunting` | object | Status stunting balita — **variabel target** |
| `wasting` | object | Status wasting balita berdasarkan standar WHO |
| `jenis_kelamin_enc` | int | Encoding biner jenis kelamin |
| `wasting_enc` | int | Encoding ordinal status wasting |
| `stunting_enc` | int | Encoding ordinal status stunting |
| `haz_zscore` | float | Height-for-Age Z-Score (WHO) |
| `waz_zscore` | float | Weight-for-Age Z-Score (WHO) |
| `baz_zscore` | float | BMI-for-Age Z-Score (WHO) |
| `bmi` | float | Body Mass Index dalam kg/m² |
| `kategori_bmi` | object | Kategori BMI balita berdasarkan threshold WHO |
| `weight_height_ratio` | float | Rasio berat badan terhadap tinggi badan |
| `growth_composite_index` | float | Indeks pertumbuhan komposit dengan skala 0–100 |
| `kategori_gci` | object | Kategori GCI: Risiko Tinggi / Perlu Perhatian / Tumbuh Baik |
| `stunting_dari_haz` | object | Klasifikasi ulang status stunting berdasarkan HAZ (untuk validasi) |


> Penjelasan lengkap setiap kolom tersedia pada file `Data_Dictionary_AnakSehat.docx`.

---

## 📓 Notebook (`notebook.ipynb`)

Notebook ini memuat seluruh alur analisis data secara sistematis, mulai dari pengumpulan data hingga pembuatan fitur baru.

### Alur Analisis

```
1. Import Library
2. Data Wrangling
   ├── Gathering Data        → memuat dataset dari Google Drive
   ├── Assessing Data        → pemeriksaan missing value, duplikat, dan tipe data
   └── Cleaning Data         → penghapusan duplikat dan standarisasi nama kolom
3. Exploratory Data Analysis (EDA)
   └── analisis distribusi stunting, usia, tinggi badan, berat badan, dan jenis kelamin
4. Feature Engineering
   ├── Encoding kolom kategorikal
   ├── HAZ Z-Score (Height-for-Age)
   ├── WAZ Z-Score (Weight-for-Age)
   ├── BAZ Z-Score (BMI-for-Age)
   ├── BMI dan Weight-Height Ratio
   └── Growth Composite Index (GCI)
5. Data Dictionary
6. Visualization & Explanatory Analysis
   ├── Pertanyaan 1 → persentase stunting per kelompok usia dan jenis kelamin
   ├── Pertanyaan 2 → karakteristik fisik per kategori stunting
   ├── Pertanyaan 3 → distribusi jumlah kasus stunting
   ├── Pertanyaan 4 → hubungan antar variabel numerik
   └── Pertanyaan 5 → pola pertumbuhan balita usia 0–24 bulan

```

### Library yang Digunakan

```python
pandas
numpy
matplotlib
seaborn
sklearn (MinMaxScaler)
```

---

## 🖥️ Dashboard (`dashboard_anaksehat.py`)

Dashboard interaktif yang menyajikan visualisasi dari 5 pertanyaan bisnis beserta insight dan kesimpulan analisis.

### Fitur Dashboard

| Tab | Konten | Kontrol Interaktif |
|---|---|---|
| **P1 · Usia & Gender** | Persentase stunting per kelompok usia dan jenis kelamin | Pilih tipe chart (Stacked Bar / Grouped Bar), filter status stunting |
| **P2 · Karakteristik** | Distribusi variabel numerik per kategori stunting | Pilih variabel, tipe chart, pemisahan per jenis kelamin |
| **P3 · Distribusi Kasus** | Jumlah kasus stunting per kelompok usia atau jenis kelamin | Toggle tampilan jumlah vs persentase |
| **P4 · Hubungan Variabel** | Scatter plot hubungan antar variabel numerik | Pilih sumbu X dan Y, jumlah sampel data |
| **P5 · Pola Pertumbuhan** | Pola pertumbuhan balita dari usia 0–24 bulan | Pilih variabel, filter status dan jenis kelamin, toggle confidence interval |
| **Kesimpulan** | Rangkuman temuan utama dan rekomendasi | — |

Filter global pada sidebar (kelompok usia, jenis kelamin, status stunting) berlaku untuk seluruh tab secara bersamaan.

### Library yang Digunakan

```python
streamlit
pandas
matplotlib
seaborn
```

---

## ⚙️ Cara Menjalankan Dashboard Secara Lokal

### 1. Pastikan Python telah terinstal
```bash
python --version
# Minimal Python 3.8
```

### 2. Instal library yang diperlukan
```bash
pip install streamlit pandas matplotlib seaborn
```

### 3. Pastikan struktur folder telah sesuai
```
dashboard_anaksehat/
├── dashboard_anaksehat.py
└── data_final_AnakSehat.csv
```

### 4. Jalankan dashboard
```bash
cd dashboard_anaksehat
streamlit run dashboard_anaksehat.py
```

### 5. Akses melalui browser
Dashboard akan terbuka secara otomatis. Apabila tidak terbuka otomatis, akses melalui:
```
http://localhost:8501
```

---

## ❓ Pertanyaan Bisnis

Berikut adalah 5 pertanyaan bisnis yang dijawab dalam notebook dan dashboard:

1. Pada kelompok usia serta jenis kelamin manakah yang memiliki presentase stunting tertinggi ditemukan pada balita dalam rentang usia 0 sampai 24 bulan?
2. Bagaimana distribusi dan karakteristik tinggi badan, berat badan, usia, serta jenis kelamin pada masing-masing kategori status stunting balita usia 0–24 bulan?
3. Bagaimana distribusi jumlah kasus stunting pada setiap kelompok usia dan jenis kelamin balita usia 0–24 bulan dalam dataset AnakSehat AI?
4. Bagaimana hubungan antara tinggi badan, berat badan, dan usia terhadap kategori status stunting balita berdasarkan hasil visualisasi data pada dataset AnakSehat AI?
5. Bagaimana perbedaan pola pertumbuhan tinggi badan dan berat badan antara balita normal, stunted, dan severely stunted usia 0–24 bulan berdasarkan dataset AnakSehat AI?

---

## 📌 Catatan

- Seluruh nilai z-score dihitung menggunakan tabel referensi **WHO Child Growth Standards** dengan median dan standar deviasi per kelompok usia dan jenis kelamin.
- Dashboard dikembangkan menggunakan **Streamlit** dengan visualisasi berbasis **Matplotlib** dan **Seaborn**.