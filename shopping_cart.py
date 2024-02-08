"""
Welcome to the Super Shopping Cart Program!

This program allows you to manage your shopping list with ease. 
You can add items along with their prices, view the contents 
of your cart, remove items, compute the total, and bid adieu 
once your shopping is done. Enjoy a seamless shopping experience!
"""

def main():
    # Initialize empty lists to store the items and their prices in the shopping cart
    cart_items = []
    cart_prices = []
    
    # Start an infinite loop to display the menu and handle user input
    while True:
        # Display the main menu options
        print("\nWelcome to the Shopping Cart Program!\n")
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        
        # Prompt the user to enter an action
        action = input("Please enter an action: ")
        
        # Check the user's input and perform the corresponding action
        if action == '1':
            # Option to add an item to the shopping cart
            item = input("What item would you like to add? ")
            price = float(input(f"What is the price of '{item}'? "))
            cart_items.append(item)  # Add the item to the cart list
            cart_prices.append(price)  # Add the price to the price list
            print(f"'{item}' has been added to the cart.\n")
        elif action == '2':
            # Option to view the contents of the shopping cart
            if not cart_items:
                print("The shopping cart is empty.\n")
            else:
                print("The contents of the shopping cart are:")
                # Display each item and its price with numbering starting from 1
                for index, item in enumerate(cart_items, start=1):
                    print(f"{index}. {item} - ${cart_prices[index-1]:.2f}")
                print()  # Print a newline for better formatting
        elif action == '3':
            # Option to remove an item from the shopping cart
            if not cart_items:
                print("The shopping cart is empty.")
            else:
                print("The contents of the shopping cart are:")
                # Display each item and its price with numbering starting from 1
                for index, item in enumerate(cart_items, start=1):
                    print(f"{index}. {item} - ${cart_prices[index-1]:.2f}")
                choice = input("Which item would you like to remove? ")
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(cart_items):
                        # Remove the selected item and its price from the lists
                        removed_item = cart_items.pop(choice - 1)
                        removed_price = cart_prices.pop(choice - 1)
                        print("Item removed.\n")
                    else:
                        print("Invalid choice. Please enter a valid item number.\n")
                except ValueError:
                    print("Invalid choice. Please enter a valid item number.\n")
        elif action == '4':
            # Option to compute the total price of all items in the shopping cart
            if not cart_items:
                print("The shopping cart is empty.")
            else:
                total_price = sum(cart_prices)  # Calculate the total price
                print(f"The total price of the items in the shopping cart is ${total_price:.2f}\n")
        elif action == '5':
            # Option to quit the program
            print("Thank you. Goodbye.")
            break  # Exit the loop and end the program
        else:
            # Handle invalid input
            print("Invalid action. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
