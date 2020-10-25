"""
File: project.py
----------------
Garden Escape: A relaxing time in a garden
- use image as a game character
- randomly generate colors
- plant flowers or shrubs
- move the Gardener game character with a mouse
"""

import tkinter
from tkinter import Button
from PIL import ImageTk, Image
import random
from pynput.keyboard import Controller

#constants
CANVAS_WIDTH = 1000      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels
CANVAS_BACKGROUND = "#51bc82"

def main():
    keyboard = Controller()
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Garden Escape")
    #add a default background image
    image = Image.open("images/garden-bg-02.png")
    backgroundImage=ImageTk.PhotoImage(image)
    canvas.create_image(10, 10, image=backgroundImage, anchor="nw")

    #canvas.bind("<Button-1>", lambda e: plant_flower(e, canvas))
    #canvas.bind("<Double-1>", lambda e: plant_shrub(e, canvas))
    canvas.bind("<Motion>", lambda e: mouse_move(e,canvas))
    canvas.bind("<space>", lambda e: space_pressed(e,canvas))
    canvas.focus_set()  # Canvas now has the keyboard focus
    game_heading(canvas)
    garden_item(canvas)
   # messagebox.showinfo("Hi", "Hello Gardeners!")

    canvas.mainloop()

########## functions #########
def plant_flower():
    if space_pressed(e,canvas):
        make_flower(canvas)
# capture mouse motion events and use them
def mouse_move(e,canvas):
    #x and y coordinates move as mouse does: e.x, #e.y
    #global to prevent tkinter image bug
    global img
    #add gardener charcter image to Canvas and move with mouse
    img = ImageTk.PhotoImage(file="../images/retro-gardener-sm.png")
    gardener_img = canvas.create_image(e.x, e.y, image=img)
    #my_label.config(text="Coordinates x:" + str(e.x) + " y:" + str(e.y))

# key presses for activity ### is another function needed?
def space_pressed(e,canvas):
    # what happens? first confirm it happened
    print("spacebar pressed")

def game_heading(canvas):
    #load the welcome and instruction text for the game
    welcome_text = canvas.create_text(400, 20, text="Welcome to Garden Escape!", fill="#587732", font=("Arial", 20))
    message_text = canvas.create_text(400, 40, text="Use your mouse to move. Left click to plant flowers. double click to plant shrubs.", fill="#5b5b5b")

def garden_item(canvas):
    selected = tkinter.IntVar()
    selected.set("1")

    #tkinter.Radiobutton(canvas, text="Plant Flowers", variable=selected, value=1, bg=CANVAS_BACKGROUND, command=lambda e: clicked(e, get(selected))).place(x=850, y=20)
    tkinter.Radiobutton(canvas, text="Plant Flowers",variable=selected, value=1, bg=CANVAS_BACKGROUND).place(x=850, y=20)
    tkinter.Radiobutton(canvas, text="Place Rocks", variable=selected,  value=2, bg=CANVAS_BACKGROUND).place(x=850, y=50)
    tkinter.Radiobutton(canvas, text="Plant Shrubs", variable=selected, value=3, bg=CANVAS_BACKGROUND).place(x=850, y=80)
    tkinter.Radiobutton(canvas, text="Build Path", variable=selected, value=4, bg=CANVAS_BACKGROUND).place(x=850, y=100)

    #item_label = Label(canvas, text=selected.get())
    item_btn = Button(canvas, text="Choose activity", command=lambda: clicked(selected.get(), canvas))
    item_btn.place(x=850, y=130)


#get the radio button selection
def clicked(value, canvas):

    #item_label = Label(canvas, text = value)
    #item_label.place(x=850, y=120)
    if value ==1:
        #call flower press action which will call make_flower
           while value==1:
               plant_flower()
               p_text = canvas.create_text(400, 70, text="Let's plant flowers!", fill="#f2f1f1", font=("Arial", 16))
        # if spacebar is pressed while value is 1, make flower
        #make_flower(canvas)
    elif value == 2:
        make_rock(canvas)
    elif value == 3:
        make_shrub(canvas)
    elif value == 4:
        make_pathway(canvas)

# make a shrub
def make_shrub(canvas):
 #create a square rectangle that can be a bush. set side length and randomize color
    rect_side = 60
    color = random.choice(["#028A0F", "#369b64", "#5dbb63"])
    # shrub will be planted at mouse location
    point_x1 = canvas.winfo_pointerx() - canvas.winfo_rootx()
    point_y1 = canvas.winfo_pointery() - canvas.winfo_rooty()
    # create a shrub
    #canvas.create_rectangle(200, 20, SHRUB_SIZE, SHRUB_SIZE, fill=SHRUB_COLOR, outline=SHRUB_COLOR)"
    canvas.create_rectangle(point_x1, point_y1, point_x1 + rect_side, point_y1 + rect_side, fill=color, outline=color)


# make a rock
def make_rock(canvas):
    # set diameter and randomize the color of the flower
    #diameter = 30
    diameter = random.choice([20, 40, 60, 80, 120, 200])
    color = random.choice(['#648381', '#333333', '#999999', '#f2f1f1'])
    # rock (oval shape) will be planted at mouse location
    point_x1 = canvas.winfo_pointerx() - canvas.winfo_rootx()
    point_y1 = canvas.winfo_pointery() - canvas.winfo_rooty()
    # create the rock
    canvas.create_oval(point_x1, point_y1, point_x1 + diameter, point_y1 + diameter, fill=color, outline=color)

# make a flower
def make_flower(canvas):
# set diameter and randomize the color of the flower
    diameter = 30
    color = random.choice(['#F7EF99','#FF70A6', '#FF9770', '#70D6FF'])
    #flower (oval shape) will be planted at mouse location
    point_x1 = canvas.winfo_pointerx() - canvas.winfo_rootx()
    point_y1 = canvas.winfo_pointery() - canvas.winfo_rooty()
    # create the flower
    canvas.create_oval(point_x1, point_y1, point_x1 + diameter, point_y1 + diameter, fill=color, outline=color)

def make_pathway(canvas):
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

def mouse_pressed(event, canvas):
    print('mouse pressed', event.x, event.y)
    x = event.x
    y = event.y
    found = canvas.find_overlapping(x, y, x, y)
    if len(found) > 0:
        canvas.delete(found[-1])

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
