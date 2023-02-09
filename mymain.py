import computer
import oo_resale_shop
def main():
    # Creating first computer
    new_computer = computer.Computer(1500, 10, "Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013) 
    # Establishing location
    PearInc = oo_resale_shop.ResaleShop("New York City", [])
    print()
    print("main start!")

    # Inventory error message test
    PearInc.print_inventory()
    print()
    # Adding first computer to inventory
    PearInc.buy_computer(new_computer)
    # Checking new inventory
    PearInc.print_inventory()
    # Creating second computer
    print()
    new_computer = computer.Computer(500, 25, "ThinkPad 701C","Pentium II", 612, 16, "Windows 95", 1995) 
    # Adding second computer to inventory
    PearInc.buy_computer(new_computer)
    # Checking new inventory
    PearInc.print_inventory()
    print()
    # Refurbish error test
    PearInc.refurbish("definitely real computer", "the best version")
    # Refurbishing first computer
    PearInc.refurbish(PearInc.inventory[0], "macOS Monterey")
    # Refurbishing second computer
    PearInc.refurbish(PearInc.inventory[1], "Windows 98")
    # Checking inventory with refurbished computers
    PearInc.print_inventory()
    print()
    # Sell error message test
    PearInc.sell_computer("definitely real computer")
    # Selling/removing first computer from inventory
    PearInc.sell_computer(new_computer)
    # Checking new inventory
    PearInc.print_inventory()
    print()
    print("main end. Goodbye!")


main()