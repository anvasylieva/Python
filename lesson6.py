def f(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

# *args - unpack t
# *kwargs - розпаковка dictionary

f('aaaa', 5, 5, 6, 7, 15, ddf = 6667, hhhh = "fgfgfg")

# a = aaaa
# b = 5
# args = (5, 6, 7, 15)
# kwargs = {'ddf': 6667, 'hhhh': 'fgfgfg'}

def qqq(x, y, z):
    """It is function..."""
    pass

# to print comment from function qqq()
print(qqq.__doc__)


def task_1(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        result = 0 if (a + b) > 0 else -1
        return result
    else:
        return 1


print(task_1(1, 3))
print(task_1("as", 3))
print(task_1(8.5, 3))
print(task_1(-1, -3))