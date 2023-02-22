import math

from area import area_formula

# volume of sphere = 4/3 pi * radius3

def volume_of_sphere(radius):
    output=4/3*math.pi*radius*radius*radius
    return output


# volume of a pyramid  = ⅓ A × H

def volume_of_pyramid(base,height):
    output=(base*height)/3
    return output


# volume of a cube = length*breadth*height

def volume_of_cube(length,breadth1,height1):
    output=(length*breadth1*height1)
    return output


# volume of a cylinder = pi * radius2 * height
def volume_of_cylinder(rad,hei):
    output=(rad*rad*hei)*math.pi
    return output


#volume of traingular pyramid = 1/3 x Area of triangular base(1/2 b*h) x Height of pyramid
# used area_formula file to compute the volume of traingle part in triangular pyramid
def volume_of_tpyramid(triangular_base,triangular_height,height_pyramid):
    area_triangular_base=area_formula.area_of_triangle(triangular_base,triangular_height)
    output=1/3*area_triangular_base*height_pyramid
    return output


