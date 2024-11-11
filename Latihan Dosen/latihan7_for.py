#Belajar Looping For 
print("---------Cetak Angka 1 - 15---------")
angka = 15
for no in range(angka):
    #no = no + 1 
    no += 1 #Increment Assignment
    print(f"Angka {no}")

print("------Cetak Angka 5 - 30------")
awal = 5
akhir = 30
step = 1
for no in range(awal,akhir,step):
    print(f"Angka {no}")
    no += 1   

print("------Cetak Angka 5 - 30------")
awal = 5
akhir = 30
step = 2
for no in range(awal,akhir,step):
    #Modulus Ganjil
    if(no % 2 == 1):
        print(f"Angka {no}")
        no += 1 