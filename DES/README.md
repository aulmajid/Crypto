# DES
<b>Deskripsi</b><br>
DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci internal (internal key) atau upa-kunci (subkey). Kunci internal dibangkitkan dari kunci eksternal (external key) yang panjangnya 64 bit.

<b>Langkah-langkah</b><br>
1.	Langkah pertama: (a).	Ubah plaintext kedalam biner. (b).	Ubah key kedalam biner.
2.	Langkah kedua: Lakukan Initial Permutation (IP) pada bit plaintext menggunakan tabel IP.
3.	Langkah ketiga: Generate kunci yang akan digunakanuntuk mengenkripsi plaintext dengan menggunakan tabel permutasi kompresi PC-1, pada langkah ini terjadi kompresi dengan membuang 1 bit masing-masing blok kunci dari 64 bit menjadi 56 bit.
4.	Langkah keempat: Lakukan pergeseran kiri (Left Shift).
5.	Langkah kelima: Pada langkah ini, kita akan meng-ekspansi data Ri-1 32 bit menjadi Ri 48 bit sebanyak 16 kali putaran dengan nilai perputaran 1<= i <=16 menggunakan Tabel Ekspansi (E).
6.	Langkah keenam: Setiap Vektor Ai disubstitusikan kedelapan buah S-Box(Substitution Box), dimana blok pertama disubstitusikan dengan S1, blok kedua dengan S2 dan seterusnya dan menghasilkan output vektor Bi32 bit.

<b>Referensi</b><br>
- http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html

# Socket (Client Server)
<b>Deskripsi</b><br>
Adalah aplikasi client dan server, dimana client dapat mengirimkan pesan ke server berupa pesan yang sudah di enkrip. Server akan mendecrypt pesan tersebut. Sehingga, isi pesan yang dikirimkan client ke server tidak dapat dibaca melalui wireshark.

<b>Langkah-langkah</b><br>
1.	Server dinyalakan, maka akan dibuat sebuah socket yang alamatnya sudah diatur.
2.	Server melakukan pengecekan input terhadap socket tersebut menggunakan select.
3.	Client membuat socket baru dan dikoneksikan kepada socket server
4.	Jika server telah terhubung dengan client, maka server akan menunggu kiriman dari client
5.	Setelah itu, pada client, pengguna menginputkan pesan
6.	Client mengenkrip pesan yang diinputkan pengguna, lalu dikirim ke server
7.	Server menerima pesan dari client, lalu mendekrip
8.	Server menampilkan pesan

<b>Referensi</b><br>
- http://ilmu-kriptografi.blogspot.co.id/2009/05/algoritma-des-data-encryption-standart.html
- Tugas mata kuliah progjar tentang socket dan select

# Diffie-Hellman
<b>Deskripsi</b><br>
Diffie-Hellman key exchange adalah metode dimana subyek menukar kunci rahasia   melalui   media   yang   tidak   aman   tanpa   mengekspos   kunci dan tanpa kunci tambahan. Metode ini memiliki dua parameter yaitu q (bilangan prima) dan a ( disebut generator, berupa integer dan lebih kecil dari q dan merupakan primitive root dari q). Kedua parameter tersebut publik dan dapat digunakan  oleh  semua  pengguna  sistem. Selain itu terdapat dua parameter lagi yang masing-masing hanya dimiliki oleh pengirim dan penerima saja.

<b>Langkah-langkah</b><br>
1. Pihak pengirim dan penerima bersama-sama menyepakati nilai q dan a.
2. Kedua pihak memilih sebuah nilai untuk disimpan sendiri (xa dan xb) yang bernilai lebih kecil dari q.
3. Pengirim menghitung nilai ya dan penerima menghitung nilai yb.
4. Pengirim mengirim nilai ya dan penerima mengirim nilai yb.
5. Pengirim menghitung nilai key dari yb dan ka, penerima menghitung nilai key dari yb dan ka.
6. Didapatkan nilai key yang sama.

<b>Referensi</b><br>
- http://maisaro-rambe.blogspot.co.id/2015/06/penjelasan-tentang-metode-rsa-diffie.html
