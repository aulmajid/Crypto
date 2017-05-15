# RSA
<b>Deskripsi</b><br>
RSA (Ron Rivest, Shamir, dan Adleman) termasuk ke dalam sistem kriptografi asimetri, dimana kunci untuk melakukan enkripsi dan dekripsi berbeda. Kekuatan utama dari RSA adalah kesulitan dalam memfaktorkan bilangan yang besar, sehingga dapat dimanfaatkan untuk mengamankan data.

<b>Langkah-langkah</b><br>
1. Pilih 2 buah bilangan prima <i>p</i> dan <i>q</i>.
2. Hitung nilai <i>n = p * q</i>. Usahakan agar setidaknya n > 255 agar dapat mewakili seluruh karakter ASCII.
3. Hitung nilai <i>m = (p-1) * (q-1)</i>.
4. Cari nilai <i>e</i>. e merupakan sembarang bilangan dimana <i>FPB(e,m) = 1</i>.
5. Cari nilai <i>d</i>, yang memenuhi persamaan <i>ed ≡ 1 mod m</i> atau <i>d = e^(-1) mod m</i>.
6. Tentukan kunci public <i>(e , n)</i> dan kunci private <i>(d , n)</i>.
7. Fungsi enkripsi → <i>E (ta)=ta^(e) mod n</i> ; dimana ta merupakan karakter ke-a dari message (pesan) yang akan dienkripsi.
8. Fungsi dekripsi → <i>D (ca)=ca^(d) mod n</i> ; dimana ca merupakan karakter ke-a dari ciphertext yang akan didekripsikan.

<b>Referensi</b><br>
- http://octarapribadi.blogspot.co.id/2016/02/enkripsi-dan-dekripsi-menggunakan-rsa.html
- http://doctrina.org/How-RSA-Works-With-Examples.html
