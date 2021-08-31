from tkinter import filedialog, Tk

listData = []

ListaNames = []
listNotas= []

listParametros = []

def openExtra():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo LFP",
        initialdir = "./",
        filetypes = (
            ("archivos LFP", "*.lfp"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        print('\nNo se seleccionó ningun archivo')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print('\n"Lectura exitosa"')
        return texto

#Purificacion de los datos
def purificacionExtra():


    text = openExtra()
    titulo = ""
    textTemp = ""

    print(text)