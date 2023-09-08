import os
import math
import pygame as py

#Determines the ratio of squares for the width and height of the given image size
def square_ratio(width, height):

    if width > height: 
        ratio = round(width/height,1)
    else: 
        ratio = round(height/width, 1)
    
    return ratio

#Calculates the common factor of the ratio
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
    total_squares = [((ratio*10)/common_factor),(10/common_factor)]
    
    return total_squares

#Calculates the total number of squares
def square_size(num_sqr, width, height):
    area = width * height
    square = area / (num_sqr[0]*num_sqr[1])
    len_sqr = math.sqrt(square)
    
    return len_sqr


def main():
    #ADD PATH OF IMAGE IN "INSERT PATH HERE"
    path = os.path.abspath("INSERT PATH HERE")
    original = py.image.load(path)

    #Gets dimensions of image
    width = original.get_width()
    height = original.get_height()

    #Gets information of image including square ratio, common factor of ratio, number of squares, and size of square
    ratio = square_ratio(width, height)
    com_factor = common_factor(ratio)
    num_sqr = num_squares(com_factor, ratio)
    sqr_size = square_size(num_sqr, width, height)

    print(f"Ratio: {ratio}, common facotr: {com_factor}, number of squares: {num_sqr}, size of squares: {sqr_size}")

    #Initializes pygame screen and adds image to screen
    py.init()
    screen = py.display.set_mode((width,height))
    screen.blit(original, (0,0))
    
    x_cor = sqr_size
    y_cor = sqr_size

    #Sets up for loops for whichever side of the image is longer
    if height > width:
        horizontal = int(num_sqr[1])
        vertical = int(num_sqr[0])
    else:
        horizontal = int(num_sqr[0])
        vertical = int(num_sqr[1])      

    #Draws horizontal lines on image
    for i in range(1, horizontal):
        py.draw.line(screen, (255,0,0), (x_cor,height), (x_cor,0), 3)
        x_cor += sqr_size
    
    #Draws vertical lines on image
    for j in range(1, vertical):
        py.draw.line(screen, (0,0,255), (0, y_cor), (width, y_cor), 3)
        y_cor += sqr_size

    #Updates screen with new linse
    py.display.flip()

    #ADD PATH OF UPDATED IMAGE IN "INSERT PATH HERE"
    py.image.save(screen, "INSERT PATH HERE")


main()