# Task 2: Numbers

# 1. Function using format()
def format_value(number, character):
    return "{}{}".format(number, character)

result = format_value(145, "o")
print("1. Formatted result:", result)
print("Representation used: string formatting with {} placeholders.")

# 2. Circular pond
radius = 84
pi = 3.14

area = pi * radius ** 2
print("2. Area of pond =", area, "square meters")

# Bonus: 1.4 liters per square meter
water = area * 1.4
print("Total water =", int(water), "liters")

# 3. Speed
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds
print("3. Speed =", int(speed), "m/s")
