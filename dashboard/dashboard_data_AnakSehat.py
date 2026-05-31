import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Dashboard AnakSehat AI",
    page_icon="📈",
    layout="wide"
)
st.title("Dashboard AnakSehat AI")
st.caption("Analisis Interaktif Stunting Balita Usia 0–24 Bulan")

# load data
df = pd.read_csv("dashboard/data/data_final_AnakSehat.csv")

# menampilkan preview data
st.subheader("Preview Dataset")
st.write("Jumlah data:", len(df))
st.dataframe(df.head(10))

st.divider()

# membuat kelompok usia 
df['kelompok_usia'] = pd.cut(
    df['umur_bulan'],
    bins=[0, 6, 12, 18, 24],
    labels=['0-6', '7-12', '13-18', '19-24'],
    include_lowest=True
)

# sidebar untuk filter
st.sidebar.header("Filter")

pilih_gender = st.sidebar.multiselect(
    "Pilih Jenis Kelamin",
    options=df['jenis_kelamin'].unique(),
    default=df['jenis_kelamin'].unique()
)

pilih_stunting = st.sidebar.multiselect(
    "Pilih Status Stunting",
    options=df['stunting'].unique(),
    default=df['stunting'].unique()
)

pilih_usia = st.sidebar.multiselect(
    "Pilih Kelompok Usia",
    options=['0-6', '7-12', '13-18', '19-24'],
    default=['0-6', '7-12', '13-18', '19-24']
)

# Menfilter data
df_filter = df[
    (df['jenis_kelamin'].isin(pilih_gender)) &
    (df['stunting'].isin(pilih_stunting)) &
    (df['kelompok_usia'].isin(pilih_usia))
]

st.write("Data setelah difilter:", len(df_filter), "baris")

st.divider()

# =============================================
# PERTANYAAN 1
# =============================================
st.subheader("Pertanyaan 1 - Stunting berdasarkan Usia dan Jenis Kelamin")
st.write("Pada kelompok usia serta jenis kelamin manakah yang memiliki presentase stunting tertinggi ditemukan pada balita dalam rentang usia 0 sampai 24 bulan?")

# pilihan chart
tipe_chart = st.radio("Mau lihat chart apa?", ["Stacked Bar", "Grouped Bar"], horizontal=True)

# membuat crosstab 
ct = pd.crosstab(
    [df_filter['kelompok_usia'], df_filter['jenis_kelamin']],
    df_filter['stunting'],
    normalize='index'
) * 100

ct = ct.reset_index()
ct['label'] = ct['kelompok_usia'].astype(str) + " - " + ct['jenis_kelamin']

kolom_status = [k for k in ['Normal', 'Stunted', 'Severely Stunted', 'Tall'] if k in ct.columns]

fig1, ax1 = plt.subplots(figsize=(10, 5))

if tipe_chart == "Stacked Bar":
    ct.set_index('label')[kolom_status].plot(kind='bar', stacked=True, ax=ax1)
else:
    ct.set_index('label')[kolom_status].plot(kind='bar', stacked=False, ax=ax1)

ax1.set_title("Persentase Stunting per Kelompok Usia dan Jenis Kelamin")
ax1.set_xlabel("Kelompok Usia - Jenis Kelamin")
ax1.set_ylabel("Persentase (%)")
ax1.legend(loc='upper right')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
st.pyplot(fig1)

st.info("Insight: Kelompok usia 19-24 bulan memiliki tingkat stunting tertinggi dibandingkan kelompok usia lainnya. Hal ini menunjukkan bahwa pada rentang usia tersebut, balita lebih rentan mengalami gangguan pertumbuhan sehingga memerlukan perhatian dan pemantauan gizi yang lebih baik.")

st.divider()

# =============================================
# PERTANYAAN 2
# =============================================
st.subheader("Pertanyaan 2 - Karakteristik Balita per Kategori Stunting")
st.write("Bagaimana distribusi dan karakteristik tinggi badan, berat badan, usia, serta jenis kelamin pada masing-masing kategori status stunting balita usia 0–24 bulan?")

