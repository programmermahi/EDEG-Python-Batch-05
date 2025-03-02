import math

num = float(input("Enter a number: "))
sqrt1 = math.sqrt(num)
sqrt2 = math.sqrt(sqrt1)
result = sqrt1 + sqrt2
print(f"First square root: {sqrt1}")
print(f"Second square root: {sqrt2}")
print(f"Sum of both: {result}")
