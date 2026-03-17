# 4⃣ Shopping Cart 
# Classes: 
# ● Item 
# ● Cart 
# Features: 
# ● Add items 
# ● Calculate total 
# ● Discount > ₹10,000 
# ● GST calculation 
# Methods / Concepts to Use: 
# ● Object aggregation (objects inside list) 
# ● Instance methods 
# ● Looping 
# ● Arithmetic logic 

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.items = []   
   
    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:   
            total += item.total_price()
        return total

    def discount(self, total):
        if total > 10000:
            discount = total * 0.10   
            print("10% Discount Applied!")
            return total - discount
        return total
 
    def add_gst(self, total):
        gst = total * 0.18
        return total + gst

    def bill(self):
        total = self.calculate_total()
        print(f"Subtotal: ₹{total}")

        t_after_discount = self.discount(total)
        print(f"After Discount: ₹{t_after_discount}")

        final_amount = self.add_gst(t_after_discount)
        print(f"Final Amount (Including GST): ₹{final_amount}")

item1 = Item("Laptop", 64000, 1)
item2 = Item("Mouse", 399, 2)
item3 = Item("Keyboard", 2000, 1)
cart = Cart()
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)
cart.bill()
