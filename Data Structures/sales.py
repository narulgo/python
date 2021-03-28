
sales = [
  {
    'location': 'Almaty',
    'amount': 100_000
  },
  {
    'location': 'Moscow',
    'amount': 1_000_000
  },
  {
    'location': 'New York',
    'amount': 50_000
  },
  {
    'location': 'London',
    'amount': 70_000
  }
 ]


def underperforming(sales, threshold):
    result = list(map(lambda sale: sale['location'], filter(lambda sale: sale['amount'] < threshold, sales)))
    return result


print(underperforming(sales, threshold=100_000))

