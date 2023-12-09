import math
from tkinter import *

HEIGHT = 400
WIDHT = 400

def center_window(width, height):
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    top.geometry('%dx%d+%d+%d' % (width, height, x, y))


top = Tk()
C = Canvas(top, bg="black", height=HEIGHT, width=WIDHT)


def draw():
    start_x, start_y = 200, 200
    end_x, end_y = 200, 100

    # Calculate differences
    dx = end_x - start_x
    dy = end_y - start_y

    # Angle in degrees and radians
    angle_degrees = 70
    angle_radians = math.radians(angle_degrees)

    # Apply rotation
    new_dx = dx * math.cos(angle_radians) - dy * math.sin(angle_radians)
    new_dy = dx * math.sin(angle_radians) + dy * math.cos(angle_radians)

    # Calculate new end point
    new_end_x = start_x + new_dx
    new_end_y = start_y + new_dy

    # Draw the rotated line
    line = C.create_line(start_x, start_y, new_end_x, new_end_y, fill='white')



draw()
C.pack()

center_window(400, 400)


top.mainloop()
