import grafo_anthony as grafo
import anthony_alg as algoritmo
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import Tk, Label, Button, Frame, PhotoImage
from tkinter.ttk import *
from tkinter.font import Font
from tkinter.constants import CENTER, SE

def ventana1():
    global ventana1
    ventana1 = Tk()
    ventana1.title("Corredor Municipal from UPC")
    
    ancho_pantalla = ventana1.winfo_screenwidth()
    altura_pantalla = ventana1.winfo_screenheight()

    x = int(ancho_pantalla / 2 - 800 / 2)
    y = int(altura_pantalla / 2 - 600 / 2)

    ventana1.geometry("800x600+{}+{}".format(x, y))
    
    imagen = PhotoImage(file = "pictures/corredor.png")
    label_fondo = Label(ventana1, image = imagen)
    label_fondo.pack()
    
    contenedor = Frame(ventana1)
    contenedor.pack(ipadx=10, ipady=10)  
    contenedor.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    titulo = Label(contenedor, text="CORREDOR", font = Font(family="Bahnschrift SemiBold Condensed", size=30, weight="normal", slant="roman", underline=0, overstrike=0))
    titulo.pack(pady=10)  
    
    subtitulo = Label(contenedor, text="Le presentamos todas nuestras rutas", font = Font(family="Bahnschrift Light Condensed", size=12, weight="normal", slant="roman", underline=0, overstrike=0))
    subtitulo.pack(pady=10)
    
    boton_mostrarG = Button(contenedor, text = "Mostrar Grafo", command = ventana_grafo)
    boton_mostrarG.pack(pady=10)
    
    subtitulo = Label(contenedor, text="Aplicaremos los algoritmos", font = Font(family="Bahnschrift Light Condensed", size=12, weight="normal", slant="roman", underline=0, overstrike=0))
    subtitulo.pack(pady=0.3)
    subtitulo = Label(contenedor, text="Porfavor elija si cuenta con tarjeta o no", font = Font(family="Bahnschrift Light Condensed", size=12, weight="normal", slant="roman", underline=0, overstrike=0))
    subtitulo.pack(pady=10)

    combo1 = Combobox(contenedor)
    combo1['values']=("Con Tarjeta","Sin Tarjeta")
    combo1.current(0)
    combo1.pack(pady=10)
    
    boton_aceptar = Button(contenedor, text="Aceptar", command = ventana2)
    boton_aceptar.pack(pady=10)
    
    def cerrar_ventana():
        ventana1.destroy()
    
    boton_salir = Button(ventana1, text="Salir", command = cerrar_ventana)
    boton_salir.place(relx=1.0, rely=1.0, anchor=SE)
    
    ventana1.mainloop()  

def ventana2():
    global ventana2
    ventana2 = Toplevel(ventana1)
    ventana2.title("Corredor Municipal from UPC")
        
    ancho_pantalla = ventana2.winfo_screenwidth()
    altura_pantalla = ventana2.winfo_screenheight()

    x = int(ancho_pantalla / 2 - 800 / 2)
    y = int(altura_pantalla / 2 - 600 / 2)

    ventana2.geometry("800x600+{}+{}".format(x, y))
    
    imagen = PhotoImage(file = "pictures/corredor.png")
    label_fondo = Label(ventana2, image = imagen)
    label_fondo.pack()

    contenedor = Frame(ventana2)
    
    titulo = Label(contenedor, text="ELIJA LA RUTA", font = Font(family="Bahnschrift SemiBold Condensed", size=16, weight="normal", slant="roman", underline=0, overstrike=0))
    titulo.pack(pady=10)  
    
    subtitulo = Label(contenedor, text="Inicio", font = Font(family="Bahnschrift Light Condensed", size=12, weight="normal", slant="roman", underline=0, overstrike=0))
    subtitulo.pack(pady=10)

    text1 = Entry(contenedor)
    text1.pack(pady=10)  

    subtitulo2 = Label(contenedor, text="Final", font = Font(family="Bahnschrift Light Condensed", size=12, weight="normal", slant="roman", underline=0, overstrike=0))
    subtitulo2.pack(pady=10)  

    text2 = Entry(contenedor)
    text2.pack(pady=10)
    
    subtitulo3 = Label(contenedor, text="Elija el algoritmo que desea ejecutar", font = Font(family="Bahnschrift Light Condensed", size=12, weight="normal", slant="roman", underline=0, overstrike=0))
    subtitulo3.pack(pady=10)  
    
    #RadioButton    
    def seleccionar_algoritmo():
        seleccion = opcion.get()
        if seleccion == "Algoritmo_A":
            ventana_A(_origen = text1.get(), _destino = text2.get())
        elif seleccion == "Algoritmo_B":
            ventana_B(_origen = text1.get(), _destino = text2.get())
            
    opcion = StringVar()

    radio_a = Radiobutton(contenedor, text="Algoritmo A", variable = opcion, value = "Algoritmo_A")
    radio_a.pack()

    radio_b = Radiobutton(contenedor, text="Algoritmo B", variable = opcion, value = "Algoritmo_B")
    radio_b.pack()
    
    #Button
    boton_mostrar = Button(contenedor, text="Mostrar Ruta", command=seleccionar_algoritmo)
    boton_mostrar.pack(pady=10)     
    
    contenedor.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    boton_volver = Button(ventana2, text="volver", command = volver_ventana1)
    boton_volver.place(relx=1.0, rely=1.0, anchor=SE)
    
    if(ventana2):
        ventana1.withdraw()

    ventana2.mainloop()
    
