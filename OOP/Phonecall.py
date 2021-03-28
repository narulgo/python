class Plan:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Phonecall:
    def __init__(self, customer, duration):
        self.customer = customer
        self.duration = duration

        customer.history.append(self)

        customer.balance = customer.balance - self.cost()

    def cost(self):
        return self.duration * self.customer.plan.cost


class Customer:
    def __init__(self, name, balance, plan):
        self.name = name
        self.balance = balance
        self.plan = plan
        self.history = []


if __name__ == '__main__':
    default = Plan('default', 2)
    alice = Customer('Alice', 200, default)
    call1 = Phonecall(alice, 20)
    call2 = Phonecall(alice, 40)
    print(call1.cost())
    print(call2.cost())
    print(alice.history)
    print(alice.balance)
    assert call1.cost() == 40
    assert call2.cost() == 80
    assert alice.history == [call1, call2]
    assert alice.balance == 80


    vip = Plan('VIP', 50)
    charlie = Customer('Charlie', 30000, vip)
    call1 = Phonecall(charlie, 75)
    call2 = Phonecall(charlie, 95)
    print(call1.cost())
    print(call2.cost())
    print(charlie.history)
    print(charlie.balance)
    assert call1.cost() == 3750
    assert call2.cost() == 4750
    assert charlie.history == [call1, call2]
    assert charlie.balance == 21500
