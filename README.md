# PRAKTIKUM_PERTEMUAN_9

A. ALGORITMA PROGRAM

1. Mulai Program:

>Siapkan tempat (list) untuk menyimpan data mahasiswa.

2. Proses Input Data:

Tampilkan pertanyaan untuk memasukkan:
>Nama mahasiswa.
>NIM mahasiswa.
>Nilai Tugas, UTS, dan UAS.

Hitung nilai akhir mahasiswa dengan rumus:
>Nilai Akhir = (Tugas * 30%) + (UTS * 35%) + (UAS * 35%)

Simpan semua data (Nama, NIM, Tugas, UTS, UAS, Nilai Akhir) ke dalam daftar.

3. Tanya kepada pengguna:

Tanyakan apakah ingin menambahkan data mahasiswa lagi:
>Jika "Ya", ulangi langkah Proses Input Data.
>Jika "Tidak", lanjutkan ke langkah berikutnya.

4. Tampilkan Data:
   
>Cetak semua data mahasiswa dalam bentuk tabel:
Kolom: Nama, NIM, Tugas, UTS, UAS, dan Nilai Akhir.

6. Akhiri Program:
   
>Tampilkan pesan selesai, dan program berakhir.

#

B. FLOWCHART

![image](https://github.com/user-attachments/assets/a5ff6a4f-77c3-4095-8407-223958ec6004)

#

C. CODE PROGRAM DAN PENJELASAN

![image](https://github.com/user-attachments/assets/a887081c-d15c-49f6-9eec-e5fad3ad5cf9)


PENJELASAN :

1. Fungsi untuk Menghitung Nilai Akhir

![image](https://github.com/user-attachments/assets/6d2ce4bf-b172-47a9-bf22-2addc25e746d)

Fungsi: Menghitung nilai akhir berdasarkan bobot:
Tugas: 30%.
UTS: 35%.
UAS: 35%.

2. List untuk Menyimpan Data

![image](https://github.com/user-attachments/assets/cd58aefe-a753-4861-a50d-e9747c5aca6e)

List Kosong: Tempat menyimpan data mahasiswa dalam bentuk dictionary

3. Perulangan untuk Input Data

![image](https://github.com/user-attachments/assets/6fa581e4-e850-4eed-b757-7e7f68670131)

while True: Perulangan berjalan terus sampai pengguna memutuskan berhenti.

Input Nama dan NIM: Pengguna memasukkan nama dan NIM sebagai string.

Input Nilai: Nilai tugas, UTS, dan UAS dimasukkan sebagai angka desimal (float).

4. Hitung Nilai Akhir dan Simpan Data

![image](https://github.com/user-attachments/assets/ce567aa2-1fb4-474f-95c5-88a795495c23)

Hitung Nilai Akhir: Fungsi hitung_nilai_akhir dipanggil untuk menghitung nilai akhir.

Simpan Data: Data nama, NIM, nilai tugas, UTS, UAS, dan nilai akhir dimasukkan ke dalam list data_mahasiswa sebagai dictionary

5. Tanya Pengguna Untuk Menambahkan Data

![image](https://github.com/user-attachments/assets/cc544768-9acd-497b-833d-8709f3436831)

Input Pilihan: Pengguna diminta memilih apakah ingin menambah data lagi.

>"y": Ulangi perulangan.

>"t": Keluar dari perulangan dengan perintah break.

6. Header Tabel

![image](https://github.com/user-attachments/assets/d2f05424-e4f9-478e-ad6b-7b2a08e901f3)

Header Tabel:

>Menampilkan kolom No, Nama, NIM, Tugas, UTS, UAS, dan Nilai Akhir.

>Garis horizontal menggunakan karakter "=" sepanjang 95 karakter.

7. Tampilkan Total Data Mahasiswa 

![image](https://github.com/user-attachments/assets/a8afb68a-c267-4c7f-bac2-c732d11ed244)

Enumerasi: Menggunakan enumerate untuk memberikan nomor urut (dimulai dari 1).

Format Output:

>No: Nomor urut.

>Nama: Rata kiri dengan lebar 20 karakter.

>NIM: Rata kiri dengan lebar 15 karakter.

>Nilai: Ditampilkan dengan 2 angka desimal.

#

D. HASIL RUN CODE

![image](https://github.com/user-attachments/assets/a9a84190-1659-4513-8d2a-da86ade92e07)


