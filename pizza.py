class Pizza:

    def __init__(self):
        self.size = ""
        self.crust_type = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        topping_str = ', '.join(self.toppings)
        print(f"I would like a {self.size}, {self.crust_type} pizza with {topping_str}")

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust_type = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()

veg = Pizza()
veg.size = 12
veg.crust_type = "thin crust"
veg.add_topping("sun-dried tomatoes")
veg.add_topping("green peppers")
veg.print_order()