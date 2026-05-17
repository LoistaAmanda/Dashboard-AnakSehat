# 🌿 AnakSehat AI — Analisis Stunting Balita Usia 0–24 Bulan

Proyek ini berisi analisis data stunting balita menggunakan dataset AnakSehat AI. Terdiri dari notebook eksplorasi data dan dashboard interaktif berbasis Streamlit.

---

## 📁 Struktur Folder

```
dashboard_anaksehat/
│
├── dashboard_anaksehat.py       # Aplikasi dashboard Streamlit
├── data_final_AnakSehat.csv     # Dataset final (sudah melalui proses cleaning & feature engineering)
├── notebook.ipynb               # Notebook analisis lengkap
├── Data_Dictionary_AnakSehat.docx  # Dokumentasi kolom dataset
└── README.md                    # File ini
```

---

## 📊 Dataset

| Info | Detail |
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
| `jenis_kelamin` | object | Laki-laki / Perempuan |
| `umur_bulan` | int | Usia balita (0–24 bulan) |
| `tinggi_cm` | float | Tinggi badan (cm) |
| `berat_kg` | float | Berat badan (kg) |
| `stunting` | object | Status stunting — **variabel target** |
| `wasting` | object | Status wasting balita |
| `jenis_kelamin_enc` | int | Encoding biner jenis kelamin |
| `wasting_enc` | int | Encoding ordinal wasting |
| `stunting_enc` | int | Encoding ordinal stunting |
| `haz_zscore` | float | Height-for-Age Z-Score (WHO) |
| `waz_zscore` | float | Weight-for-Age Z-Score (WHO) |
| `baz_zscore` | float | BMI-for-Age Z-Score (WHO) |
| `bmi` | float | Body Mass Index (kg/m²) |
| `kategori_bmi` | object | Kategori BMI balita |
| `weight_height_ratio` | float | Rasio berat / tinggi |
| `growth_composite_index` | float | Indeks pertumbuhan komposit (0–100) |
| `kategori_gci` | object | Kategori GCI (Risiko Tinggi / Perlu Perhatian / Tumbuh Baik) |
| `stunting_dari_haz` | object | Klasifikasi ulang dari HAZ (untuk validasi) |
| `kelompok_usia` | category | Pengelompokan usia per 6 bulan |

> Penjelasan lengkap ada di `Data_Dictionary_AnakSehat.docx`

---

## 📓 Notebook (`notebook.ipynb`)

Notebook berisi alur analisis data secara lengkap dari awal hingga akhir.

### Alur Notebook

```
1. Import Library
2. Data Wrangling
   ├── Gathering Data        → load dari Google Drive
   ├── Assessing Data        → cek missing value, duplikat, tipe data
   └── Cleaning Data         → hapus duplikat, rename kolom
3. Exploratory Data Analysis (EDA)
   └── distribusi stunting, usia, tinggi, berat, jenis kelamin
4. Feature Engineering
   ├── Encoding kolom kategorikal
   ├── HAZ Z-Score (Height-for-Age)
   ├── WAZ Z-Score (Weight-for-Age)
   ├── BAZ Z-Score (BMI-for-Age)
   ├── BMI & Weight-Height Ratio
   └── Growth Composite Index (GCI)
5. Data Dictionary
6. Visualization & Explanatory Analysis
   ├── Pertanyaan 1 → stunting per kelompok usia & gender
   ├── Pertanyaan 2 → karakteristik per kategori stunting
   ├── Pertanyaan 3 → distribusi jumlah kasus
   ├── Pertanyaan 4 → hubungan antar variabel
   └── Pertanyaan 5 → pola pertumbuhan 0–24 bulan

```

### Library yang Digunakan (Notebook)

```python
pandas
numpy
matplotlib
seaborn
sklearn (MinMaxScaler)
```

---

## 🖥️ Dashboard (`dashboard_anaksehat.py`)

Dashboard interaktif yang menampilkan visualisasi dari 5 pertanyaan bisnis beserta insight dan kesimpulan.

### Fitur Dashboard

| Tab | Isi | Kontrol Interaktif |
|---|---|---|
| **P1 · Usia & Gender** | Persentase stunting per kelompok usia & gender | Pilih tipe chart (Stacked/Grouped Bar), filter status |
| **P2 · Karakteristik** | Distribusi variabel per kategori stunting | Pilih variabel, tipe chart, pisah gender |
| **P3 · Distribusi Kasus** | Jumlah kasus per kelompok usia / gender | Toggle jumlah vs persentase |
| **P4 · Hubungan Variabel** | Scatter plot antar variabel numerik | Pilih sumbu X & Y, jumlah sampel |
| **P5 · Pola Pertumbuhan** | Pola pertumbuhan 0–24 bulan | Pilih variabel, filter status & gender, toggle CI |
| **Kesimpulan** | Ringkasan temuan & rekomendasi | — |

**Filter global di sidebar:** kelompok usia, jenis kelamin, status stunting — semua tab ikut berubah otomatis.

### Library yang Digunakan (Dashboard)

```python
streamlit
pandas
matplotlib
seaborn
```

---

## ⚙️ Cara Menjalankan Dashboard

### 1. Pastikan Python sudah terinstall
```bash
python --version
# minimal Python 3.8
```

### 2. Install library yang dibutuhkan
```bash
pip install streamlit pandas matplotlib seaborn
```

### 3. Pastikan struktur folder sudah benar
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

### 5. Buka di browser
Dashboard akan otomatis terbuka di browser. Kalau tidak terbuka otomatis, akses manual di:
```
http://localhost:8501
```

---

## ❓ Pertanyaan Bisnis

Berikut 5 pertanyaan bisnis yang dijawab dalam notebook dan dashboard:

1. Pada kelompok usia serta jenis kelamin manakah yang memiliki persentase stunting tertinggi pada balita usia 0–24 bulan?
2. Bagaimana distribusi dan karakteristik tinggi badan, berat badan, usia, serta jenis kelamin pada masing-masing kategori status stunting?
3. Bagaimana distribusi jumlah kasus stunting pada setiap kelompok usia dan jenis kelamin balita?
4. Bagaimana hubungan antara tinggi badan, berat badan, dan usia terhadap kategori status stunting berdasarkan hasil visualisasi?
5. Bagaimana perbedaan pola pertumbuhan tinggi badan dan berat badan antara balita Normal, Stunted, dan Severely Stunted usia 0–24 bulan?

---

## 📌 Catatan

- Dataset tidak mengandung variabel sosial-ekonomi langsung (pendapatan, pendidikan orang tua, dll), sehingga **Growth Composite Index (GCI)** digunakan sebagai proxy kondisi pertumbuhan berdasarkan kombinasi z-score antropometri WHO
- Semua z-score dihitung menggunakan tabel referensi **WHO Child Growth Standards** dengan median dan SD per usia dan jenis kelamin
- Dashboard dibuat menggunakan **Streamlit** dan **Matplotlib/Seaborn** (bukan Plotly) agar lebih ringan