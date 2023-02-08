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
    def print_computer(self):
        print("Description:", self.description)
        print("Processor Type:", self.processor_type)
        print("Hard Drive Capacity:", self.hard_drive_capacity)
        print("Memory:", self.memory)
        print("Operating System:", self.operating_system)
        print("Year Made:", self.year_made)
        print("Price:", self.price)


