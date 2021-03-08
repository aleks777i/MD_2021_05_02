from functools import wraps


def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        print(f"Function {func.__name__} has been called {wrapper.counter} times")
        return func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper


@call_counter
def print_ok():
    print('Ok')


@call_counter
def print_hi():
    print('Hi')


print_ok()
print_ok()
print_hi()
print_ok()
print_hi()
