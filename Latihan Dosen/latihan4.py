#If dengan Operator Logika
siswa = 'Deden Hamdani'
nilai = 100

#Logika Lulus Minimal 60
'''
if nilai >= 60:
    ket = 'Lulus'
else:
    ket = 'Tidak Lulus
'''
#Ternary
# ket = nilai >= 60 ? 'Lulus' : 'Gagal'
ket = 'Lulus' if nilai >= 60 else 'Gagal'
'''Logic Grade Nilai
A: 85 - 100
B: 70 - < 85
C: 60 - < 70
D: 40 - < 60
E: 0 - < 40
'''
if nilai >= 85 and nilai <= 100: grade = 'A'
elif nilai >= 70 and nilai < 85: grade = 'B'
elif nilai >= 60 and nilai < 70: grade = 'C'
elif nilai >= 40 and nilai < 60: grade = 'D'
elif nilai >= 0 and nilai < 40: grade = 'E'
else: grade = ''
    
print(f"Siswa\t\t : {siswa} \nNilai\t\t : {nilai} \nKeterangan\t : {ket} \nGrade\t\t : {grade}")    

#If MultiKondisi
cuaca = 'Badai'
# kondisi = 'Sehat'
# uang = 10000
# and kondisi == 'Sehat' and uang >= 10000

if cuaca == 'Cerah': berangkat = 'Jalan Kaki'
elif cuaca == 'Gerimis': berangkat = 'Naik Sepeda'
elif cuaca == 'Hujan Lebat': berangkat = 'Mobil'
else: berangkat = 'Ijin'
    
print(f"Cuaca\t\t : {cuaca} \nBerangkat\t : {berangkat}")