class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

        
    def send(self, customer, amount):
        self.balance = self.balance - amount
        customer.balance = customer.balance + amount

            
alice = Customer('Alice', 100)
bob = Customer('Bob', 200)
assert alice.balance == 100
assert bob.balance == 200 


alice.send(bob, 10)
assert alice.balance == 90
assert bob.balance == 210


bob.send(alice, 100)
assert alice.balance == 190
assert bob.balance == 110


charlie = Customer('Charlie', 555)
charlie.send(bob, 500)
assert charlie.balance == 55
assert bob.balance == 610


print(alice.balance)
print(charlie.balance)
print(bob.balance)
