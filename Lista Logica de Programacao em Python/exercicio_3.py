import math

radius = float(input("informe o raio da circunferência: "))
perimeter = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f"Radius: {radius}")
print(f"Perimeter: {round(perimeter, 2)}")
print(f"Area: {round(area, 2)}")