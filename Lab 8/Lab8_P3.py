def shopping_cart():
    cart = {}  # Initialize an empty shopping cart

    while True:
       # Read user input
        command = input().strip().split()

        action = command[0]

        if action == "add":
            item_name = command[1]
            quantity = int(command[2])

            # Add or update the item in the cart
            if item_name in cart:
                cart[item_name] += quantity
            else:
                cart[item_name] = quantity
            
            print(f"{item_name}: {cart[item_name]}")

        elif action == "remove":
            item_name = command[1]
            amount = command[2]

            # Remove the item from the cart
            if item_name in cart:
                if amount > 0:
                    print(f"{item_name}: {cart[item_name] - quantity}")
                else:
                    print(f"{item_name}: {cart[item_name]}")
            else:
                print("Item not found")

        elif action == "show":
            # Show the current contents of the shopping cart
            if not cart:
                print("Cart is empty")
            else:
                sorted_cart = sorted(cart.items())
                output = ", ".join(f"{item}: {quantity}" for item, quantity in sorted_cart)
                print(output)

        elif action == "quit":
            break

# Output
shopping_cart()