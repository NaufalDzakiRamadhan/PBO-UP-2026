# Mengapa PBO diperlukan pada Sistem Pencatatan Depot Air Minum Isi Ulang di Bangkinang

## 1. Gambaran Pencatatan Saat Ini
Sebagian besar usaha depot air minum isi ulang skala lokal di wilayah Bangkinang saat ini masih menerapkan pencatatan manual berbasis buku saku, atau bahkan tidak mencatat transaksi harian sama sekali. Pelanggan biasanya datang langsung membawa galon sendiri, atau memesan galon melalui pesan singkat untuk diantar ke rumah maupun warung makan.

Setelah galon diisi dan dibayar tunai di tempat, uang pembayaran langsung dimasukkan ke laci kasir tanpa adanya bukti nota atau pencatatan riwayat transaksi harian yang rinci.

## 2. Persoalan yang Timbul
Cara operasional yang belum terdata secara digital ini sering memicu beberapa kendala bagi pemilik depot:

1. **Aset Galon Pinjaman Hilang dan Tidak Terpantau**
   Pemilik depot sering meminjamkan galon fisik kepada pelanggan tetap atau pemilik warung makan. Karena tidak ada catatan riwayat pinjaman yang rapi, pengelola sering lupa berapa jumlah galon yang masih berada di pihak pelanggan sehingga rawan hilang atau tidak kembali.
2. **Kesulitan Memantau Penjualan dan Stok Air Baku**
   Tanpa rekapitulasi harian, pemilik depot kesulitan mengetahui total galon yang terjual setiap harinya secara pasti. Selain itu, pengelola kesulitan memperkirakan kapan pasokan air baku di tangki penampungan utama harus diisi ulang.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)
Dengan menerapkan konsep Pemrograman Berbasis Objek (PBO), seluruh alur operasional depot air minum dapat dikelola secara lebih terstruktur:

* **Manajemen Pelanggan dan Galon via Kelas `Pelanggan` dan `Galon`**
  Data konsumen disimpan dalam kelas `Pelanggan` (atribut: `id_pelanggan`, `nama`, `alamat`, `galon_dipinjam`). Jenis produk air dimodelkan dalam kelas `Galon` (atribut: `jenis_air`, `harga_isi_ulang`). Melalui *method* seperti `tambah_pinjaman_galon()` dan `kembalikan_galon()`, jumlah galon fisik yang sedang dipinjam pelanggan dapat terpantau secara presisi.

* **Otomatisasi Transaksi & Rekap Pendapatan via Kelas `Transaksi`**
  Aktivitas penjualan galon ditampung dalam kelas `Transaksi` yang menghubungkan objek `Pelanggan` dan `Galon`. Kelas ini memiliki atribut `jumlah_galon`, `total_biaya`, dan `tipe_layanan` (Ambil Sendiri/Diantar), serta dilengkapi *method* `hitung_total_bayar()`. Setiap kali ada penjualan, sistem secara otomatis menghitung total pembayaran dan memperbarui laporan penjualan harian secara real-time.

Melalui pendekatan PBO ini, pengelolaan galon pinjaman menjadi lebih aman, pencatatan transaksi harian lebih rapi, dan pemilik depot bisa dengan mudah melihat rekap penjualan secara otomatis.