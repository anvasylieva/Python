a = 123
b = str(a)
c = list(b)

print(c)

print("type of a:", type(a))
print("type of b:", type(b))

print(iter(b))

sss = iter(b)
print(sss)

step_1 = next(sss)
print(step_1)
step_2 = next(sss)
print(step_2)

list_1 = []
list_2 = [None]

print(f"list_1: {list_1}")
print(f"list_1: {bool(list_1)}")
print(f"list_2: {list_2}")
print(f"list_1: {bool(list_2)}")

f = "dfdlojxmc,xmlkoglpj"
print(f"max: {max(f)}, min: {min(f)}")

# lambda arg1, arg2, ..., argn: вираз, який використовує аргументи

g = (lambda x, y, z: x + y * z)

print(g(1, 2, 3))

list_3 = [
    lambda x: pow(x, 0),
    lambda x: pow(x, 1),
    lambda x: pow(x, 2),
    lambda x: pow(x, 3),
]

print(list_3[2](4))

for i in list_3:
    print(i(2))

