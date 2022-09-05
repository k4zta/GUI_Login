import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#A9B0B5')
        self.ventana.resizable(width=0, height=0)

        menu = Menu(self.ventana)
        self.ventana.config(menu=menu)

        Notas = Menu(menu)
        Seguimiento = Menu(menu)
        Help = Menu(menu)

        menu.add_cascade(label="Notas", menu=Notas)
        menu.add_cascade(label="Seguimiento", menu=Seguimiento)
        menu.add_cascade(label="Help", menu=Help)
        logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))
                        
        label = tk.Label( self.ventana, image=logo,bg='#A9B0B5' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        self.ventana.mainloop()