import PySimpleGUI as sg
from PIL import Image, ImageDraw
import os
import tkinter
import io

def draw_lake():
    #im = Image.new('RGB', (500,300), (128,128,128))
    #draw = ImageDraw.Draw(im)
    #draw.rectangle((200,100,300,200), fill=(0,192,192), outline=(255,255,255))

    img = Image.open("lake.jpeg")
    img.thumbnail((1200,800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    img2 = Image.open("park.jpeg")
    img2.thumbnail((400,400))
    bio2 = io.BytesIO()
    img2.save(bio2, format="PNG")

    layout = [[[sg.Text("Lake:", font=("Arial", 25))], [sg.Image(data=bio.getvalue())]], [sg.Text("Park:", font=("Arial", 25))], [sg.Image(data=bio2.getvalue())],[sg.Button("Don't Show Me Anymore")]]
    window = sg.Window("Image", layout, size=(1200,800))


    while True:
        event, values = window.read()
        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break
    
    window.close()

draw_lake()
