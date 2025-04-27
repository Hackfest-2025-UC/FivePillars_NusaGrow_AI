# API Pencocokan Investor

## Deskripsi

Kode ini adalah API berbasis Flask yang berfungsi untuk membantu mencocokkan deskripsi supplier dengan daftar deskripsi investor menggunakan model *sentence embedding*. Tujuannya adalah untuk menemukan investor yang paling relevan berdasarkan tingkat kemiripan teks.

## Alur Kerja

1. **Inisialisasi Aplikasi**  
   Menggunakan `Flask` untuk membangun server web sederhana.

2. **Load Model**  
   Menggunakan `SentenceTransformer` dengan model `'all-MiniLM-L6-v2'` untuk mengubah teks menjadi representasi vektor.

3. **Endpoint `/cari-investor`**  
   - Metode: `POST`
   - Input: JSON dengan dua field:
     - `deskripsi_supplier`: Deskripsi dari supplier
     - `deskripsi_investor_list`: List berisi beberapa deskripsi investor
   - Proses:
     - Deskripsi supplier dan semua deskripsi investor diubah menjadi vektor embedding.
     - Menghitung kesamaan kosinus (*cosine similarity*) antara supplier dan setiap investor.
     - Menentukan investor dengan nilai kesamaan tertinggi.
   - Output: JSON berisi deskripsi investor terbaik dan nilai similarity-nya.

4. **Menjalankan Server**  
   API akan berjalan secara lokal dengan mode `debug=True` untuk keperluan pengembangan.

## Cara Menggunakan

- Lakukan request `POST` ke endpoint `/cari-investor`.
- Format body request (JSON):

```json
{
  "deskripsi_supplier": "Supplier ini fokus pada bahan baku pertanian organik.",
  "deskripsi_investor_list": [
    "Investor A fokus pada pertanian organik.",
    "Investor B fokus pada teknologi keuangan.",
    "Investor C fokus pada industri kreatif."
  ]
}
```

- Contoh response yang dikembalikan:

```json
{
  "investor_cocok": "Investor A fokus pada pertanian organik.",
  "similarity_score": 0.87
}
```

## Dependensi

Pastikan telah menginstal library berikut:

- Flask
- sentence-transformers
- torch

Instalasi dapat dilakukan dengan perintah:

```bash
pip install flask sentence-transformers torch
```

## Catatan Tambahan

- Model `all-MiniLM-L6-v2` adalah model ringan dan cepat, cocok untuk kasus perbandingan teks dengan performa yang efisien.
- Nilai `similarity_score` berkisar antara -1 hingga 1. Semakin mendekati 1, maka semakin mirip teks tersebut.
- Untuk penggunaan di produksi, disarankan untuk menonaktifkan mode `debug`.

---

Kalau kamu mau sekalian aku buatkan README untuk penggunaan dengan *Postman* atau contoh curl command juga, beritahu saja. Mau sekalian?
