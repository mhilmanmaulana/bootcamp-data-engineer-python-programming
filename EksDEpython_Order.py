class Order:


    def __init__ (self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_tax (self, tax_rate):
        return self.total_amount * tax_rate

    def display_order (self):
        print (f"ID: {self.order_id} | Nama: {self.customer_name} | Total: {self.total_amount}")

class OrderProcessor:


    def __init__(self):
        self.orders = []

    def add_order (self, order):
        self.orders.append(order)

    def calculate_total_revenue (self):
        total = 0
        for order in self.orders:
            total = total + order.total_amount
        return total

    def calculate_total_tax (self, tax_rate):
        tax_total = 0
        for order in self.orders:
            tax_total = tax_total + order.calculate_tax(tax_rate)
        return tax_total
                    
pesanan1 = Order("001", "Budi", "2024-01-13", 100000)
pesanan2 = Order("002", "Arman", "2024-01-23", 150000) 
pesanan3 = Order("003", "Mirna", "2024-02-22", 70000) 
pesanan4 = Order("004", "Zubzub", "2024-03-14", 300000) 
pesanan5 = Order("005", "Ayub", "2024-04-09", 300000) 
pesanan6 = Order("006", "Aan", "2024-04-04", 300000)         



prosesor = OrderProcessor()
prosesor.add_order(pesanan1)
prosesor.add_order(pesanan2)
prosesor.add_order(pesanan3)
prosesor.add_order(pesanan4)
prosesor.add_order(pesanan5)
prosesor.add_order(pesanan6)
pesanan1.display_order()
pesanan2.display_order()
pesanan3.display_order()
pesanan4.display_order()
pesanan5.display_order()
pesanan6.display_order()
print(prosesor.calculate_total_revenue())
print(prosesor.calculate_total_tax(0.1))