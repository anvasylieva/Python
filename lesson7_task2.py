def square(base):
    result = base ** 2
    print(f"The square of {base} is {result}")


square(4)

# another_var = 400


def outer_func():
    var = 100
    another_var = 300

    def inner_func():
        # var = 50
        # another_var = 200
        print(f"printing var from inner_func(): {var}")
        print(f"printing another_var from inner_func(): {another_var}")

    inner_func()
    print(f"printing var from outer_func(): {var}")
    print(f"printing another_var from outer_func(): {another_var}")


outer_func()
print(__name__)
print(type(__name__))
print(dir())


