def is_prime(number):
    if not isinstance(number, int) or number < 0:
        return False

    if number in (0, 1):
        return False

    for element in range(2, number):
        if number % element == 0:
            return False
    return True


print(is_prime(1))
assert is_prime(2)
assert is_prime(3)
assert is_prime(5)
assert is_prime(7)
assert is_prime(97)
assert not is_prime(93)
assert not is_prime(4)
assert not is_prime(16)
assert not is_prime(21)
assert is_prime(101)