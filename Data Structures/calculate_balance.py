
balance = { 'Alice': 100, 'Bob': 100, 'Charlie': 5000, 'Eric': 50, 'Fiona': 300 }
plans = { 'cheap': 1, 'average': 2, 'expensive': 10 }
users = { 'Alice': 'cheap', 'Bob': 'average', 'Charlie': 'expensive', 'Fiona': 'cheap' }
history = [ {'Charlie': 50}, {'Alice': 10}, {'Alice': 20}, {'Bob': 2}, {'Eric': 15} ]


def calculate_balance(balance, plans, users, history):
    user_cost = {name: plans[plan] for name, plan in users.items()}
    for call in history:
        for user, duration in call.items():
            balance[user] = balance[user] - duration * user_cost.get(user, 1)
    return balance



print(calculate_balance(balance, plans, users, history))
assert balance == {'Alice': 70, 'Bob': 96, 'Charlie': 4500, 'Eric': 35, 'Fiona': 300}

