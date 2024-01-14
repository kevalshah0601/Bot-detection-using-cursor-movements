import subprocess
from tkinter import Tk, Label, Button

def execute_tasks(mode):
    if mode == "Human":
        subprocess.run(['make', 'run-human'])
    elif mode == "Robot":
        subprocess.run(['make', 'run-robot'])
    else:
        print("Invalid mode.")

def on_button_click(mode, root):
    execute_tasks(mode)
    root.destroy()

def center_window(root, width, height):

    screen_width = 1920
    screen_height = 1080

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

def run_mode():
    root = Tk()
    root.title("Select Mode")

    window_width = 300
    window_height = 150
    center_window(root, window_width, window_height)

    label = Label(root, text="Which mode do you want to test?")
    label.pack()

    button_human = Button(root, text="Human", command = lambda: on_button_click("Human", root))
    button_human.pack()

    button_robot = Button(root, text="Robot", command = lambda: on_button_click("Robot", root))
    button_robot.pack()

    root.mainloop()

run_mode()