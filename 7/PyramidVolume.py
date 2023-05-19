#7.5.2: Function definition: Volume of a pyramid with modular functions.
#Define a function calc_pyramid_volume() with parameters 
#base_length, base_width, and pyramid_height, 
#that returns the volume of a pyramid with a rectangular base. 
#calc_pyramid_volume() calls the given calc_base_area() function in the calculation.

#Relevant geometry equations:
#Volume = base area x height x 1/3

def calc_base_area(base_length, base_width):
   return base_length * base_width

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    base_area = calc_base_area(base_length, base_width)
    return round((base_area * pyramid_height / 3), 2)


length = float(input())
width = float(input())
height = float(input())
print('Volume for', length, width, height, "is:", calc_pyramid_volume(length, width, height))
