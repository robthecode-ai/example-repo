# ========The beginning of the class==========


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = str(country)
        self.code = str(code)
        self.product = str(product)
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        This method returns the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):
        '''
        This method returns the quantity of the shoe.
        '''
        return self.quantity

    def __str__(self):
        '''
        This method returns a string representation of the shoe object.
        '''
        return (
            f"Country: {self.country}, "
            f"Code: {self.code}, "
            f"Product: {self.product}, "
            f"Cost: {self.cost}, "
            f"Quantity: {self.quantity}"
        )


# ============= Shoe list ===========
# The list will be used to store a list of objects of shoes.

shoe_list = []


# ==========Functions outside the class==============


def read_shoes_data():
    '''
    This function reads the shoe data from the inventory.txt file and creates
    shoe objects which are appended to the shoe_list.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line

            for line in file:
                data = line.strip().split(",")

                if len(data) == 5:
                    country, code, product, cost, quantity = data
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
                else:
                    print(f"Skipping invalid line: {line.strip()}")

    except FileNotFoundError:
        print("Error: inventory.txt was not found.")

    except Exception as error:
        print(f"An error occurred while reading the file: {error}")


def capture_shoes():
    '''
    This function captures the shoe data
    from the user and creates a shoe object
    which is appended to the shoe_list.
    It also writes the shoe data to the inventory.txt file.
    '''
    try:
        country = input("Enter country: ")
        code = input("Enter code: ")
        product = input("Enter product: ")
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))

        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        with open("inventory.txt", "a") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}")

    except ValueError:
        print("Invalid input. Please enter the correct data types.")


def view_all():
    '''
    This function iterates through the shoe_list
    and prints the details of each shoe.
    '''
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """
    Find the shoe with the lowest quantity,
    update its stock level, and save the changes
    to inventory.txt.
    """
    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())

    print(lowest_shoe)

    while True:
        try:
            amount = int(input("How many would you like to add? "))

            if amount < 0:
                print("Please enter a positive number.")
                continue

            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    lowest_shoe.quantity += amount

    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")

        for shoe in shoe_list:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},"
                f"{shoe.cost},{shoe.quantity}\n")


def search_shoe():
    '''
    This function searches for a shoe in the shoe_list by its code.
    If the shoe is found, it returns the shoe object.
    '''
    code = input("Enter shoe code to search for: ").strip()
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    print("Shoe not found.")
    return None


def value_per_item():
    """
    Calculate and display the total value
    of each shoe item in inventory.
    """
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: Total Value = {value}")


def highest_qty():
    """
    Find and display the shoe with the
    highest quantity in stock.
    """
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"{highest_shoe.product} is for sale!")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

read_shoes_data()
while True:
    print("\nMenu:")
    print("1. Capture Shoes")
    print("2. View All Shoes")
    print("3. Re-stock Shoes")
    print("4. Search for a Shoe")
    print("5. Calculate Value per Item")
    print("6. Identify Shoe with Highest Quantity")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        capture_shoes()
    elif choice == "2":
        view_all()
    elif choice == "3":
        re_stock()
    elif choice == "4":
        shoe = search_shoe()
        if shoe:
            print(shoe)
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
