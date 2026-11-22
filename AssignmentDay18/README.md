<div align="center">

# Case Study Specialized SQL Techniques

### Terdapat 5 soal dan 2 Reflection Question yang harus dijawab

**Assignment Data Engineering DE16 · Day 18**

</div>

## Tentang Proyek

Repositori ini berisi pembahasan dan solusi SQL untuk lima soal dari HackerRank dan menjawab pertanyaan refleksi. Setiap query dilengkapi ringkasan tujuan dan konsep yang digunakan agar alur penyelesaiannya mudah diikuti.

> Fokus latihan: mengubah aturan soal menjadi query yang jelas, terstruktur, dan mudah dibaca.

## Isi Tantangan

| No. | Tantangan | Fokus SQL |
| --- | --- | --- |
| 1 | [The Report](#1-the-report) | `CASE`, `JOIN`, pengurutan bersyarat |
| 2 | [Weather Observation Station 18](#2-weather-observation-station-18) | Agregasi, fungsi matematika, pembulatan |
| 3 | [Top Competitor](#3-top-competitor) | Banyak `JOIN`, `COUNT DISTINCT`, `HAVING` |
| 4 | [Ollivanders' Inventory](#4-ollivanders-inventory) | Subquery berkorelasi, nilai minimum |
| 5 | [Contest Leaderboard](#5-contest-leaderboard) | Subquery, `MAX`, agregasi skor

## SOAL

### Soal 1: The Report

Soal meminta untuk membuat laporan dari data siswa. Laporan itu punya tiga kolom: Name, Grade, dan Marks.
Untuk membuat laporan itu, perlu mencari grade setiap siswa dari tabel Grades. Grade ditentukan berdasarkan rentang nilai. Contohnya, nilai 88 berada di rentang 80-89, jadi gradenya 9.

Setelah itu, tampilkan semua siswa dengan aturan berikut:
* Urutkan dari grade tertinggi ke terendah
* Untuk grade 8, 9, dan 10, tampilkan nama siswa. Jika gradenya sama, urutkan nama secara alfabetis
* Untuk grade di bawah 8, tampilkan NULL sebagai nama. Jika gradenya sama, urutkan berdasarkan nilai dari yang terkecil

Jadi yang diminta bukan menghitung rata - rata atau memilih siswa tertentu, tetapi membuat daftar semua siswa dengan grade mereka, lalu menyamarkan nama siswa yang gradenya dibawah 8 sesuai aturan tersebut.

Solusi Code:

![alt text](image.png)