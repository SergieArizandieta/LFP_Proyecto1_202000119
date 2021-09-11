from tkinter import *
from tkinter import ttk
from Operaciones import purificacionExtra

def ventana():
    ventana = Tk()
    ventana.title('Proyecto 1')
    ventana.geometry("500x200")

    def sustituir():
        ventana.destroy()
        pass

    notebook = ttk.Notebook(ventana,width=490,height=160)
    notebook.grid()

    pes0 = ttk.Frame(notebook)
    pes1 = ttk.Frame(notebook)
    notebook.add(pes0,text='Cargar')
    notebook.add(pes1,text='Analizar')

    Label(pes0,text="Carga de Datos",fg="Gray",font=("Popins",12)).grid(row=0 ,column=0,sticky="w",padx=5,pady=5)
    #textoTxt = Text(pes0,width=30,height=10)
    #textoTxt.grid(row=1,column=0,sticky='nssew',padx=10,pady=1)
    botonEliminar = Button(pes0,text="Salir",command= sustituir)
    botonEliminar.grid(row=1,column=90,padx=5,pady=5)
    

    botonEnviar = Button(pes0,text="Cargar",command= purificacionExtra)
    botonEnviar.grid(row=2,column=0,padx=5,pady=5)

    
    ventana.mainloop()