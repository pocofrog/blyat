from tkinter import *
import webbrowser

def open_link():
     webbrowser.open('https://youtu.be/wh9QLjk3M2k?si=FoMZwG5Zzq12Dl65')


okoshko = Tk()

original_photo = PhotoImage(file='chipichapa.png')

zoom_factor = 5
resized_photo = original_photo.zoom(zoom_factor, zoom_factor)

background_label = Label(okoshko, image=resized_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

okoshko.geometry("400x400")
okoshko.title("Bane")

icon = PhotoImage(file='PIWO.png')
okoshko.iconphoto(True, icon)

button = Button(okoshko, text="Click me!", command=open_link)
button.pack()

okoshko.mainloop()