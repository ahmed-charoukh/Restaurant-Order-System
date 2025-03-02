class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "New"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        items_list = "\n".join([str(item) for item in self.items])
        total = self.calculate_total()
        return f"Order ID: {self.order_id}\nStatus: {self.status}\nItems:\n{items_list}\nTotal: ${total}"


class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)
        print(f"Added {name} to the menu.")

    def remove_menu_item(self, name):
        self.menu = [item for item in self.menu if item.name != name]
        print(f"Removed {name} from the menu.")

    def create_order(self):
        order_id = len(self.orders) + 1
        order = Order(order_id)
        self.orders.append(order)
        print(f"Created new order with ID: {order_id}")
        return order

    def display_menu(self):
        print("Menu:")
        for item in self.menu:
            print(item)

    def display_orders(self):
        if not self.orders:
            print("No orders available.")
        else:
            for order in self.orders:
                print(order)


restaurant = Restaurant()

restaurant.add_menu_item("Burger", 5.99)
restaurant.add_menu_item("Pizza", 8.99)
restaurant.add_menu_item("Salad", 4.99)

restaurant.display_menu()

order1 = restaurant.create_order()
order1.add_item(MenuItem("Burger", 5.99))
order1.add_item(MenuItem("Salad", 4.99))

restaurant.display_orders()

order1.update_status("In Progress")

restaurant.display_orders()

order2 = restaurant.create_order()
order2.add_item(MenuItem("Pizza", 8.99))

restaurant.display_orders()
