string = ""
bar = 1
baris = int(input('Masukan Jumlah Baris : '))

#Looping Bintang Menggunakan While
while bar <= baris:
    col = bar
    while col > 0:
        string += "*"
        col -= 1
    string += "\n"
    bar = bar + 1
print (string)
