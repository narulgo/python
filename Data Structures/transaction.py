balance = {'user1': 100, 'user2': 500}
transactions = [{'user1': 50, 'user2': 10},
                 {'user1': 30, 'user2': -10},
                 {'user1': 100}, {'user2': -50}]

def apply_transactions(balance, transactions):
    for transaction in transactions:
        for user, money in transaction.items():
            balance[user] = balance[user] + money
    return balance

print(apply_transactions(balance, transactions))
assert balance, transactions == {'user1': 280, 'user2': 450}
