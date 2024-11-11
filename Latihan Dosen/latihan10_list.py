#Struktur data List
ar_buah = ["Pepaya","Mangga","Pisang","Jambu","Belimbing"]
#ganti pisang dengan apel
ar_buah[2] = "Apel"
#Delete Belimbing
del ar_buah[4]
#Menambah Array
ar_buah.insert(2,'Naga')
ar_buah.append('Jeruk')
ar_buah.append('Salak')
ar_buah.append('Melon')
ar_buah.append('Manggis')

print('------------Cetak------------')
for buah in ar_buah:
    print(f'Buah {buah}')
print('--------Select Buah in Range--------')
print(f'Buah {ar_buah[3:6]}')