# Importacion de las libreias.
from tkinter import *

#Create & Configure root 
root = Tk()
Grid.rowconfigure(root, 0, weight=10)
Grid.columnconfigure(root, 0, weight=10)
root.geometry("500x500")
#Create & Configure frame 
frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)
indice = 0
#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(8):
    Grid.rowconfigure(frame, row_index, weight=10)
    for col_index in range(8):
        Grid.columnconfigure(frame, col_index, weight=10)
        if row_index == 0:
            btn = Button(frame, text = col_index) #create a button inside frame
        elif col_index == 0:
            btn = Button(frame, text = indice)
            indice +=1
        else:
            btn = Button(frame) #create a button inside frame 
        btn.grid(row = row_index, column = col_index, sticky = N+S+E+W)

root.mainloop()