# Mengapa PBO Diperlukan pada Sistem Penyewaan Alat Pertanian UPJA

## 1. Gambaran Pencatatan Saat Ini

UPJA (Usaha Pelayanan Jasa Alsintan) menyediakan layanan penyewaan alat dan mesin pertanian kepada petani. Dalam kegiatan operasionalnya, pengelola perlu mendata alat pertanian yang tersedia, mencatat identitas penyewa, serta mengelola informasi petugas yang melayani proses penyewaan.

Jika pendataan masih dilakukan secara manual, informasi mengenai alat, penyewa, dan petugas dapat tersebar di beberapa catatan. Hal ini dapat menyulitkan pengelola ketika mencari data atau memeriksa informasi penyewaan.

## 2. Persoalan yang Timbul

Beberapa persoalan yang dapat terjadi dalam pengelolaan penyewaan alat pertanian adalah:

1. **Data Alat Pertanian Sulit Dikelola**  
   Pengelola perlu mencatat kode, nama, dan tarif harian setiap alat. Kesalahan pencatatan tarif dapat menyebabkan perhitungan biaya sewa menjadi tidak tepat.

2. **Data Penyewa Perlu Disimpan dengan Terstruktur**  
   Identitas penyewa seperti nama, NIK, dan alamat perlu dicatat agar mudah ditemukan kembali ketika diperlukan.

3. **Informasi Petugas Perlu Dikelola**  
   Data petugas, termasuk nama dan nomor telepon, perlu disimpan agar pengelola dapat mengetahui petugas yang bertanggung jawab dalam pelayanan.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)

Dengan menerapkan konsep Pemrograman Berorientasi Objek (PBO), data dan fungsi dalam sistem penyewaan alat pertanian dapat dikelompokkan berdasarkan objeknya.

- **Manajemen Alat Pertanian melalui Kelas `AlatTani`**  
  Kelas ini menyimpan atribut kode, nama, dan tarif harian alat. Method seperti `biaya_sewa()` digunakan untuk menghitung biaya berdasarkan jumlah hari penyewaan. Validasi tarif juga membantu mencegah penggunaan tarif di luar batas yang ditentukan.

- **Pengelolaan Data Penyewa melalui Kelas `Penyewa`**  
  Kelas ini digunakan untuk menyimpan informasi identitas penyewa, seperti nama, NIK, dan alamat. Dengan demikian, data penyewa dapat dikelola secara lebih terstruktur.

- **Pengelolaan Data Petugas melalui Kelas `Petugas`**  
  Kelas ini menyimpan informasi petugas, seperti nama dan nomor telepon. Data tersebut dapat digunakan untuk mendukung kebutuhan pelayanan penyewaan alat.

Melalui pendekatan PBO, setiap bagian sistem memiliki tanggung jawab yang lebih jelas. Data alat, penyewa, dan petugas dapat dikelola melalui kelas masing-masing sehingga program menjadi lebih terstruktur, mudah dipahami, dan lebih mudah dikembangkan.