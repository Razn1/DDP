p1 = {'Nama':'Budi', 'Jabatan':'Manager', 'Agama':'Islam', 'Status':'Menikah'}
p2 = {'Nama':'Siti', 'Jabatan':'Asisten Manager', 'Agama':'Islam', 'Status':'Menikah'}
p3 = {'Nama':'I Gede', 'Jabatan':'Supervisor', 'Agama':'Hindu', 'Status':'Menikah'}
p4 = {'Nama':'Joko', 'Jabatan':'Staff', 'Agama':'Islam', 'Status':'Belum Menikah'}
p5 = {'Nama':'Alex', 'Jabatan':'Staff', 'Agama':'Kristen Protestan', 'Status':'Belum Menikah'}

ar_pegawai = [p1, p2, p3, p4, p5]

for pegawai in ar_pegawai:
    if pegawai['Jabatan'] == 'Manager':
        pegawai['Gapok'] = 15000000
    elif pegawai['Jabatan'] == 'Asisten Manager':
        pegawai['Gapok'] = 10000000
    elif pegawai['Jabatan'] == 'Supervisor':
        pegawai['Gapok'] = 7000000
    elif pegawai['Jabatan'] == 'Staff':
        pegawai['Gapok'] = 4000000
    
    
    pegawai['TunjanganJabatan'] = pegawai['Gapok'] * 0.3
    pegawai['BPJS'] = pegawai['Gapok'] * 0.1
    pegawai['TunjanganKeluarga'] = (0, pegawai['Gapok'] * 0.1)[pegawai['Status'] == 'Menikah']
    pegawai['Gakot'] = pegawai['Gapok'] + pegawai['TunjanganJabatan'] + pegawai['TunjanganKeluarga']
    pegawai['Zakat'] = (0, pegawai['Gapok'] * 0.025)[pegawai['Agama'] == 'Islam' and pegawai['Gakot'] >= 7000000]
    pegawai['Gaber'] = pegawai['Gakot'] - pegawai['Zakat'] - pegawai['BPJS']
    
    
    print(f"Nama\t\t\t: {pegawai['Nama']}"
         f"\nJabatan\t\t\t: {pegawai['Jabatan']}"
         f"\nAgama\t\t\t: {pegawai['Agama']}"
         f"\nStatus\t\t\t: {pegawai['Status']}"
         f"\nGaji Pokok\t\t: Rp. {pegawai['Gapok']:,.0f}"
         f"\nTunjangan Jabatan\t: Rp. {pegawai['TunjanganJabatan']:,.0f}"
         f"\nTunjangan Keluarga\t: Rp. {pegawai['TunjanganKeluarga']:,.0f}"
         f"\nBPJS\t\t\t: Rp. {pegawai['BPJS']:,.0f}"
         f"\nZakat\t\t\t: Rp. {pegawai['Zakat']:,.0f}"
         f"\nGaji Kotor\t\t: Rp. {pegawai['Gakot']:,.0f}"
         f"\nGaji Bersih\t\t: Rp. {pegawai['Gaber']:,.0f}\n")

