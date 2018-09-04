from tkinter import *
import astar

def event(event):
    if event.keysym == "Up":
        a_star.up()
    elif event.keysym == "Down":
        a_star.down()
    elif event.keysym == "Left":
        a_star.left()
    else:
        a_star.right()

if __name__ == "__main__":
    width, height = 800, 800
    rows, cols = 20, 20

    root = Tk()
    root.geometry("{}x{}".format(width, height))

    canvas = Canvas(root, width=width, height=height)
    canvas.pack()

    a_star = astar.AStar(root, canvas, width, height, rows, cols)

    root.bind("<Up>", event)
    root.bind("<Down>", event)
    root.bind("<Left>", event)
    root.bind("<Right>", event)

    root.after(0, a_star.run())
    root.after(0, a_star.keep_window())
    root.mainloop()