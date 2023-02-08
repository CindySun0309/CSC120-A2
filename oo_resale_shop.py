from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    def buy(self, new_computer:Computer):
        self.inventory.append(new_computer)
        # 1. call Computer(...) constructor to create a new Computer instance
        # 2. call inventory.append(...) to add the new Computer instance to the inventory
    
    def sell(self, remove_computer:Computer):
        if remove_computer in self.inventory:
            self.inventory.remove(remove_computer)
        else:
            print("There is no such computer in the inventory.")

    def print_inventory(self):
        for computer in self.inventory:
            computer.print_computer()

    def update_price(self, computer:Computer, new_price):
        computer.price = new_price

    def update_operating_system(self, computer:Computer, new_operating_system):
        computer.operating_system = new_operating_system

    #refurbishing a computer (update price based on age of machine, optionally update OS)
    def refurbish(self, computer:Computer):
        if computer in self.inventory:
            if computer["year_made"] < 2000:
                computer["price"] = 0
            elif computer["year_made"] < 2010:
                computer["price"] = 250
            elif computer["year_made"] < 2020:
                computer["price"] = 500
            else:
                computer["price"] = 900
        else:
            print("Item", computer, "not found. Please select another item to refurbish.")

def main():
     myStore = ResaleShop()
     c1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64, "macOS Big Sur", 2013, 1500)
     #c1.print_computer()


     c2= Computer("Mac (Late 1990)",
        "Something",
        100, 64, "Something", 1990, 300)
     #c2.print_computer()

     myStore.buy(c1)
     myStore.buy(c2)
     
     # Two ways to print the inventory: 
     myStore.print_inventory() # 1.with all information
     print(myStore.inventory) # 2.with only the location (counts how many computers are there)

     myStore.update_price(c1, 1000) #Update c1 price from 1500 to 1000
     #myStore.print_inventory()

     myStore.update_operating_system(c1, "Intel") #Change c1 operating system from MacOS to Intel
     #myStore.print_inventory()
     
     myStore.refurbish(c1)
     myStore.print_inventory()

     #myStore.sell(c1)
     #myStore.print_inventory()



     

main()
