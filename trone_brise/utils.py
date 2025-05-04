class Inventory:
    
    # The Class Constructor
    # This one is very basic, it just declares how many items you can fit 
    # in your inventory and creates an Empty list to keep them!
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        
class Item:

    # The Class Constructor
    # Creates a basic item, more attrs can be added for more complexity!
    def __init__(self, name, description, amount, individual_value):
        self.name = name
        self.description = description
        self.amount = amount
        self.individual_value = individual_value
    
    # Property that shows the worth of the item (x amount).
    @property
    def worth(self):
        return f'${self.amount * self.individual_value:.2f}'