from IPython.display import clear_output


# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

def shopping_carts(my_cart={}):
    #     creating loop
    total = []
    while True:

        item = input("What is your item? ").title()
        ammount = int(input(f"How many {item}'s will you buy? "))
        cost = float(input(f"How much does {item} cost? "))
        price = int(ammount) * float(cost)

#         updating cart
        my_cart[item] = {'item': item, 'ammount': ammount,
                         'cost': cost, 'price': price}

        clear_output()
        print("Your cart currently has these items:")

        for item, info, in my_cart.items():
            print(
                f"{info['ammount']} {info['item']}: {info['cost']} x {info['ammount']} = {info['price']}")

        ask = input("""Are you finished with your purchases? Press A if you'd like to add.\n 
            If you'd like to remove something press r.
            If you are finished enter c to check out. """).lower()

        while ask not in {'c', 'r', 'a'}:
            clear_output()
            ask = input(
                'that is not a valid response. Please answer c, r or a.')

        if ask == 'r':
            clear_output()
            for item in my_cart.items():
                my_cart.pop(input("What would you like to remove?").title())
                ask = input(
                    "Would you like add more items or would you like to check out? a or c")
                break

        if ask == 'a':
            continue

        if ask == 'c':
            for item, info in my_cart.items():
                total.append(int(info['price']))

            total = sum(total)
            break

    print("Your cart currently has these items:")
    for item in my_cart.items():
        print(
            f"{info['ammount']} {info['item']}: {info['cost']} x {info['ammount']} = {info['price']}")
        print(f"Your total ammount is ${total}")
        return my_cart


shopping_carts()
