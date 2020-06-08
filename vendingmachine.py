#set up menu

#money in
#
#item 1
#item 2
#item 3
#item 4
#add money
#get change/exit

balance = float(0.00)

menu = {
    "Soda": "1.00",
    "Lemonade": "1.15",
    "Water": "1.25",
    "Tea": "0.80",
}

#not quite right, but something like this
while balance == 0.00:
    print({balance})
    print("")
    for item, price in menu.items() and i < 5
        listing = (item, price)
        print(i + ") " + " $".join(listing))
        print((len(menu) += 1) +") " + "Add currency")
        balance = input("Amount to add:")
    print