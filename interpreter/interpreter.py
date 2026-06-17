math = input("Problem: ")
x, y, z = math.split(" ")
x = int(x)
z = int(z)

if y == "+":
    p = x + z
elif y == "-":
    p = x - z
elif y == "*":
    p = x * z
elif y == "/":
    p = x / z
print(f"{p:.1f}")
