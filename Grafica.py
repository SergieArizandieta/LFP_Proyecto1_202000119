from tkinter import *
from tkinter import ttk
from Operaciones import purificacionExtra
from PIL import ImageTk, Image




def ventana():
    ventana = Tk()
    ventana.title('Proyecto 1')
    ventana.geometry("1000x700")

    def sustituir():
        #ventana.destroy()
        exit()
        

    notebook = ttk.Notebook(ventana)
    notebook.pack(fill=BOTH, expand=1)

    #Pestana 1 ------------------------------------------------------------------------------------
    pes0 = ttk.Frame(notebook)

    notebook.add(pes0,text='Cargar')
  
    botonEliminar = Button(pes0,text="Salir",command= sustituir).place(x=900, y =0)
    
    Label(pes0,text="Carga de Datos",fg="Gray",font=("Popins",12)).place(x=450, y =150)
    botonEnviar = Button(pes0,text="Cargar",command= purificacionExtra).place(x=480, y =200)

    #Pestana 2 ------------------------------------------------------------------------------------
    pes1 = ttk.Frame(notebook)
    notebook.add(pes1,text='Analizar')

    imagen = ImageTk.PhotoImage(Image.open(r'./Imagenes/imagen.jpg').resize((300, 300)))   
    imagens = ImageTk.PhotoImage(Image.open(r'./Imagenes/IMG.png').resize((300, 300)))
    Texto = Label(pes1,image=imagen).place(x=500, y =305)

    def SayHi():
        Texto = Label(pes1,image=imagens).place(x=500, y =305)

     
    botonEliminar = Button(pes1,text="Salir",command= sustituir).place(x=900, y =0)

    Label(pes1,text="Visualizador",fg="Gray",font=("Popins",12)).place(x=25, y =25)
    botonOriginal = Button(pes1,text="Original",command= SayHi).place(x=80, y =100)
    botonFiltroX = Button(pes1,text="MIRRORX",command= SayHi).place(x=80, y =150)
    botonFiltroY = Button(pes1,text="MIRRORY",command= SayHi).place(x=80, y =200)
    botonFiltroDouble = Button(pes1,text="DOUBLEMIRROR",command= SayHi).place(x=80, y =250)

    #Pestana 3 ------------------------------------------------------------------------------------
    pes2 = ttk.Frame(notebook)

    notebook.add(pes2,text='Generar Reportes')
  
    botonEliminar = Button(pes2,text="Salir",command= sustituir).place(x=900, y =0)
    
    Label(pes2,text="Generar Reportes",fg="Gray",font=("Popins",12)).place(x=450, y =150)

    botonEnviar = Button(pes2,text="Generar",command= reportes).place(x=480, y =200)
    
    #Terminar ------------------------------------------------------------------------------------
    ventana.mainloop() 

def reportes():
    print("reportes")