#Luas Persegi
s = 10
lp = s * s

print(f"Luas Persegi dengan Sisi {s} = {lp}")

#Luas Persegi Panjang
p = 13
l = 6
lps = p * l

print(f"Luas Persegi Panjang dengan Panjang {p} dan Lebar {l} = {lps}")

#Luas Segitiga
a = 5
t = 9
ls = 1 / 2 * a * t

print(f"Luas Segitiga dengan Alas {a} dan Tinggi {t} = {ls}")

#Luas Lingkaran
r = 7
pi = 3.14
ll = pi * r * r

print(f"Luas Persegi dengan Phi {pi} dan Jari-Jari {r} = {ll}")

#Perbandingan Lebih Besar dan Lebih Kecil antara Luas Persegi dan Persegi Panjang
print(f"Luas Persegi adalah {lp} sedangkan Luas Persegi Panjang adalah {lps}, maka Luas Persegi > Luas Persegi Panjang =",lp > lps)

print(f"Luas Persegi Panjang adalah {lps} sedangkan Luas Persegi adalah {lp}, maka Luas Persegi Panjang < Luas Persegi =",lps < lp)

#Perbandingan Lebih Besar dan Lebih Kecil antara Luas Segitiga dan Lingkaran
print(f"Luas Segitiga adalah {ls} sedangkan Luas Lingkaran adalah {ll}, maka Luas Segitiga < Luas Lingkaran =",ls < ll)

print(f"Luas Lingkaran adalah {ll} sedangkan Luas Segitiga adalah {ls}, maka Luas Lingkaran > Luas Segitiga =",ll > ls)