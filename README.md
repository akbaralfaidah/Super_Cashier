# Super_Cashier
## Latar Belakang
Super Cashier adalah sistem kasir self service yang memungkinkan pelanggan bisa memasukkan item, jumlah item dan harga item yang ingin dibeli

Modul disusun dengan menggunakan OOP, try-Except, Function dan Clean Code

## Objektif
Alur pembuatan sistem kasir self service:

1. Customer membuat akun/ID transaksi
2. Customer memasukkan nama item, jumlah item dan harga item yang dibeli
3. Apabila ada kesalahan dalam memasukkan nama,jumlah dan harga maka akan ada function yaitu update_item():
   a. Update nama item
   b. update harga item
   c. update jumlah item
4. Apabila customer membatalkan membeli satu item atau ingin membatalkan semua item maka bisa melakukan hapus item:
   a. hapus 1 item
   b. reset seluruh transaksi
5. Apabila sudah selesai berbelanja tetapi customer masih ragu apakah harga dan nama yang diinput sudah benar maka customer bisa melakukan check order:
   a. Jika tidak ada kesalahan input -> "Pemesanan berhasil"
   b. Jika ada kesalahan input -> "Terdapat kesalahan input"
   c. Menampilkan tabel berisi seluruh data pesanan
6. Customer bisa menampilkan total belanja dan diskon dengan ketentuan
   a. Apabila belanja diatas 500.000 mendapatkan diskon 10%
   b. Apabila belanja diatas 300.000 mendapatkan diskon 8%
   c. Apabila belanja diatas 200.000 mendapatkan diskon 5%

## Flowchart

   ![Gambar Flowchart](/supercashier.jpg)

## Function
1. init()
   Fungsi inisialisasi untuk class Transaction
   
   dict_txn(dict) = dictionary untuk menyimpan data transaksi (dict)

   txn_valid(boolean) = untuk menandai apakah data yang diinput ke dalam dictionary transaksi udah valid. Nilai awal adalah True bisa berubah False setelah dicek validitasnya lewat fungsi

2. add_item(nama, jumlah, harga)
   Fungsi untuk menambahkan item ke dalam dictionary transaksi

   nama(String, key) =  nama item yang dibeli, key ke dalam dictionary

   jumlah(int) = jumlah item yang dibeli
   
   harga(int) = harga per item

3. update_item(nama, nama_baru)
   Fungsi untuk mengubah nama item ke dalam dictionary yang sudah diinnput.

   nama(String) = nama item sebelum diganti, key baru dari dictionary

   nama_baru(String) = nama baru untuk item, menjadi key baru dari dictionary

4. update_item_qty(nama, jumlah_baru)
   Fungsi untuk mengubah jumlah item dalam dictionary yang sudah diinput

   nama(String) = nama item yang ingin diubah jumlahnya, key dari dictionary

   jumlah_baru(int) = jumlah baru dari nama item yang dibeli

5. update_item_price(nama, harga_baru)
   Fungsi untuk mengubah harga item dalam dictionary yang sudah diinput.

   nama(String) = nama item yang ingin diubah jumlahnya, key dari dictionary

   harga_baru(int) = harga baru dari nama item yang dibeli

6. delete_item(nama)
   Fungsi untuk menghapus data nama item beserta jumlah dan harganya dari dictionary.

   nama(String) = nama item yang ingin dihapus

7. reset_transaction()
   Fungsi untuk menghapus semua data pesanan di dalam dictionary

8. print_order()
   Fungsi untuk menampikan semua pesanan ke dalam dictionary

9. check_order()
   Fungsi untuk mengecek validitas dan menampilkan semua pesanan dalam dictionary

10. total_price()
    Fungsi untuk menampilkan semua pesanan dan total belanja


