#7.1.5: Function definition: Volume of a pyramid.
#Define a function calc_pyramid_volume with parameters base_length, base_width, and pyramid_height, that 
#returns as a number the volume of a pyramid with a rectangular base.

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    calc_pyramid_volume = (base_area * pyramid_height) * (1/3)
    return calc_pyramid_volume

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')
