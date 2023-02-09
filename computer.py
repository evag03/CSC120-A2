class Computer:

    # What attributes will it need?
        # Price of computer, age of computer, OS version before update, description of computer, processor type, hard drive capacity, memory, operating system, year made
    price: int
    age: int
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    # How will you set up your constructor?
        # Redefine attributes with self
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, price: int, age: int, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int):
        self.price = price
        self.age = age
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made

    # What methods will you need?
        # Change the OS version, define the computer's age in years, return computer attributes to class

    def comp_age(self, given_age: int):
        '''
        Assigns computer age attribute.

        :self: Used with dot notation to get age attribute from Computer class.
        :given_age: (str) The age of the computer in years.
        :return: (None)

        >>>comp_age(self, 5)
        None

        >>>comp_age(self, 8)
        None

        >>>comp_age(self, 1)
        None
        '''
        self.age = given_age



    def update_version(self, new_operating_system: str):
        '''
        Updates version of computer.

        :self: Used with dot notation to get version attribute from Computer class.
        :new_version: (str) The version of the computer after updating.
        :return: (None)

        >>>update_version(self, macOS Monterey)
        None

        >>>update_version(self, macOS Ventura)
        None

        >>>update_version(self, Windows 98)
        None
        '''
        self.operating_system = new_operating_system


    def return_attributes(self):
        '''
        Returns the attributes from the Computer class.

        :self: Used with dot notation to get all attributes from Computer class.
        :return: Returns the Computer class' attributes from the constructor

        >>>return_attributes(self)
        self.price, self.age, self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made

        >>>return_attributes(self)
        self.price, self.age, self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made

        >>>return_attributes(self)
        self.price, self.age, self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made
        '''
        return(self.price, self.age, self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made)

