class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def update_description(self, new_description):
        self.description = new_description

    def update_processor_type(self, new_processor_type):
        self.processor_type = new_processor_type

    def uptade_hard_drive_capacity(self, new_hard_drive_capacity):
        self.hard_drive_capacity = new_hard_drive_capacity

    def update_memory(self, new_memory):
        self.memory = new_memory

    def update_operating_system(self, new_operating_system):
        self.operating_system = new_operating_system

    def update_price(self, new_price):
        self.price = new_price

    
    def print_computer(self):
        print(self.description)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.memory)
        print(self.operating_system)
        print(self.year_made)
        print(self.price)
