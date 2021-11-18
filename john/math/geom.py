"""
Provide routines for geometry

Blah blah blah
"""
import math

PI = math.pi

ANIMAL = "wombat"

def circle_area(diameter):
    """
    Calculate the area of a circle, given the diameter

    :param diameter: Diameter of the circle
    :return: Area of circle is same units as diameter
    """
    radius = diameter / 2
    return math.pi * radius ** 2

def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    :param length: Length of rectangle
    :param width: Width of rectangle
    :return: Area of rectangle in same units as length and width.
    """
    return length * width

def square_area(length):
    """
    Calculate area of square given length of one side.

    :param length: Length of a side
    :return: Area of square.
    """
    return rectangle_area(length, length)

def _secret():  # private
    print("shhhhh")


