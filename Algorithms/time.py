import time


def decorator(func):
    def decorated(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result
    return decorated


def timer(func):
    def decorated(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()))
        return result
    return decorated


def pause(t):
    def wrapper(f):
        def tmp(*args, **kwargs):
            time.sleep(t)
            return f(*args, **kwargs)
        return tmp
    return wrapper


@decorator
@timer
@pause(0)
def func(x, y):
    return x + y


print(func(1, 2))
