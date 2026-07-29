- Class: A blueprint or template. Defines what a thing should look like.
- Object: The physical thing built from the blueprint.
- In Python, __init__ stands for "initialize." It is a special method that runs automatically the exact moment you create a new object.
- self represents the specific object you're currently working with.
- When you write self.color = color, you are telling Python: "Take the color passed into the function, and attach it to this specific object's color attribute."
- Every method inside a class must have self as its very first parameter.
- title is just a temporary variable that vanishes when the function ends.
Ex:
class CoffeeCup:
    # __init__ sets up the initial state of every new CoffeeCup
    def __init__(self, color, capacity_oz):
        self.color = color
        self.capacity_oz = capacity_oz
        self.is_full = False  # Default attribute, not passed in

- Classes can hold other classes. If you have a CoffeeShop class, it could have an attribute that is a simple Python list, and you can append CoffeeCup objects to that list.
class CoffeeShop:
    def __init__(self):
        self.cups_in_stock = [] # A list to hold CoffeeCup objects

    def add_cup(self, cup):
        self.cups_in_stock.append(cup)

- Instantiating:
# Create instances
my_cup = CoffeeCup("Red", 12)
my_shop = CoffeeShop()

# Use methods
my_shop.add_cup(my_cup)