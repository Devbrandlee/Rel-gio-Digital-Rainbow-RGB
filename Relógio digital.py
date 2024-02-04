import tkinter as tk
from tkinter import font
from time import strftime
import colorsys

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

def update_rainbow_bg():
    global rainbow_index
    hue = rainbow_index / 360.0
    rgb = [int(x * 255) for x in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
    lbl.configure(background=hex_color)
    rainbow_index = (rainbow_index + 1) % 360
    lbl.after(50, update_rainbow_bg)

root = tk.Tk()
root.title("Relógio")

# Substitua o caminho abaixo pelo caminho da fonte "nome da fonte" no seu sistema
font_path = "DotGothic16\DotGothic16-Regular.ttf"

# Define a fonte com o tamanho desejado
font_style = ('DotGothic16', 55, 'bold') 

lbl = tk.Label(root, font=font_style, foreground='white')
lbl.pack(anchor='center')

rainbow_index = 0
update_rainbow_bg()
time()

root.mainloop()
