menu = [
    ['Mie Ayam','Karedok','Ayam Penyet','Pecel Lele'],
    ['Es Teh','Es Jeruk','Es Kelapa','Jus Alpukat'],
    ['Es Krim','Pisang Goreng','Puding']
]

print(f'Budi Makan {menu[0][2]}, Minum {menu[1][0]}, dan Desert {menu[2][2]}')
print(f'Faisa Makan {menu[0][1]}, Minum {menu[1][1]}, dan Desert {menu[2][0]}')

for food in menu:
    for food_drink in food:
        print(food_drink)