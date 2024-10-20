print("-----------------------")
print("Luas Bidang")
print("-----------------------")

print("Pilih Bidang : \n1. Segitiga \n2. Lingkaran \n3. Persegi Panjang\n")

while True:
    pilihan = int(input("Masukan Pilihan : "))
    #Segitiga
    if pilihan == 1 : 
        a = eval(input("Masukan Alas\t :"))
        t = eval(input("Masukan Tinggi\t :"))
        
        #hitung luas
        hasil = 0.5 * a * t
        print(f"Hasil dari perhitungan luas dari segitiga adalah {hasil}")
    elif pilihan == 2 : 
        r = eval(input("Masukan Jari Jari :"))
        pi = 3.14
        
        #hitung luas
        hasil = pi * r * r
        print(f"Hasil dari perhitungan luas dari segitiga adalah {hasil}")
    elif pilihan == 3 : 
        p = eval(input("Masukan Panjang\t :"))
        l = eval(input("Masukan Lebar\t :"))
        
        #hitung luas
        hasil = p * l
        print(f"Hasil dari perhitungan luas dari segitiga adalah {hasil}")
    else: print("Nomor yang Anda Masukan Tidak ada dalam Daftar")
