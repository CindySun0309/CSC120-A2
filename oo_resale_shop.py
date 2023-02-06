from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass 

    # What methods will you need?
    def buy(self, new_computer):
        self.inventory.append(new_computer)
        # 1. call Computer(...) constructor to create a new Computer instance
        # 2. call inventory.append(...) to add the new Computer instance to the inventory
    
    def sell(self, remove_computer):
        self.inventory.remove(remove_computer)

    def print_inventory(self):
        print(self.inventory)


    
    
