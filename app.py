import os
import math
import pygame as py

path = os.path.abspath("")

original = py.image.load(path)

width = original.get_width()
height = original.get_height()

#Determines the ratio of how many squares width to height of the given image size
def square_ratio(width, height):

    if width > height: 
        ratio = round(width/height,1)
    else: 
        ratio = round(height/width, 1)
    
    return ratio

#Calculates the common factor of the ratio, assuming the ratio is x by 10 squares
def common_factor(ratio):
    previous_rem = None
    current_rem = None
    num = ratio*10
    den = 10

    while current_rem != 0:
        current_rem = num%den
        if current_rem == 0: 
            return previous_rem
        num = den
        den = current_rem
        previous_rem = current_rem

#Determines the total number of minimum squares, if a common factor exists in the ratio, then it will reduce the amount of squares accordingly
def num_squares(common_factor, ratio):
    total_squares = ((ratio*10)/common_factor)*(10/common_factor)
    print(f"square by square: {(ratio*10)/common_factor,(10/common_factor) }")
    
    return total_squares

#Calculates the total number of squares
def square_size(num_squares, width, height):
    area = width*height
    square_size = area/num_squares
    return square_size

#Draws the grid on the image
def draw_grid(square_size):
    pass

def main():
    w = 1920
    h = 1080
    ratio = square_ratio(w, h)
    print(f"ratio: {ratio}")
    print(f"common factor: {common_factor(ratio)}")
    print(f"total squares: {num_squares(common_factor(ratio), ratio)}")

main()