import computer
class ResaleShop:

    # What attributes will it need?
        # Inventory, location
    # How will you set up your constructor?
        # Import computer functions and redefine location attribute with self
    inventory = []
    location: str
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, location: str, inventory: list):
        '''
        Assigns location attribute.

        :self: Used with dot notation to get location attribute from ResaleShop class.
        :location: (str) The location of the store.
        :return: (None)

        >>>__init__(self, "New York City")
        None

        >>>__init__(self, "Salt Lake City")
        None

        >>>__init__(self, "Cleveland")
        None
        '''
        self.location = location
        self.inventory = inventory



    # What methods will you need?
        # Changing price of computer, moving computer in and out of inventory (buy/sell), cupdating computer's price and version (refurbish), printing inventory

    def price_change(self, new_price: int, computer_item: str):
        '''
        Changes the price of a computer if the computer called exists in the inventory. If it doesn't the program prints a statement saying it cannot update its price.
        
        :self: Used with dot notation to get price attribute from computer class.
        :new_price: (int) The new price of the computer.
        :computer_item: (computer.Computer) The computer itself.
        :return: (None)
        
        >>>price_change(999,"Macbook Pro")
        "Price of Macbook Pro updated."

        >>>price_change(1, "Macbook Air")
        "Price of Macbook Pro updated."

        >>>price_change(100000, "Windows '98")
        "Computer Windows '98 not found. Cannot update price."
        '''
        self.price = new_price
        if computer_item in self.inventory:
            computer_item.price = new_price
            print("Price of", computer_item.description, "updated.")
        else:
            print("Computer", computer_item.description, "not found. Cannot update price.")



    def buy_computer(self, computer_item: str):
        '''
        Adds a computer to the store's inventory, then prints a statement once complete using the computer's description.

        :self: Used with dot notation to get inventory from ResaleShop class.
        :computer_item: (str) The computer being bought/added.
        :return: (None)
        
        >>>buy_computer(self, computer_item)
        "MacBook Pro added to inventory."

        >>>buy_computer(self, computer_item)
        "Macbook Air added to inventory."

        >>>buy_computer(self, computer_item)
        "Windows '98 added to inventory."
        '''
        self.inventory.append(computer_item)
        print(computer_item.description, "added to inventory.")



    def sell_computer(self, computer_item: str):
        '''
        Removes a computer from the store's inventory if it exists, then prints a statement once complete using the computer's description.  If it doesn't exist, the program prints a statement saying it doesn't have it.

        :self:  Used with dot notation to get inventory from ResaleShop class.
        :computer_item: (str) The computer being sold/removed.
        :return: (None)
        
        >>>sell_computer(self, computer_item)
        "MacBook Pro sold!"

        >>>sell_computer(self, computer_item)
        "Macbook Air sold!"

        >>>sell_computer(self, computer_item)
        "Sorry, we don't have that. Select another computer to sell."
        '''
        if computer_item in self.inventory:
            self.inventory.remove(computer_item)
            print(computer_item.description, "sold!")
        else:
            print("Sorry, we don't have that. Select another computer to sell.")



    def print_inventory(self):
        '''
        Prints inventory with each computer given their own line. Lists computers' details and index in the inventory. If inventory is empty, program prints statement saying there are is no inventory to display.
        :self:  Used with dot notation to get inventory from ResaleShop class.
        :return: (None)
        
        >>>print_inventory(self)
        "Computer: (1500, 10, '1.16', 'Mac Pro (Late 2013)', '3.5 GHc 6-Core Intel Xeon E5', 1024, 64, 'macOS Big Sur', 2013) : 0"

        >>>print_inventory(self)
        "Computer: (1, 3523, '1.0', 'The First Computer', 'Can't process anything', 1, 1, 'The oldest version', 1500 BC) : 0"

        >>>print_inventory(self)
        "No inventory to display."
        '''
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for computer_item in self.inventory:
            # Print its details
                print(f'Computer: {computer_item.return_attributes()} : {self.inventory.index(computer_item)}')
        else:
            print("No inventory to display.")



    def refurbish(self, computer_item: str, new_operating_system: str):
        '''
        If the computer is in the inventory, it updates the price based on the year the computer was made. If there is a new version, the computer is updated. If the computer isn't in the enventory, a statement is printed saying it couldn't find the computer. 
        
        :self: Used with dot notation to get inventory from ResaleShop class.
        :computer_item: The computer being refurbished
        :new_operating_system: The name of the updated version.
        :return: (None)

        >>>refurbish(self, inventory[0], "macOS Monterey")
        "Price of Mac Pro (Late 2013) updated."
        "Mac Pro (Late 2013) OS updated to macOS Monterey"

        >>>refurbish(self, inventory[1], "Windows 98")
        "Price of ThinkPad 701C updated."
        "Windows Laptop (Early 1999) OS updated to Windows 98"

        >>>refurbish(self, "very real computer", "macOS Sierra")
        "Item not found. Please select another item to refurbish."
        '''
        if computer_item in self.inventory:
            if int(computer_item.year_made) < 2000:
                        self.price_change(0, computer_item) # too old to sell, donation only
            elif int(computer_item.year_made) < 2012:
                        self.price_change(250, computer_item) # heavily-discounted price on machines 10+ years old
            elif int(computer_item.year_made) < 2018:
                self.price_change(550, computer_item) # discounted price on machines 4-to-10 year old machines
            else:
                self.price_change(1000, computer_item) # recent stuff

            if new_operating_system is not None:
                computer.Computer.update_version(computer_item, new_operating_system) # update details after installing new OS
                print(computer_item.description, "OS updated to", new_operating_system)
        else:
            print("Item not found. Please select another item to refurbish.")