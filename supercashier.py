import pandas as pd
from tabulate import tabulate


class Transaction:
    def __init__(self):
        '''init() Fungsi inisialisasi untuk class Transaction
        dict_txn(dict) = dictionary untuk menyimpan data transaksi (dict)
        txn_valid(boolean) = untuk menandai apakah data yang diinput ke dalam dictionary transaksi udah valid. Nilai awal adalah True bisa berubah False setelah dicek validitasnya lewat fungsi
        '''

        self.dict_txn = dict()
        self.txn_valid = True

    def add_item(self, nama, jumlah, harga):
        '''add_item(nama, jumlah, harga) Fungsi untuk menambahkan item ke dalam dictionary transaksi
        nama(String, key) = nama item yang dibeli, key ke dalam dictionary
        jumlah(int) = jumlah item yang dibeli
        harga(int) = harga per item
        '''

        # mengecek tipe data integer
        if type(jumlah) != int:
            print("Masukkan Jumlah barang dalam bentuk angka!")

        elif type(harga) != int:
            print("Masukkan Harga barang dalam bentuk angka!")

        else:
            # memasukkan data ke dalam dictionary
            dict_add = {nama: [jumlah, harga, jumlah*harga]}
            self.dict_txn.update(dict_add)
            print(
                f'Menambahkan ke dalam pesanan: {nama} sebanyak {jumlah} dengan harga Rp {harga}')

    def update_item_name(self, nama, nama_baru):
        '''update_item(nama, nama_baru) Fungsi untuk mengubah nama item ke dalam dictionary yang sudah diinnput.
            nama(String) = nama item sebelum diganti, key baru dari dictionary
            nama_baru(String) = nama baru untuk item, menjadi key baru dari dictionary
        '''
        
        temp = self.dict_txn[nama]
        self.dict_txn.pop(nama)
        self.dict_txn.update({nama_baru: temp})
        
        #menampilkan data pesanan setelah terjadi perubahan
        self.print_order()
        print(f"Mengubah nama item {nama} menjadi {nama_baru}")
        
    def update_item_qty(self, nama, jumlah_baru):
        '''update_item_qty(nama, jumlah_baru) Fungsi untuk mengubah jumlah item dalam dictionary yang sudah diinput
            nama(String) = nama item yang ingin diubah jumlahnya, key dari dictionary
            jumlah_baru(int) = jumlah baru dari nama item yang dibeli
        '''
        
        #mengecek tipe data integer
        if type(jumlah_baru) != int:
            print("Masukkan jumlah barang dalam bentuk angka!")
            
        else:
            #memasukkan data ke dalam dictionary
            self.dict_txn[nama][0]= jumlah_baru
            self.dict_txn[nama][2]= jumlah_baru*self.dict_txn[nama][1]
            
            #menampilkan data pesanan setelah terjadi perubahan
            self.print_order()
            print(f'mengubah jumlah item {nama} menjadi {jumlah_baru}.')
            
            
    def update_item_price(self, nama, harga_baru):
        '''update_item_price(nama, harga_baru) Fungsi untuk mengubah harga item dalam dictionary yang sudah diinput.
            nama(String) = nama item yang ingin diubah jumlahnya, key dari dictionary
            harga_baru(int) = harga baru dari nama item yang dibeli
        ''' 
        
        #mengecek tipe data integer
        if type(harga_baru)!=int:
            print("Masukkan harga barang berupa angka!")
            
        else:
            #memasukkan data ke dalam dictionary
            self.dict_txn[nama][1]= harga_baru
            self.dict_txn[nama][2]= harga_baru*self.dict_txn[nama][0]
            
            #menampilkan data pesanan setelah terjadi perubahan
            self.print_order()
            print("Mengubah harga item {nama} menjadi {harga_baru}.")
            
    def delete_item(self, nama):
        '''Fungsi untuk menghapus data nama item beserta jumlah dan harganya dari dictionary.
        nama(String) = nama item yang ingin dihapus'''
        
        try:
            self.dict_txn.pop(nama)
            print("Menghapus pesanan {nama}")
            print("")
            self.print_order()
            
        except KeyError:
            print(f"{nama} ini tidak ada di dalam daftar pesanan")
            
            
    def reset_transaction(self):
        '''Fungsi untuk menghapus semua data pesanan di dalam dictionary'''

        self.dict_txn = self.dict_txn.clear
        print("Semua item di reset")
            
    def print_order(self):
        '''Fungsi untuk menampikan semua pesanan ke dalam dictionary'''
        
        try:
            table_txn = pd.DataFrame(self.dict_txn).T
            headers = ["Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
            print(tabulate(table_txn, headers, tablefmt="github"))
            
        except:
            print("Tidak ada pemesanan")

    def check_order(self):
        '''Fungsi untuk mengecek validitas dan menampilkan semua pesanan dalam dictionary'''
        try:
            #menampilkan semua pesanan
            table_txn = pd.DataFrame(self.dict_txn).T
            headers = ["Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
            print(tabulate(table_txn, headers, tablefmt="github"))

            kolom = 0
            while kolom < 2:
                for data in table_txn[kolom]:
                    if data <= 0:
                        self.txn_valid = False
                kolom +=1
                

            if self.txn_valid:
                print("Pemesanan berhasil")
            else:
                print("Terdapat kesalahan input, cek ulang pesanan anda")

        except ValueError:
            print("Tidak ada pemesanan")
    
    def total_price(self):
        '''Fungsi untuk menampilkan semua pesanan dan total belanja'''
        
        #memastikan pesanan sudah valid sebelum menjalankan method
        self.check_order()
        
        #menghitung diskon yang didapat
        if self.txn_valid:
            
            #menghitung total belanja
            total_belanja = 0
            for item in self.dict_txn:
                total_belanja += self.dict_txn[item][2]
                
            #menghitung dikon
            if total_belanja > 500_000:
                diskon = int(total_belanja*0.1)
                total_belanja = int(total_belanja-diskon)
                print(f'selamat anda mendapatkan diskon sebesar 10% maka potongan anda menjadi Rp {diskon}')
                print(f"Total belanja anda adalah Rp {total_belanja}")                
                
            elif total_belanja > 300_000:
                diskon = int(total_belanja*0.08)
                total_belanja = int(total_belanja-diskon)
                print(f'selamat anda mendapatkan diskon sebesar 10% maka potongan anda menjadi Rp {diskon}')
                print(f"Total belanja anda adalah Rp {total_belanja}")                
                
            elif total_belanja > 200_000:
                diskon = int(total_belanja*0.05)
                total_belanja = int(total_belanja-diskon)
                print(f'selamat anda mendapatkan diskon sebesar 10% maka potongan anda menjadi Rp {diskon}')
                print(f"Total belanja anda adalah Rp {total_belanja}")                
            
            else:
                print(f"Total belanja anda adalah Rp {total_belanja}")                
            
        else:
            print("Terjadi kesalahan coba lakukan pengulangan input")


#TEST CASE

#test case 1 menambahkan item
transaksi = Transaction()
transaksi.add_item("Ayam goreng", 2, 20_000)
transaksi.add_item("Pasta Gigi", 3, 15_000)

#test case 2 menghapus item
transaksi.delete_item("Pasta Gigi")

#test case 3 mereset transaksi
transaksi.reset_transaction()

#test case 4 menghitung total belanja
transaksi = Transaction()
transaksi.add_item("Ayam goreng", 2, 20_000)
transaksi.add_item("Pasta Gigi", 3, 15_000)
transaksi.total_price()