pilih_variabel = st.selectbox(
    "Pilih variabel yang ingin dilihat",
    ["tinggi_cm", "berat_kg", "umur_bulan", "waz_zscore", "bmi"]
)

pilih_chart2 = st.radio("Pilih tipe chart", ["Box Plot", "Violin Plot", "Histogram"], horizontal=True)

pisah_gender = st.checkbox("Pisahkan per jenis kelamin?")

fig2, ax2 = plt.subplots(figsize=(10, 5))

urutan = ['Severely Stunted', 'Stunted', 'Normal', 'Tall']
urutan_ada = [u for u in urutan if u in df_filter['stunting'].unique()]

if pilih_chart2 == "Box Plot":
    if pisah_gender:
        sns.boxplot(data=df_filter, x='stunting', y=pilih_variabel, hue='jenis_kelamin', order=urutan_ada, ax=ax2)
    else:
        sns.boxplot(data=df_filter, x='stunting', y=pilih_variabel, order=urutan_ada, ax=ax2)

elif pilih_chart2 == "Violin Plot":
    if pisah_gender:
        sns.violinplot(data=df_filter, x='stunting', y=pilih_variabel, hue='jenis_kelamin', order=urutan_ada, ax=ax2)
    else:
        sns.violinplot(data=df_filter, x='stunting', y=pilih_variabel, order=urutan_ada, ax=ax2)

else:
    for status in urutan_ada:
        data_status = df_filter[df_filter['stunting'] == status][pilih_variabel]
        ax2.hist(data_status, alpha=0.5, label=status, bins=30)
    ax2.legend()

ax2.set_title(f"Distribusi {pilih_variabel} per Status Stunting")
ax2.set_xlabel("Status Stunting")
ax2.set_ylabel(pilih_variabel)
plt.xticks(rotation=15)
plt.tight_layout()
st.pyplot(fig2)

# tabel rata-rata
st.write("Rata-rata per kategori:")
rata2 = df_filter.groupby('stunting')[[
    'tinggi_cm',
    'berat_kg',
    'umur_bulan',
    'waz_zscore',
    'bmi',
    'baz_zscore'
]].mean().round(2)
st.dataframe(rata2)

st.info("Insight: Balita dengan kategori severely stunted memiliki rata-rata tinggi badan paling rendah dibandingkan dengan kategori lainny dan terlihat jauh berada di bawah balita dengan pertumbuhan normal. Kondisi ini menunjukkan adanya gangguan pertumbuhan yang cukup serius pada balita tersebut.")

st.divider()

# =============================================
# PERTANYAAN 3
# =============================================
st.subheader("Pertanyaan 3 - Jumlah Kasus Stunting")
st.write("Bagaimana distribusi jumlah kasus stunting pada setiap kelompok usia dan jenis kelamin balita usia 0–24 bulan dalam dataset AnakSehat AI?")

tampilkan = st.radio("Tampilkan berdasarkan", ["Kelompok Usia", "Jenis Kelamin"], horizontal=True)

persen_atau_jumlah = st.checkbox("Tampilkan dalam persen?")

if tampilkan == "Kelompok Usia":
    kolom_x = "kelompok_usia"
else:
    kolom_x = "jenis_kelamin"

if persen_atau_jumlah:
    tabel3 = pd.crosstab(df_filter[kolom_x], df_filter['stunting'], normalize='index') * 100
    label_y = "Persentase (%)"
else:
    tabel3 = pd.crosstab(df_filter[kolom_x], df_filter['stunting'])
    label_y = "Jumlah"

fig3, ax3 = plt.subplots(figsize=(9, 5))
tabel3.plot(kind='bar', ax=ax3)
ax3.set_title(f"Distribusi Stunting per {tampilkan}")
ax3.set_xlabel(tampilkan)
ax3.set_ylabel(label_y)
ax3.legend(loc='upper right')
plt.xticks(rotation=15)
plt.tight_layout()
st.pyplot(fig3)

st.info("Insight: Jumlah kasus stunting paling banyak ditemukan pada kelompok usia 13-24 bulan. Selain itu, distribusi kasus antara balita laki-laki dan perempuan terlihat hampir seimbang, sehingga stuntin dapat terjadi pada kedua jenis kelamin dengan tingkat yang relatif sama.")

