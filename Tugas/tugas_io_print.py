while True:
    print("---------- PT.XYZ ----------")
    #Input 
    nama = input("Nama\t\t\t : ").capitalize()
    while not nama : 
        print("Nama Tidak Boleh Kosong, Harap Isi Kembali")
        nama = input("Nama\t\t\t : ").capitalize()
        
    agama = input("Agama\t\t\t : ").capitalize()
    while not agama :
        print("Agama Tidak Boleh Kosong, Harap Isi Kembali")
        agama = input("Agama\t\t\t : ").capitalize()
        
    divisi = input("Divisi\t\t\t : ").capitalize()
    while not divisi :
        print("Divisi Tidak Boleh Kosong, Harap Isi Kembali")
        divisi = input("Divisi\t\t\t : ").capitalize()
    
    jabatan = input("Jabatan (Staff, Kabag, Manager) : ").capitalize()
    while not jabatan :
        print("Jabatan Tidak Boleh Kosong, Harap Isi Kembali")
        jabatan = input("Jabatan (Staff, Kabag, Manager) : ").capitalize()

    #Cek Jabatan Valid atau Tidak
    if jabatan == "Manager" :
        status = "Manager"
    elif jabatan == "Staff" :
        status = "Staff"
    elif jabatan == "Kabag" :
        status = "Kabag"
    else :
        status = "Tidak Memiliki Jabatan PT.XYZ"
        
    #Gaji Pokok
    if jabatan == "Staff":
        gapok = 4000000
    elif jabatan == "Kabag":
        gapok = 7000000
    elif jabatan == "Manager":
        gapok = 10000000
    else:
        gapok = 0

    #Tunjangan Jabatan
    tunjab = 0.2 * gapok

    #Gaji Kotor
    gakot = gapok + tunjab

    #Zakat Profesi
    zakat = gapok * 0.025 if agama == "Islam" and gakot >= 7000000 else 0 

    #Gaji Bersih
    gaber = gapok + tunjab - zakat

    #Cetak
    print(f"\nNama\t\t : {nama}"
        f"\nAgama\t\t : {agama}"
        f"\nDivisi\t\t : {divisi}"
        f"\nJabatan\t\t : {status}"
        f"\nGaji Pokok\t : Rp {gapok:,.0f}"
        f"\nTunjangan Jabatan: Rp {tunjab:,.0f}"
        f"\nGaji Kotor\t : Rp {gakot:,.0f}"
        f"\nZakat Profesi\t : Rp {zakat:,.0f}"
        f"\nGaji Bersih\t : Rp {gaber:,.0f}")
    retry = input("Ingin Menginput Kembali? (Y/N) : ").upper()
    if retry == "N":
        break
    
print("Sukses Mengisi Form, Terima Kasih Karena Telah Mengisi") 