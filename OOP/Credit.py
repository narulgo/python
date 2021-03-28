class Product:
    def __init__(self, name, interest):
        self.name = name
        self.interest = interest * 0.01


class Credit:
    def __init__(self, customer, amount, product):
        self.amount = amount
        self.cost = amount
        self.customer = customer
        self.product = product
        self.counter = 0
        customer.credits.append(self)
    def pay(self, amount):
        self.cost -= amount
        if self.cost == 0:
            self.customer.credits.remove(self)
    def tick(self):
        self.cost = self.cost + self.cost * self.product.interest
        self.counter += 1


class Customer:
    def __init__(self, name):
        self.name = name
        self.credits = []
    def take_credit(self, product, amount):
        credit = Credit(self, amount, product)
        return credit
    def pay(self, credit, amount):
        credit.pay(amount)


default = Product('default', 10) 
alice = Customer('Alice') 
credit = alice.take_credit(default, 1000) 
assert alice.credits == [credit] 
credit.tick() 
assert credit.cost == 1100 
assert credit.counter == 1 
credit.tick() 
assert credit.cost == 1210 
assert credit.counter == 2 
alice.pay(credit, 210) 
assert credit.cost == 1000 
alice.pay(credit, 1000) 
assert credit.cost == 0 
assert alice.credits == []
print(alice.credits)

