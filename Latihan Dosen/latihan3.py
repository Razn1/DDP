#Struktur Kendali If
pelanggan = "Adalah Saya"
total_belanja = 15000

#Logika jika belanja > 100rb dapat hadiah
if(total_belanja > 100000):
    ket = "Selamat Anda mendapatkan Hadiah"
else:
    ket = "Terima Kasih sudah berbelanja"

print(f"Pelanggan\t : {pelanggan} \nTotal Belanja\t : Rp{total_belanja} \nKeterangan\t : {ket}")