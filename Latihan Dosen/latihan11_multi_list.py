list_makanan = [
    ['Bakwan','Combro','Misro','Tahu','Tempe'],
    ['Sop Iga','Sop Buntut','Sop Ayam','Soto Mie'],
    ['Nasi Uduk','Nasi Goreng','Nasi Rames','Nasi Padang']
]

print('---------Cetak Makanan Tertentu---------')
print(list_makanan[0][3]) #Tahu
print(list_makanan[1][3]) #Soto Mie
print(list_makanan[2][0]) #Nasi Uduk

print('-------Cetak Seluruh Makanan-------')
for menu in list_makanan:
    for food in menu:
        print(f'Makanan {food}')