def ventana_A(_origen, _destino):
    camino, distancia = algoritmo.mi_grafo.BFS(_origen, _destino)
    #grafo.dibujar_BFS(camino)
    global ventana_A
    ventana_A = Toplevel(ventana2)
    ventana_A.title("Corredor Municipal from UPC")
    ancho_pantalla = ventana_A.winfo_screenwidth()
    altura_pantalla = ventana_A.winfo_screenheight()

    x = int(ancho_pantalla / 2 - 800 / 2)
    y = int(altura_pantalla / 2 - 600 / 2)

    ventana_A.geometry("800x600+{}+{}".format(x, y))
    
    titulo1 = Label(ventana_A, text=f"La ruta para llegar al destino es de :{camino}, con una distancia de {distancia} km", font=("Arial", 8), justify= "center")
    titulo1.place(relx=0.1, rely=0.1, anchor=NW)
    
    imagen = PhotoImage(file = grafo.dibujar_BFS(camino))
    imagen_redimensionada = imagen.subsample(3, 3)
    #imagen redimensionada
    label_fondo = Label(ventana_A, image=imagen_redimensionada)
    label_fondo.place(relx=0.5, rely=0.5, anchor=CENTER)

    #BOTONES    
    boton_volver = Button(ventana_A, text="volver", command = volver_ventana2A)
    boton_volver.place(relx=1.0, rely=1.0, anchor=SE)
    
    if(ventana_A):
        ventana2.withdraw()
    
    ventana_A.mainloop()
    
def ventana_B(_origen, _destino):
    camino, precios = algoritmo.mi_grafo.PRIM(_origen, _destino)
    _camino = []
    
    for (i, j) in camino:
        _camino.append(i)
    
    global ventana_B
    ventana_B = Toplevel(ventana2)
    ventana_B.title("Corredor Municipal from UPC")
    
    ancho_pantalla = ventana_B.winfo_screenwidth()
    altura_pantalla = ventana_B.winfo_screenheight()

    x = int(ancho_pantalla / 2 - 800 / 2)
    y = int(altura_pantalla / 2 - 600 / 2)

    ventana_B.geometry("800x600+{}+{}".format(x, y))
    
    titulo2 = Label(ventana_B, text=f"La ruta para llegar al destino es de :{_camino}, con un precio total de s/. {precios}", font=("Arial", 8), justify= "center")
    titulo2.place(relx=0.1, rely=0.1, anchor=NW)
    
    imagen = PhotoImage(file = grafo.dibujar_Prim(camino))
    imagen_redimensionada = imagen.subsample(3, 3)
    #imagen redimensionada
    label_fondo = Label(ventana_B, image=imagen_redimensionada)
    label_fondo.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    boton_volver = Button(ventana_B, text="volver", command = volver_ventana2B)
    boton_volver.place(relx=1.0, rely=1.0, anchor=SE)
    
    if(ventana_B):
        ventana2.withdraw()
    
    ventana_B.mainloop()
    
def ventana_grafo():
    global ventana_grafo
    ventana_grafo = Toplevel(ventana1)
    ventana_grafo.title("Corredor Municipal from UPC")
    ancho_pantalla = ventana_grafo.winfo_screenwidth()
    altura_pantalla = ventana_grafo.winfo_screenheight()

    x = int(ancho_pantalla / 2 - 800 / 2)
    y = int(altura_pantalla / 2 - 600 / 2)

    ventana_grafo.geometry("800x600+{}+{}".format(x, y))
    
    imagen = PhotoImage(file = "pictures/grafos/grafo_Estación 1_temp.png")#grafo_Estación 1_temp
    imagen_redimensionada = imagen.subsample(2, 2)
    #imagen redimensionada
    label_fondo = Label(ventana_grafo, image=imagen_redimensionada)
    label_fondo.pack()
     
    if(ventana_grafo):
        ventana1.withdraw()
    boton_volver = Button(ventana_grafo, text="volver", command = volver_de_grafo)  
    boton_volver.place(relx=1.0, rely=1.0, anchor=SE)
    boton_volver2 = Button(ventana_grafo, text="zoom", command = zoom)  
    boton_volver2.place(relx=1.0, rely=0.95, anchor=SE)
    
    ventana_grafo.mainloop()
    
def zoom():
    grafo.dibujar_grafo()
    
    
def volver_ventana1():
    ventana1.iconify()
    ventana1.deiconify()
    ventana2.destroy()

def volver_de_grafo():
    ventana1.iconify()
    ventana1.deiconify()
    ventana_grafo.destroy()
    
def volver_ventana2A():
    ventana2.iconify()
    ventana2.deiconify()
    ventana_A.destroy()
    
def volver_ventana2B():
    ventana2.iconify()
    ventana2.deiconify()
    ventana_B.destroy()
        
ventana1()