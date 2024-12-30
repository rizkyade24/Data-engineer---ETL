# Design Datamart
link: https://drive.google.com/file/d/1g_PkzG_xIb1B7gGzv5HyEyem0kU_0aah/view?usp=sharing

![Dashboard2 drawio](https://github.com/user-attachments/assets/873f1164-7bbf-4254-966a-34ab7d05aa8d)


## 1. Tabel Fakta: fact_stock
Tabel fact_stock adalah tabel fakta yang menyimpan data kuantitatif terkait stok material yang tersedia. Tabel ini menghubungkan berbagai dimensi dan menyimpan informasi seperti jumlah stok dan status material pada waktu tertentu.

Kolom:

- fact_stock_id
- material_id
- entity_id
- batch_id
- date_id
- province_id
- regency_id
- qty
- status
- Fungsi: Tabel fact_stock digunakan untuk analisis jumlah stok yang tersedia berdasarkan berbagai dimensi (material, entitas, lokasi, waktu). Ini memungkinkan untuk mengukur dan melacak stok berdasarkan waktu, lokasi geografis, dan material.

## 2. Tabel Dimensi: dim_material
Tabel dim_material berisi informasi tentang material yang disimpan di sistem. Setiap material bisa berupa vaksin atau material non-vaksin, dan informasi lainnya seperti jenis distribusi dan status suhu.

Kolom:

- material_id: ID unik untuk setiap material.
- material_name: Nama material (misalnya, PCV, masker, dll.).
- unit_of_distribution
- pieces_per_unit
- temperature_sensitive
- temperature_min
- temperature_max
- is_vaccine
- bpom_code
- description
Fungsi: Tabel ini digunakan untuk memberikan informasi rinci tentang material yang ada, termasuk unit distribusi, sensitivitas suhu, dan kategori vaksin atau non-vaksin. Ini memungkinkan untuk analisis distribusi stok berdasarkan jenis material.

## 3. Tabel Dimensi: dim_batch
Tabel dim_batch menyimpan informasi tentang batch material, seperti tanggal produksi dan kadaluarsa serta status batch material.

Kolom:

- batch_id: ID unik untuk setiap batch material.
- expiry_date
- production_date
- manufacture_date
- status
Fungsi: Tabel ini memberikan informasi tentang status dan tanggal penting terkait batch material, yang dapat digunakan untuk memantau kualitas dan ketahanan material selama distribusi dan penyimpanan.

## 4. Tabel Dimensi: dim_location
Tabel dim_location menyimpan informasi geografis tentang lokasi, termasuk provinsi dan kabupaten.

Kolom:

- location_id.
- province_id
- regency_id
- lat
- lng
Fungsi: Tabel ini digunakan untuk analisis geografis dan visualisasi data stok berdasarkan provinsi, kabupaten, dan lokasi spesifik. Lokasi digunakan untuk melacak distribusi material di berbagai wilayah Indonesia.

## 5. Tabel Dimensi: dim_date
Tabel dim_date berisi informasi tentang tanggal yang digunakan dalam data stok, memberikan detail seperti tahun, bulan, dan hari.

Kolom:

- date_id
- date
- year
- month
- day
Fungsi: Tabel ini memudahkan analisis stok berdasarkan waktu, memungkinkan untuk melacak perubahan stok berdasarkan bulan, tahun, atau hari tertentu. Ini juga berguna untuk melihat tren stok material dari waktu ke waktu.

## 6. Tabel Dimensi: dim_entity
Tabel dim_entity menyimpan data tentang entitas yang memiliki stok material, seperti fasilitas kesehatan atau lembaga yang terlibat dalam distribusi material.

Kolom:

- entity_id: ID unik untuk setiap entitas.
- entity_name
- entity_type
- address:
- province_id
- regency_id
- status
Fungsi: Tabel ini memberikan detail tentang entitas yang menyimpan stok material, dan memungkinkan untuk analisis distribusi stok berdasarkan jenis dan lokasi entitas.

<br>
Tabel-tabel ini berfungsi untuk menyusun data yang dapat digunakan untuk analisis stok material. Data ini disusun dimensi, seperti material, lokasi, waktu, dan entitas, yang memungkinkan pembuatan dashboard yang menyajikan informasi mengenai stok material yang tersedia, status batch, dan distribusi geografis.
