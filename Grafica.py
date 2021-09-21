
from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image
from Operaciones import purificacionExtra
from CrearImagenes import *
import main
import Operaciones as Op
from reportes import *
Nombre = ""

imgOriginal= './IMG_Programa/auxiliar.png'
imgMirrorx= './IMG_Programa/auxiliar.png'
imgMirrory= './IMG_Programa/auxiliar.png'
imgMirrorDouble= './IMG_Programa/auxiliar.png'

opcion = []
def ventanas():
    try:
        global imgOriginal
        global imgMirrorx
        global imgMirrory
        global imgMirrorDouble
        

        ventana = Tk()
        ventana.title('Proyecto 1')
        ventana.geometry("1000x700")

        def cerrar():
            exit()

        def sustituir():
            global Nombre
            Nombre = ImagenesCombo.get()
            textLabel['text'] = "Visualizando: " + ImagenesCombo.get()
            listado =  Op.lista_e.buscar(ImagenesCombo.get())

            definir(listado)
            ventana.destroy()
            destruir()
            #ventanas
            
        notebook = ttk.Notebook(ventana)
        notebook.pack(fill=BOTH, expand=1)

        pes0 = ttk.Frame(notebook)
        notebook.add(pes0,text='Cargar')

        pes1 = ttk.Frame(notebook)
        notebook.add(pes1,text='Analizar')

        #Pestana 1 ------------------------------------------------------------------------------------
        Button(pes0,text="Salir",command= cerrar).place(x=900, y =0)

        def data():
            try: 
                purificacionExtra()
                global opcion
                opcion = Op.lista_e.OptenerNames()
                combobox()
            except Exception:
                print("Error, v")
        
        Label(pes0,text="Carga de Datos",fg="Gray",font=("Popins",12)).place(x=450, y =150)
        Button(pes0,text="Cargar",command= data).place(x=480, y =200)

        #Pestana 2 ------------------------------------------------------------------------------------
        text = "Visualizador"
        Button(pes1,text="Salir",command= cerrar).place(x=900, y =0)
        Label(pes1,text="Seleccione una imagen",fg="Gray",font=("Popins",12)).place(x=250, y =25)

        print(imgOriginal, "IMGORIGINAL")


       

        imgOriginal = ImageTk.PhotoImage(Image.open(imgOriginal).resize((500, 500)))
        imgMirroX = ImageTk.PhotoImage(Image.open(imgMirrorx).resize((500, 500)))
        imgMirroY = ImageTk.PhotoImage(Image.open(imgMirrory).resize((500, 500)))
        imgMirroDOUBLE = ImageTk.PhotoImage(Image.open(imgMirrorDouble).resize((500, 500)))
        
        lblimg = Label(pes1)
        lblimg['image'] =  imgOriginal
        lblimg.place(x=300, y =105)

        ImagenesCombo = ttk.Combobox(pes1, width = 27,state="readonly")
        ImagenesCombo.pack( padx=0, pady=50)
        ImagenesCombo.current()
        global opcion
        ImagenesCombo['values'] = opcion
    
        textLabel = Label(pes1,fg="Gray",font=("Popins",12))
        textLabel['text'] = text
        textLabel.place(x=10, y =25)
            
        def Original():
            lblimg['image'] = imgOriginal
            
        def MirrorX():
            lblimg['image'] = imgMirroX

        def MirrorY():
            lblimg['image'] = imgMirroY

        def MirrorDouble():
            lblimg['image'] = imgMirroDOUBLE

        def combobox():
            global opcion
            ImagenesCombo['values'] = opcion
        Button(pes1,text="Cargar",command= sustituir).place(x=445, y =77)
        Button(pes1,text="Original",command= Original).place(x=80, y =100)
        Button(pes1,text="MIRRORX",command= MirrorX).place(x=80, y =150)
        Button(pes1,text="MIRRORY",command= MirrorY).place(x=80, y =200)
        Button(pes1,text="DOUBLEMIRROR",command= MirrorDouble).place(x=80, y =250)

        #Pestana 3 ------------------------------------------------------------------------------------
        
        
        pes2 = ttk.Frame(notebook)

        notebook.add(pes2,text='Generar Reportes')
    
        Button(pes2,text="Salir",command= cerrar).place(x=900, y =0)
        
        Label(pes2,text="Generar Reportes",fg="Gray",font=("Popins",12)).place(x=450, y =150)

        Button(pes2,text="Generar",command= reportes).place(x=480, y =200)
        
        #Terminar ------------------------------------------------------------------------------------
    
        ventana.mainloop() 
    except Exception:
       
        print("Error, v")

def reportes():
    ReporteTokens()
    ReporteTErrores()
    print("reportes")

def destruir():
    main.abrir_ventana()

def definir(listado):

    
    global imgOriginal
    global imgMirrorx
    global imgMirrory
    global imgMirrorDouble
    print(listado)
     
    imgOriginal= listado[0]
    imgMirrorx=  listado[1]
    imgMirrory=  listado[2]
    imgMirrorDouble=  listado[3]

    """ imgOriginal = './IMG_generada/Cubo_ORIGINAL.png'
    imgMirrorx= './IMG_generada/Cubo_MIRRORX.png'
    imgMirrory= './IMG_generada/Cubo_MIRRORY.png'
    imgMirrorx= './IMG_generada/Cubo_DOUBLE.png'"""