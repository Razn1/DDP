#Ternary
customer = 'Al'
totall = 500000

ket = 'Selamat Anda Mendapatkan Cash Back 10000' if totall >= 100000 else 'Terima Kasih sudah Belanja'
print(f"Pelanggan\t : {customer} \nTotal Belanja\t : {totall} \nKeterangan\t : {ket}")