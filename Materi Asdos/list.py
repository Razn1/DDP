topping_popice = ['Choco Crunch','Keju','Chocolate','Wafer']
print(topping_popice[1])
del topping_popice[3]


topping_popice.insert(1,'Choco Chip')
# topping_baru = ['Cincau','Boba','Meses']
topping_popice.append('Meses')
print('---------Cetak All Topping--------')
print(topping_popice)
print('---------Cetak Topping Loop--------')
for topping in topping_popice:
    print(f'Topping yang ada : {topping}')

print('---------Cetak Select with Range--------')
print(topping_popice[0:3])
print('---------Cetak Select with Range--------')
print(topping_popice[1:5])

