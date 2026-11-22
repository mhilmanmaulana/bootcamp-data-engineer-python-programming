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

Penjelasan:

Setiap siswa memiliki nilai, dan tugas kita adalah menentukan gradenya dengan mencocokkan nilai tersebut ke rentang nilai pada tabel Grades. Misalnya, nilai masuk ke rentang 80-89, jadi gradenya 9. Setelah itu, urutkan siswa berdasarkan grade dari tertinggi ke terendah. Untuk siswa dengan grade 8-10, tampilkan nama mereka dan urutkan secara alfabetis jika gradenya sama. Untuk siswa dengan grade di bawah 8, tampilkan NULL sebagai nama dan urutkan berdasarkan nilai  dari yang terkecil jika gradenya sama.

Hasil:

![alt text](<image-1.png>)


### Soal 2: Weather Observation Station 18

Soal ini meminta kita menghitung jarak Manhattan antara dua titik yang dibuentuk dari koordinat di tabel STATION

Titik pertama memakai latitude terkecil dan longitude terkecil. Titik kedua memakai latitude terbesar dan longitude terbesar. Jarak Manhattan dihitung dengan menjumlahkan selisih kedua koordinat: selisih latitude ditambah selisih longitude. Hasil akhirnya diminta dibulatkan menjadi 4 angka dibelakang koma.

Jadi tugasnya adalah mencari empat nilai minimum dan maksimum dari kolom LAT_N dan LONG_W, lalu memasukkannya ke rumus jarak tersebut.

Solusi Code:

![alt text](<image-2.png>)

Penjelasan:

Query ini mencari latitude dan longitude terkecil serta terbesar, lalu menjumlahkan selisih masing -masing koordinat untuk menghitung jarak Manhattan. Fungsi ABS memastikan selisihnya positif, sedangkat ROUND(...,4) membulatkan hasil hingga empat angkat desimal. Sebelumnya kode menghasilkan 259.68590000 : nilainya sudah benar, tetapi masih menampilkan angka nol tambahan di belakang desimal. Karena itu, CAST(....AS DECIMAL(10, 4)) digunkan agar hasilnya ditampilkan dengan empat angka desimal, yaitu 259.6859

Hasil:

![alt text](<image-3.png>)

### Soal 3: Top Competitor

Soal ini meminta membuat daftar hacker_id dan nama hacker yang berhasil mendapat nilai penuh pada lebih dari satu tantangan. Nilai penuh berarti nilai submission sama dengan nilai maksimum untuk tantangan tersebut. Nilai maksismum tantangan ditentukan dari tingkat kesulitannya, jadi data dari tabel Submission, Challenges, dan Difficulty perlu dicocokkan untuk mengetahui siapa yang mendapat nilai penuh. Setelah itu, hitung jumlah tantangan berbeda yang diselesaikan setiap hacker dengan nilai penuh, lalu menampilkan hanya hacker yang jumlahnya lebih dari satu. Urutkan hasil berdasarkan jumlah tersebut dari terbanyak ke tersedikit, jika jumlahnya sama, urutkan bersarkan hacker_id dari yang terkecil

Solusi Code:

![alt text](<image-4.png>)

Penjelasan:

Query ini menggambungkan tabel Hackers, Submissions, Challanges, dan Difficulty untuk mengetahui nilai penuh dari setiap tantangan dan membandingkannya dengan nilai submission tiap hacker. Baris yang nilainya sama dengan nilai penuh akan dipilih. Setelah itu, hasil dari yang dikelompokkan perrhacker dan hanya hacker yang mendapat nilai penuh pada lebih dari satu tantangan berbeda yang ditampilkan. Terakhir, daftar diurutkan berdasarkan jumlah tantangan bernilai penuh dari terbanyak ke tersedikit, lalu berdasarlkan hacker_id dari yang terkecil jika jumlahnya sama.

Hasil:

![alt text](<image-5.png>)

### Soal 4: Ollivanders' Inventory

