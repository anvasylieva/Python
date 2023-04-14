a = "Hello world"
result = ""
for char in a:
    if char == "o":
        result = result + "a"
    elif char == "l":
        result = result + "e"
    else:
        result = result + char
print(result)

b = ""
i = 0
while i < len(a):
    if a[i] == "o":
        b = b + "a"
    elif a[i] == "l":
        b = b + "e"
    else:
        b = b + a[i]
    i += 1
print(b)


