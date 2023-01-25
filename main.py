import turtle
import pandas as pd

# Declaring Objects
screen = turtle.Screen()
screen.title("Your Screen Title Here")
screen.addshape("blank_states_img.gif")
image = turtle.Turtle(shape="blank_states_img.gif")

# Declaring lists of coordinates
x_axis = []
y_axis = []


# Defining the function used to get the x,y coordinates from mouse click
def get_mouse_click_coordinates(x, y):
    print(x, y)
    x_axis.append(x)
    y_axis.append(y)


# Defining the function used to create the csv file after finishing collecting points
def create_csv():
    screen.bye()
    df = pd.DataFrame(list(zip(x_axis, y_axis)), columns=["x_axis", "y-axis"])
    df.to_csv("coordinates.csv")


screen.onscreenclick(get_mouse_click_coordinates)


screen.listen()
screen.onkeypress(create_csv, key="Escape")
screen.mainloop()

