import math

garden = float(input("Input: "))

area = math.pi * math.pow(garden, 2)
circumference = 2 * math.pi * garden
root = math.sqrt(area)
up = math.ceil(area)
down = math.floor(area)

print(f"Area of the Garden: {area:.2f}" )
print(f"Circumference of the Garden: {circumference:.2f}" )
print(f"Square root of the Garden: {root:.2f}" )
print(f"Area rounded down: {down}" )
print(f"Area rounded up: {up}" )