st.divider()

# =============================================
# PERTANYAAN 4
# =============================================
st.subheader("Pertanyaan 4 - Hubungan antar Variabel")
st.write("Bagaimana hubungan antara tinggi badan, berat badan, dan usia terhadap kategori status stunting balita berdasarkan hasil visualisasi data pada dataset AnakSehat AI?")

col1, col2 = st.columns(2)
with col1:
    sumbu_x = st.selectbox("pilih sumbu X",[
    "tinggi_cm",
    "berat_kg",
    "umur_bulan",
    "waz_zscore",
    "bmi",
    "baz_zscore",
    "weight_height_ratio"
], index=0)
with col2:
    sumbu_y = st.selectbox("pilih sumbu Y",[
    "tinggi_cm",
    "berat_kg",
    "umur_bulan",
    "waz_zscore",
    "bmi",
    "baz_zscore",
    "weight_height_ratio"
], index=1)

jumlah_sampel = st.slider("jumlah data yang ditampilkan", 500, 5000, 2000, 500)

pisah_gender2 = st.checkbox("pisah warna per jenis kelamin juga?")

# ambil sampel
df_sampel = df_filter.sample(min(jumlah_sampel, len(df_filter)), random_state=42)

fig4, ax4 = plt.subplots(figsize=(10, 6))

warna_stunting = {
    'Normal': 'green',
    'Stunted': 'orange',
    'Severely Stunted': 'red',
    'Tall': 'blue'
}

if pisah_gender2:
    for gender in df_sampel['jenis_kelamin'].unique():
        for status in df_sampel['stunting'].unique():
            subset = df_sampel[(df_sampel['jenis_kelamin'] == gender) & (df_sampel['stunting'] == status)]
            marker = 'o' if gender == 'Laki-laki' else '^'
            ax4.scatter(subset[sumbu_x], subset[sumbu_y],
                       c=warna_stunting.get(status, 'gray'),
                       marker=marker, alpha=0.4, s=20,
                       label=f"{status} - {gender}")
else:
    for status in df_sampel['stunting'].unique():
        subset = df_sampel[df_sampel['stunting'] == status]
        ax4.scatter(subset[sumbu_x], subset[sumbu_y],
                   c=warna_stunting.get(status, 'gray'),
                   alpha=0.4, s=20, label=status)

ax4.set_xlabel(sumbu_x)
ax4.set_ylabel(sumbu_y)
ax4.set_title(f"Scatter Plot: {sumbu_x} vs {sumbu_y}")
ax4.legend(loc='upper left', fontsize=7, markerscale=2)
plt.tight_layout()
st.pyplot(fig4)

st.info("Insight: Balita dengan kategori severely stunted membentuk kelompok pada bagian kiri bawah, yang menunjukkan bahwa balita tersebut memiliki tinggi badan dan berat badan yang sama-sama rendah dibandingkan kategori lainnya.")

st.divider()

# =============================================
# PERTANYAAN 5
# =============================================
st.subheader("Pertanyaan 5 - Pola Pertumbuhan")
st.write("Bagaimana perbedaan pola pertumbuhan tinggi badan dan berat badan antara balita normal, stunted, dan severely stunted usia 0–24 bulan berdasarkan dataset AnakSehat AI?")

pilih_var5 = st.selectbox(
    "Variabel yang ingin dilihat polanya",
    [
    "tinggi_cm",
    "berat_kg",
    "waz_zscore",
    "bmi",
    "baz_zscore",
    "weight_height_ratio"
]
)

pilih_status5 = st.multiselect(
    "Pilih kategori yang ingin ditampilkan",
    options=['Severely Stunted', 'Stunted', 'Normal', 'Tall'],
    default=['Severely Stunted', 'Stunted', 'Normal']
)

pilih_gender5 = st.radio("filter gender", ["Semua", "Laki-laki", "Perempuan"], horizontal=True)

tampilkan_ci = st.checkbox("tampilkan rentang datanya (CI)?", value=True)

# filter
df5 = df_filter[df_filter['stunting'].isin(pilih_status5)].copy()
if pilih_gender5 != "Semua":
    df5 = df5[df5['jenis_kelamin'] == pilih_gender5]

