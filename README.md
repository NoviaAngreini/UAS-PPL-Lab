# UAS Praktikum Proyek Perangkat Lunak

Nama: Novia Angreini 

NPM: 2208107010068

# Struktur Fodler
```
toko/
│
├── manage.py
│
├── toko/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── produk/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── daftar_konser.html
│   │   ├── detail_konser.html
│   │   ├── kontak.html
│   │   ├── list.html
│   │   └── form.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── db.sqlite3
```

# Fitur Utama
Fitur User (Publik)
1. Halaman Home
   - Menampilkan informasi aplikasi penjualan tiket konser.
   - Menampilkan daftar konser yang tersedia.
2. Halaman Daftar Konser
   - Menampilkan seluruh konser yang tersedia.
   - Menampilkan nama konser, artis, lokasi, tanggal, dan harga tiket.
3. Halaman Detail Konser
   - Menampilkan informasi lengkap konser.
   - Menampilkan status tiket tersedia atau sold out.
4. Halaman Kontak
   - Menampilkan informasi kontak penyelenggara.

# Fitur Admin
- Login Admin Django
- Tambah Data Konser
- Melihat Data Konser
- Mengubah Data Konser
- Menghapus Data Konser

(CRUD: Create, Read, Update, Delete)

# Teknologi
Aplikasi Concert Ticket Hub dikembangkan menggunakan beberapa teknologi utama, yaitu:
- Python
- HTML dan CSS

# Framework yang Digunakan
Django Framework

Django merupakan framework web berbasis Python yang digunakan untuk mempercepat proses pengembangan aplikasi. Django menyediakan berbagai fitur bawaan seperti sistem routing URL, manajemen database, autentikasi pengguna, serta panel administrasi (Admin Dashboard).

# Arsitektur Sistem
Aplikasi ini menggunakan arsitektur MVT (Model-View-Template) yang merupakan pola arsitektur bawaan Django.

# Database yang Digunakan
Aplikasi menggunakan SQLite3 sebagai sistem manajemen database. SQLite merupakan database bawaan Django yang ringan, mudah digunakan, dan tidak memerlukan instalasi server database tambahan.
Database SQLite digunakan untuk menyimpan:
- Data konser
- Informasi tiket
- Data pengguna/admin
- Data autentikasi sistem
