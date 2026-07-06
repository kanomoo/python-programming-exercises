name1, qa1, price1, name2, qa2, price2 = input("Enter item 1 name: "), int(input("Enter item 1 quantity: ")), float(input("Enter item 1 price: ")), input("Enter item 2 name: "), int(input("Enter item 2 quantity: ")), float(input("Enter item 2 price: "))
print(f"{"-" * 54}\n|{"Item":16}|{"Qty":^9}|{"Price":>12} |{"Total":>11}|\n{"-" * 54}")
print(f"|{name1:16}|{qa1:^9}|{price1:>12.2f} |{qa1 * price1:>11,.2f}|")
print(f"|{name2:16}|{qa2:^9}|{price2:>12.2f} |{qa2 * price2:>11,.2f}|\n{"-" * 54}")
total = qa1 * price1 + qa2 * price2
print(f"|{"Subtotal":40}|{total:>11,.2f}|")
print(f"|{"Vat":40}|{total * 0.07:>11,.2f}|")
print(f"|{"Grand Total":40}|{total + total * 0.07:>11,.2f}|\n{"=" * 54}")