import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tkinter import Tk, Label, Button
from keras.models import load_model
import matplotlib.pyplot as plt

def read_int(filename):
    integers = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.strip().split()
            integers.extend([int(num) for num in numbers])
    return integers

def center_window(root, width, height):

    screen_width = 1920
    screen_height = 1080

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

def show_prediction():
    loaded_model = load_model('model_folder/cursor_model')
    x_cord = read_int('x_test.txt')
    y_cord = read_int('y_test.txt')
    x_final = []
    for i in range(len(x_cord)):
        temp = []
        temp.append(x_cord[i])
        temp.append(y_cord[i])
        x_final.append(temp)

    prediction = loaded_model.predict([x_final])
    prediction = prediction[0]

    if prediction > 0.5:
        result = f"Robot with a probability of {prediction*100} %"
    else:
        result = f"Human with a probability of {(1-prediction)*100} %"

    output_label.config(text=result)

    predict_button.destroy()
    close_button = Button(root, text="Close", command=root.destroy)
    close_button.pack()

    x_axis = x_cord
    y_axis = []
    for i in y_cord:
        y_axis.append(1079-i)

    plt.plot(x_axis, y_axis, label = 'Cursor Movement')
    plt.xlim(0,1920)
    plt.ylim(0,1080)
    plt.show()

root = Tk()
root.title("Cursor Prediction")

window_width = 300
window_height = 150
center_window(root, window_width, window_height)

output_label = Label(root, text = "Movement Prediction")
output_label.pack()

predict_button = Button(root, text = "Predict", command = show_prediction)
predict_button.pack()

root.mainloop()
