# TODO: it's a playground, let's write some code (no unit tests to run here)
from math import pi
import os
os.system('clear')

def circle_math(radius):
    perimeter = 2*pi*radius
    area =pi*(radius**2)
    return perimeter, area

values = circle_math(5)
print(f'{values} is a list')
print(f"Radius=5 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")
print(f'Perimeter of the circle is {round(values[0], 1)}')
print(f'Area of the disk is {round(values[1], 1)}')

# you can also not use the brackets in the return and just 
# use {perimeter} to call the function parameters.
# use :.2f for two decimal places instead of 1 like above (round(values[1], 1))

radius = 5
perimeter, area = circle_math(radius)
print(f"Perimeter: {perimeter:.2f}, Area: {area:.2f}")