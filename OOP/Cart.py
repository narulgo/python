

class Item:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost


class Cart:
  def __init__(self, customer):
    self.items = {}
    self.customer = customer
    customer.cart = self


  def cost(self):
    return sum(item.cost * quantity for item, quantity in self.items.items())


  def checkout(self):
    if self.cost() > self.customer.money:
      return False
    self.customer.money -= self.cost()
    return True


class Customer:
  def __init__(self, name, money):
    self.name = name
    self.money = money


  def add_to_cart(self, item, quantity=1):
    if item in self.cart.items: 
      self.cart.items[item] += quantity
    else:
      self.cart.items[item] = quantity


  def remove(self, item, quantity=1):
    if item in self.cart.items and quantity > 0: 
      self.cart.items[item] -= quantity
      if self.cart.items[item] <= 0:
        del self.cart.items[item]


alice = Customer('Alice', 600)
purse = Item('Purse', 50)
cart = Cart(alice)
dress = Item('Dress', 500)
alice.add_to_cart(purse)
print(cart.items)
print(cart.cost())
print(cart.checkout())
print(alice.money)
cart2 = Cart(alice)
alice.add_to_cart(dress)
print(cart2.items)
print(cart2.cost())
print(cart2.checkout())
print(alice.money)
cart3 = Cart(alice)
alice.add_to_cart(purse, 3)
print(cart3.items)
print(cart3.cost())
print(cart3.checkout())
print(alice.money)
alice.remove(purse, 2)
print(cart3.checkout())
print(alice.money)

