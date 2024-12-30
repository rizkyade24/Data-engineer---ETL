## Design Datamart
link: https://drive.google.com/file/d/1g_PkzG_xIb1B7gGzv5HyEyem0kU_0aah/view?usp=sharing

![Dashboard2 drawio](https://github.com/user-attachments/assets/3b24f296-d96c-429f-984c-2ee56b7352d4)

## 1. Tabel Fakta: fact_stock
Tabel fact_stock adalah tabel fakta yang menyimpan data kuantitatif terkait stok material yang tersedia. Tabel ini menghubungkan berbagai dimensi dan menyimpan informasi seperti jumlah stok dan status material pada waktu tertentu.

Kolom:

- fact_stock_id: ID unik untuk setiap entri dalam tabel stok.
- material_id: ID material yang terkait dengan stok. Menghubungkan ke tabel dim_material untuk mendapatkan informasi lebih lanjut mengenai material.
- entity_id: ID entitas yang menyimpan stok material, menghubungkan ke tabel dim_entity.
- batch_id: ID batch material, menghubungkan ke tabel dim_batch untuk informasi lebih lanjut tentang batch tersebut.
- date_id: ID tanggal yang terkait dengan stok, menghubungkan ke tabel dim_date untuk mengetahui kapan stok tersebut tercatat.
- province_id: ID provinsi tempat stok material berada, menghubungkan ke tabel dim_location untuk informasi geografis.
- regency_id: ID kabupaten/kota tempat stok material berada, menghubungkan ke tabel dim_location.
- qty: Jumlah stok yang tersedia dari material di lokasi dan waktu tertentu.
- status: Status dari stok (misalnya, apakah stok tersebut tersedia, sudah kadaluarsa, atau dalam kondisi tertentu lainnya).
- Fungsi: Tabel fact_stock digunakan untuk analisis jumlah stok yang tersedia berdasarkan berbagai dimensi (material, entitas, lokasi, waktu). Ini memungkinkan untuk mengukur dan melacak stok berdasarkan waktu, lokasi geografis, dan material.

## 2. Tabel Dimensi: dim_material
Tabel dim_material berisi informasi tentang material yang disimpan di sistem. Setiap material bisa berupa vaksin atau material non-vaksin, dan informasi lainnya seperti jenis distribusi dan status suhu.

Kolom:

- material_id: ID unik untuk setiap material.
- material_name: Nama material (misalnya, PCV, masker, dll.).
- unit_of_distribution: Satuan distribusi material (misalnya, box, pack, vial).
- pieces_per_unit: Jumlah potongan per unit distribusi.
- temperature_sensitive: Menunjukkan apakah material tersebut sensitif terhadap suhu (misalnya, vaksin biasanya memiliki suhu tertentu).
- temperature_min: Suhu minimum yang dibutuhkan untuk material yang sensitif terhadap suhu.
- temperature_max: Suhu maksimum yang dibutuhkan untuk material yang sensitif terhadap suhu.
- is_vaccine: Menandakan apakah material tersebut adalah vaksin (boolean: 0 untuk non-vaksin, 1 untuk vaksin).
- bpom_code: Kode BPOM (jika material tersebut adalah vaksin yang disetujui oleh BPOM).
- description: Deskripsi tambahan tentang material.
Fungsi: Tabel ini digunakan untuk memberikan informasi rinci tentang material yang ada, termasuk unit distribusi, sensitivitas suhu, dan kategori vaksin atau non-vaksin. Ini memungkinkan untuk analisis distribusi stok berdasarkan jenis material.

## 3. Tabel Dimensi: dim_batch
Tabel dim_batch menyimpan informasi tentang batch material, seperti tanggal produksi dan kadaluarsa serta status batch material.

Kolom:

- batch_id: ID unik untuk setiap batch material.
- expiry_date: Tanggal kedaluwarsa material dalam batch tersebut.
- production_date: Tanggal produksi material dalam batch tersebut.
- manufacture_date: Tanggal pembuatan batch material.
- status: Status batch material (misalnya, aktif, kadaluarsa, atau lainnya).
Fungsi: Tabel ini memberikan informasi tentang status dan tanggal penting terkait batch material, yang dapat digunakan untuk memantau kualitas dan ketahanan material selama distribusi dan penyimpanan.

## 4. Tabel Dimensi: dim_location
Tabel dim_location menyimpan informasi geografis tentang lokasi, termasuk provinsi dan kabupaten.

Kolom:

- location_id: ID unik untuk setiap lokasi.
- province_id: ID provinsi tempat lokasi tersebut berada, menghubungkan ke tabel dim_location untuk provinsi.
- regency_id: ID kabupaten/kota tempat lokasi tersebut berada, menghubungkan ke tabel dim_location untuk kabupaten/kota.
- lat: Koordinat lintang lokasi (dalam derajat).
- lng: Koordinat bujur lokasi (dalam derajat).
Fungsi: Tabel ini digunakan untuk analisis geografis dan visualisasi data stok berdasarkan provinsi, kabupaten, dan lokasi spesifik. Lokasi digunakan untuk melacak distribusi material di berbagai wilayah Indonesia.

## 5. Tabel Dimensi: dim_date
Tabel dim_date berisi informasi tentang tanggal yang digunakan dalam data stok, memberikan detail seperti tahun, bulan, dan hari.

Kolom:

- date_id: ID unik untuk setiap tanggal.
- date: Tanggal dalam format standar (YYYY-MM-DD).
- year: Tahun dari tanggal tersebut.
- month: Bulan dari tanggal tersebut.
- day: Hari dari tanggal tersebut.
Fungsi: Tabel ini memudahkan analisis stok berdasarkan waktu, memungkinkan untuk melacak perubahan stok berdasarkan bulan, tahun, atau hari tertentu. Ini juga berguna untuk melihat tren stok material dari waktu ke waktu.

## 6. Tabel Dimensi: dim_entity
Tabel dim_entity menyimpan data tentang entitas yang memiliki stok material, seperti fasilitas kesehatan atau lembaga yang terlibat dalam distribusi material.

Kolom:

- entity_id: ID unik untuk setiap entitas.
- entity_name: Nama entitas (misalnya, Puskesmas, Rumah Sakit, Dinas Kesehatan).
- entity_type: Jenis entitas (misalnya, Puskesmas, Rumah Sakit, dll.).
- address: Alamat entitas.
- province_id: ID provinsi tempat entitas tersebut berada.
- regency_id: ID kabupaten/kota tempat entitas tersebut berada.
- status: Status entitas (misalnya, aktif atau tidak aktif).
Fungsi: Tabel ini memberikan detail tentang entitas yang menyimpan stok material, dan memungkinkan untuk analisis distribusi stok berdasarkan jenis dan lokasi entitas.

Kesimpulan
Tabel-tabel ini berfungsi untuk menyusun data dalam bentuk yang dapat digunakan untuk analisis stok material. Data ini disusun berdasarkan berbagai dimensi, seperti material, lokasi, waktu, dan entitas, yang memungkinkan pembuatan dashboard yang dapat menyajikan informasi yang komprehensif mengenai stok material yang tersedia, status batch, dan distribusi geografis.
