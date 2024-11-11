nilai = { 'Ambatron':89, 'Al':100, 'Bumble Bee':29,'Optimus':95}
print("Data nilai : ",nilai)
#tambah data
nilai['Megatron'] = 50
#looping semua key
for data in nilai.keys():
    kalimat = f"Nilai {data} adalah {nilai[data]}"
    print(kalimat)

# ubah nilai Bumble Bee
nilai['Bumble Bee'] = 10

# hapus nilai Megatron
# nilai.pop('Megatron')
del nilai['Megatron']

print("----------------cetak item saja---------------------")
#looping items (key dan value)
for nama, skor in nilai.items():
    kalimat = f"Nilai {nama} adalah {skor}"
    print(kalimat)