from math import ceil
import pygame
import sys

def validate_int_input(message):
    while True:
        try:
            userInput = int(input(message))
            return userInput
        except:
            print("Please enter an integer")

def validate_float_input(message):
    while True:
        try:
            userInput = float(input(message))
            return userInput
        except:
            print("Please enter a float")

def validate_bool_input(message):
    while True:
        userInput = input(message)
        if userInput == "True":
            return True
        elif userInput == "False":
            return False

def draw_pixel(upperCoords,sideLengths,colour):
    #for y in range(0,sideLengths[1],1):
        #for x in range(0,sideLengths[0],1):
            #screen.set_at((upperCoords[0] + x,upperCoords[1] + y),colour)
    pygame.draw.rect(screen,colour,(upperCoords[0],upperCoords[1],sideLengths[0],sideLengths[1]))

screenWidth = 1920
screenHeight = 1080

width = validate_int_input("width: ")
height = validate_int_input("height: ")
xBounds = (validate_float_input("X lower bound: "),validate_float_input("X upper bound: "))
yBounds = (validate_float_input("Y lower bound: "),validate_float_input("Y upper bound: "))
screenshotMode = validate_bool_input("Screenshot Mode (True/False): ")
if screenshotMode:
    screenshotCount = validate_int_input("Screenshot Count: ")
    iterationCount = 254
else:
    screenshotCount = 1
    iterationCount = validate_int_input("iteration count: ")

if screenWidth > screenHeight:
    xBounds = (xBounds[0] * screenWidth/screenHeight,xBounds[1] * screenWidth/screenHeight)
else:
    yBounds = (yBounds[0] * screenHeight/screenWidth,yBounds[1] * screenHeight/screenWidth)

xMagn = ceil(1920/width)
yMagn = ceil(1080/height)

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Mandelbrot Set")

for screenshot in range(255,screenshotCount,1):
    if screenshotMode:
        iterationCount += 1
        print("iteration " + str(iterationCount))

    for y in range(0,height,1):
        line = ""
        for x in range(0,width,1):

            z = complex(0,0)

            cRealPart = (xBounds[1] - xBounds[0])*x/width + xBounds[0]
            cComplexPart = (yBounds[1] - yBounds[0])*y/height + yBounds[0]
            c = complex(cRealPart,cComplexPart)

            stable = True
            for iteration in range(0,iterationCount,1):
                z = z**2 + c
                if z.real > xBounds[1] or z.real < xBounds[0] or z.imag > yBounds[1] or z.imag < yBounds[0]:
                    stable = False
                    break
            colour = (iteration+1)*255/iterationCount
            colour = (colour,colour,colour)

            if colour != (0,0,0):
                
                draw_pixel((x*xMagn,y*yMagn),(xMagn,yMagn),colour)
        pygame.display.flip()

    if screenshotMode:
        pygame.image.save(screen,"mandelbrot-iterations/" + str(iterationCount) + ".png")
