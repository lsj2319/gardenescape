#__main__.py
"""
File: __main__.py
----------------
Garden Escape: A relaxing time in a garden
- uses image as a game character "the gardener"
- randomly generate colors for shrubs and flowers
- plant flowers with spacebar or shrubs with a double mouse click
- move the Gardener game character with a mouse
Current status: milestone 1
"""

import tkinter

from PIL import ImageTk, Image
import random

#constants
CANVAS_WIDTH = 800      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels
CANVAS_BACKGROUND = "#51bc82"

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Garden Escape")
    #add a default background image
    bg_image = Image.open("images/bg/python-is-fun.png")
    backgroundImage=ImageTk.PhotoImage(bg_image)
    canvas.create_image(10, 10, image=backgroundImage, anchor="nw")

# event binds
    canvas.bind("<space>", lambda e: plant_flower(e, canvas))
    canvas.bind("<Double-1>", lambda e: plant_shrub(e, canvas))
    canvas.bind("<Motion>", lambda e: mouse_move(e,canvas))
    #canvas.bind("<Key>", lambda event: key_pressed(event, canvas))
    canvas.focus_set()  # Canvas now has the keyboard focus
    # print the welcome message and title of the game
    game_heading(canvas)

    canvas.mainloop()

########## functions #########
 # refactor so use a radio box and keypress to plant a flower?
def plant_flower(event, canvas):
    make_flower(canvas)

def plant_shrub(event, canvas):
    make_shrub(canvas)
# capture mouse motion events and use them
def mouse_move(e,canvas):
    #x and y coordinates move as mouse does: e.x, #e.y
    #global to prevent tkinter image bug
    global img
    #add gardener charcter image to Canvas and move with mouse
    img = ImageTk.PhotoImage(file="images/retro-gardener-sm.png")
    gardener_img = canvas.create_image(e.x, e.y, image=img, anchor="center")
    #my_label.config(text="Coordinates x:" + str(e.x) + " y:" + str(e.y))


def game_heading(canvas):
    #load the welcome and instruction text for the game
    welcome_text = canvas.create_text(400, 20, text="Welcome to Garden Escape!", fill="#f2f1f1", font=("Arial", 36))
    message_text = canvas.create_text(400, 50, text="Use your mouse to move. use spacebar to plant flowers. double click to plant shrubs.", fill="#5b5b5b")

# make a shrub
def make_shrub(canvas):
 #create a square rectangle that can be a bush. set side length and randomize color
    rect_side = 60
    color = random.choice(["#028A0F", "#369b64", "#5dbb63"])
    # shrub will be planted at mouse location
    point_x1 = (canvas.winfo_pointerx() - canvas.winfo_rootx()) - 30
    point_y1 = (canvas.winfo_pointery() - canvas.winfo_rooty()) - 30
    # create a shrub
    #canvas.create_rectangle(200, 20, SHRUB_SIZE, SHRUB_SIZE, fill=SHRUB_COLOR, outline=SHRUB_COLOR)"
    canvas.create_rectangle(point_x1, point_y1, point_x1 + rect_side, point_y1 + rect_side, fill=color, outline=color)
# make a flower
def make_flower(canvas):
# set diameter and randomize the color of the flower
    diameter = 30
    color = random.choice(['#F7EF99','#FF70A6', '#FF9770', '#70D6FF'])
    #flower (oval shape) will be planted at mouse location
    point_x1 = (canvas.winfo_pointerx() - canvas.winfo_rootx()) - 15
    point_y1 = (canvas.winfo_pointery() - canvas.winfo_rooty()) - 15
    # create the flower
    canvas.create_oval(point_x1, point_y1, point_x1 + diameter, point_y1 + diameter, fill=color, outline=color)

def start_pathway(canvas):
    #adding a pathway - work in progress
    point_x1 = canvas.winfo_pointerx() - canvas.winfo_rootx()
    point_y1 = canvas.winfo_pointery() - canvas.winfo_rooty()
    canvas.create_rectangle(point_x1, point_y1, point_x1 + 10, point_y1 + 10, fill="#DD9F6C",outline="#DD9F6C")

def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    return get_bottom_y() >= CANVAS_HEIGHT


def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]

def get_file():
    # use the default file
    filename = DEFAULT_FILE
    return filename
"""
def mouse_pressed(event, canvas):
    print('mouse pressed', event.x, event.y)
    x = event.x
    y = event.y
    found = canvas.find_overlapping(x, y, x, y)
    if len(found) > 0:
        canvas.delete(found[-1])
"""
######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1, bg="#51bc82")
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
    canvas.pack()

    return canvas




if __name__ == '__main__':
    main()