# hitung rata-rata per bulan
pola = df5.groupby(['umur_bulan', 'stunting'])[pilih_var5].agg(['mean', 'std']).reset_index()
pola.columns = ['umur_bulan', 'stunting', 'rata2', 'std']

fig5, ax5 = plt.subplots(figsize=(11, 5))

warna5 = {
    'Normal': 'green',
    'Stunted': 'orange',
    'Severely Stunted': 'red',
    'Tall': 'blue'
}

for status in pilih_status5:
    data_status = pola[pola['stunting'] == status].sort_values('umur_bulan')
    if data_status.empty:
        continue
    warna = warna5.get(status, 'gray')
    ax5.plot(data_status['umur_bulan'], data_status['rata2'],
             label=status, color=warna, linewidth=2, marker='o', markersize=3)
    if tampilkan_ci:
        ax5.fill_between(
            data_status['umur_bulan'],
            data_status['rata2'] - data_status['std'],
            data_status['rata2'] + data_status['std'],
            alpha=0.15, color=warna
        )

ax5.set_title(f"Pola Pertumbuhan {pilih_var5} per Kategori Stunting")
ax5.set_xlabel("Umur (bulan)")
ax5.set_ylabel(pilih_var5)
ax5.legend()
ax5.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig5)

st.info("Insight: Semakin bertambah usia balita, perbedaan antara anak dengan pertumbuhan normal dan anak yang terkena stunting terlihat semakin jelas. Hal ini menunjukkan bahwa stuntin terjadi sevara bertahap dari waktu ke waktu dan akan semakin sulit diperbaiki jika penanganannya terlambat.")

st.divider()

# =============================================
# KESIMPULAN
# =============================================
st.subheader("Kesimpulan")
st.write("ini rangkuman dari semua yang telah dianalisis")

total_data   = len(df_filter)
jml_normal   = len(df_filter[df_filter['stunting'] == 'Normal'])
jml_stunted  = len(df_filter[df_filter['stunting'] == 'Stunted'])
jml_severe   = len(df_filter[df_filter['stunting'] == 'Severely Stunted'])
jml_tall     = len(df_filter[df_filter['stunting'] == 'Tall'])
pct_stunting = (jml_stunted + jml_severe) / total_data * 100 if total_data > 0 else 0

col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("Normal",           f"{jml_normal:,}")
col_b.metric("Stunted",          f"{jml_stunted:,}")
col_c.metric("Severely Stunted", f"{jml_severe:,}")
col_d.metric("Tall",             f"{jml_tall:,}")

st.write(f"total balita yang terkena stunting (stunted + severely stunted): **{jml_stunted + jml_severe:,} balita ({pct_stunting:.1f}%)**")

st.success("""
**Kesimpulan dari analisis:**

1. Kasus stunting paling banyak ditemukan pada kelompok usia 13-24 bulan. Hal ini menunjukkan bahwa intervensi gizi dan pemantauan pertumbuhan perlu dilakukan sedini mungkin, terutama sebelum anak memasuki usia 12 bulan.

2. Berdasarkan hasil analisis, tidak ditemukan perbedaan yang signifikan antara balita laki-laki dan perempuan dalam jumlah kasus stunting. Kondisi ini menunjukkan bahwa stunting dapat terjadi pada kedua jenis kelamin dengan tingkat yang relatif sama. Karena tubuh manusia ternyata cukup adil saat membagikan masalah kesehatan. Tragis, tapi konsisten.

3. Balita yang mengalami stunting memiliki tinggi badan dan berat badan yang lebih rendah dibandingkan balita dengan pertumbuhan normal. Kondisi tersebut juga tercermin pada nilai WAZ dan BAZ yang menunjukkan perbedaan kondisi pertumbuhan antar kategori stunting.

4. Selain itu, pola pertumbuhan menunjukkan bahwa perbedaan antara balita normal dan balita stunting semakin terlihat seiring bertambahnya usia. Hal ini menandakan bahwa penanganan yang dilakukan lebih awal akan memberikan hasil yang lebih baik dalam mencegah maupun mengurangi risiko stunting.
""")