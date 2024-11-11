#Latihan Nested Loop
a = int(input('Masukan Jumlah Baris : '))
s = a - 1
for i in range(0,a):
    for a in range(0, s):
        print(' ', end='')
    s -= 1
    for a in range(0, i + 1):
        print('* ', end='')
    print('')