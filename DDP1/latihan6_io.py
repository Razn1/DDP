nama = input("Nama Mahasiswa\t: ")
bb = float(input("Berat Badan\t: "))
tb = float(input("Tinggi Badan\t: "))
fisik = str("")
imt = bb /(tb ** 2)

if imt > 0 and imt < 18.5 : 
    fisik = "Kurus"
elif imt >= 18.5 and imt < 25 : 
    fisik = "Normal"
elif imt >= 25 and imt < 30 : 
    fisik = "Overweight"
elif imt >= 30 : 
    fisik = "Obesitas"
else: imt = "Kurang Gizi"

print("Nama Mahasiswa\t: %s"
      "\nBerat Badan\t: %.2f"
      "\nTinggi Badan\t: %.2f"
      "\nIMT\t\t: %.2f" 
      "\nKondisi Fisik\t: %s" 
      %(nama,bb,tb,imt,fisik))