Soal ini meminta kita mencari tongkat yangg tidak jahat (is_evil=0) dan paling murah untuk setiap kombinasi usia dan kekuatan. Jika ada beberapa tongkat dengan usia dan kekuatan yang sama, pilih yang harga belinya (coins_needed) paling rendah. Setelah menemukan tongkat termurah untuk tiap kombinasi usia dan kekuatan, tampilkan ID tongkat, usia, harga, dan kekuatannya. Urutkan berdasarkan kekuatan dari tertinggi ke terendah. Jika kekuatannya sama, urutkan berdasarkan usia dari tertua ke termuda.

Solusi Code:

![alt text](<image-6.png>)

Penjelasan:

Menggabungkan tabel Wands dan Wands_Property agar setiap tongkat memiliki informasi usia dan statusnya. Baris dengan is_evil=0 dipilih karena hanya tongkat yang tidak jahat yang diminta. Untuk setiap tongkat, subquery mencari harga terendah dari tongkat lain yang memiliki usia dan kekuatan sama serta tidak jahat. Tongkat ditampilkan jika harganya sama dengan harga terendah tersebut. Terkahir, hasil diurutkan berdasarkan kekuatan dari tertinggi ke terendah, lalu usia dari tertua ke termuda.

Hasil:

![alt text](<image-7.png>)

### Soal 5: Contest Leaderboard

Diminta menghitung total skor setiap hacker. Jika seorang hacker mengirim beberapa submission untuk tantangan yang sama, yang dihitung hanya skor tertinggi yang ia dapatkan pada tantangan itu. Setelah menentukan skor tertinggi untuk tiap tantangan, jumlahkan skor - skor tersebut untuk setiap hacker. Tampilkan hacker_id, nama, dan total skor, tetapi jangan tampilkan hacker yang total skornya 0. Urutkan dari total skor tertinggi ke terendah, jika skornya sama, urutkan berdasarkan hacker_id terkecil lebih dulu

Solusi Code:

![alt text](<image-8.png>)

Penjelasan:

Subquery best_scores mencari skor tertinggi yang diperoleh setiap hacker untuk setiap tantangan, supaya beberapa submission pada tantangan yang sama tidak dijumlahkan semuanya. Hasilnya kemudian digabungkan  dengan tabel Hackers untuk mengambil nama, lalu skor tertinggi dari tiap tantangan dijumlahkan per hacker. Having menyaring hacker yang total skornya lebih dari 0. Terkahir, hasil diurutkan dari total skor terbesar ke terkecil, lalu bedasarkan hacker_id terkecil jika total skornya sama.

Hasil:

![alt text](<image-9.png>)


## Reflection Answers
1. Pada setiap soal saya membaca apa yang diinginkan/diperlukan dari soal yang disajikan yang dimana setelah itu saya membagi menjadi step step kecil. Apabila langkahnya banya, seperti mencari skor tertinggi untuk setiap hacker pada setiap tantangan lalu menjumlahkannya, saya memakai subquery agar prosesnya lebih mudah dibaca. Kalau hanya perlu mengambil nilai ringkasan, agregasi biasa sudah cukup. Saya juga belajar bahwa query yang terlihat rapi belum tentu langsung cocok dengan database yang digunakan. Contohnya query dengan CTE yang saya coba mengalami kegagalan di DB2. Setelah melihat pesan error, saya menggantinya dengan subquery. Dari situ saya belajar untuk memeriksa hasil dan pesan error, lalu menyesuaikan cara penulisan query dengan kebutuhan soal dan database.
2. Teknik yang paling membantu saya ialah agregasi bertahap dan CASE WHEN.. Agregasi bertahap membantu saat satu data perlu diringkas lebih dulu sebelum dihitung lagi, seperti memilih skor tertinggi untuk tiap tantangan sebelum menjumlahkannya per hacker. CASE WHEN membantu mengatur hasil berdasarkan kondisi, misalnya menampilkan nama tertentu atau menggantinya dengan NULL. Saya juga sempat mengalami jawaban yang dinilai salah meskipun hasil angkanya tampak benar, karena format angka desimalnya masih menampilkan nol tambahan. Pengalaman itu mengingatkan saya untuk memeriksa bukan hanya perhitungannya, tetapi juga format hasil dan aturan database. Teknik - teknik ini berguna di pekerjaan nyata, misalnya saat membuat laporan nilai, penjualan, atau kinerja, ketika data perlu dikelompokkan, dibandingkan, lalu disajikan dengan aturan tertentu.
