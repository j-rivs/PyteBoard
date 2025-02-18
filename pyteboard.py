import tkinter as tk
from tkinter.colorchooser import askcolor



"""Functions and Event Handling"""

# function to handle the action of drawing in the GUI
def start_drawing(event): # defines out start_drawing function and specifies it will take an event as an argument
    global is_drawing, prev_x, prev_y # declares the 3 global variables
    is_drawing = True # set variable to true to indicate a drawing action is in progress
    prev_x, prev_y = event.x, event.y # captures current mouse cursor coordinates when the function is called and assigns x & y to their prev variables. These variables track the starting point of the draw action

# function for drawing onto the whiteboard canvas
def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing: # checks if the is_drawing function is currently active/true
        current_x, current_y = event.x, event.y # creates current values or x & y based on their event values
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True) # creates a line between the previous and current x & y event positions and sets the color, line width, style, and smooths it out
        prev_x, prev_y = current_x, current_y # sets the previous coordinates to the current coordinates, setting up the function to move/draw progressively

# create a function to call when the drawing / mouse event is finished
def stop_drawing(event):
    global is_drawing
    is_drawing = False # set the global to false to end the drawing event


# calling th askcolor module to implement color selection
def change_pen_color():
    global drawing_color # define the drawing color as a global var
    color = askcolor()[1] # call the askcolor funtion to ask the user to select a color, visually, and returns an RGB or hexidecimal string. Returns None if cancelled
    if color: # if True for color
        drawing_color = color # set the drawing color to the color value from askcolor

# function for controlling the line width of the pen
def change_line_width(value): # define function with a value taken as the arg
    global line_width
    line_width = int(value) # change the line width to the int typecast value



"""
Building GUI
- title app
- blank white canvas for drawing
- frame to hold app controls
- color selection button
- clear canvas button
- slider for line width selection
"""



"""Window and Canvas Creation"""

# create the white canvas for the whiteboard
root = tk.Tk() # creates main app window by assigning the Tkinter app initialization to variable root. Window contains the graphical elements
root.title("Pyteboard") # adds a title to the application window

canvas = tk.Canvas(root, bg="white") # Assigns the created drawing canvas within the app window to the canvas variable. Sets white background.
canvas.pack(fill="both", expand=True) # configure canvas to fill all vert and hori space + allowing it to expand to fill the window

is_drawing = False # initializes is_drawing to false, it can then be used to track whether drawing is occurring
drawing_color = "black" # specifies the color used to draw on the canvas
line_width = 2 # specifies the line width used to draw

root.geometry("800x600") # sets the initial size of the root/canvas. This can be adjusted after the window launches



"""Navbar and Controls"""

# create frame to hold buttons or controls
controls_frame = tk.Frame(root) # assigns a frame within root to the controls_frame variable
controls_frame.pack(side="top", fill="x") # 'packs' a widget within the parent widget that is on the top side and expands with the frame along x

# create 2 buttons with default positions within the screen
color_button = tk.Button(controls_frame, text="Change Color", command=change_pen_color) # create the color button within the controls frame, with name text, and using the change_pen_color function
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all")) # create the clear canvas button with a lambda function passthrough on command to delete elements on the canvas

color_button.pack(side="left", padx=5, pady=5) # set color button to default left side with 5 padding on x & y. Configures the widgets place within the control_frame
clear_button.pack(side="left", padx=5, pady=5) # configures the widgets place within the control_frame

# create slider for line width control
line_width_label = tk.Label(controls_frame, text="Line Width: ") # create a label widget for line width in the control frame, gives it a name, and save it to a var
line_width_label.pack(side="left", padx=5, pady=5) # configures the widgets place within the control_frame

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val)) # creates a horizontal scale widget that lets the user select line width on a scale from 1 to 10. Command is set to call the change_line_wdith function with the selected lue whenever the slider position is changed
line_width_slider.set(line_width) # Sets the initial position of the slider to the value stored in line_width (initialized earlier)
line_width_slider.pack(side="left", padx=5, pady=5) # configures the widgets place within the control_frame



"""Connect Features to GUI"""

# bind/link coded functions with buttons and controls
canvas.bind("<Button-1>", start_drawing) # begins start_drawing function when the left mouse button is clicked
canvas.bind("<B1-Motion>",draw) # while left mouse button is held, triggers draw function on the canvas
canvas.bind("<ButtonRelease-1>", stop_drawing) # when the left mouse button is released (button release event) triggers the stop_drawing function


root.mainloop() # .mainloop keeps the window running until exited by the user (or crashes)