from tkinter import filedialog, Tk

TablaDeTokens = []

def openExtra():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo PXLA",
        initialdir = "./",
        filetypes = (
            ("archivos LFP", "*.pxla"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        print('\nNo se seleccionó ningun archivo')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        #print('\n"Lectura exitosa"')
        return texto

#Purificacion de los datos
def purificacionExtra():


    text = openExtra()
    titulo = ""
    textTemp = ""

    print(text)


def TablaTokens():
    TokensReservados = ["TITULO","ANCHO","ALTO","FILAS","COLUMNAS","CELDAS","FILTROS"]
    ReservadosPatron = [["(T)(I)(T)(U)(L)(O)","(A)(N)(C)(H)(O)","(A)(L)(T)(O)","(F)(I)(L)(A)(S)","(C)(O)(L)(U)(M)(N)(A)(S)","(C)(E)(L)(D)(A)(S)","(F)(I)(L)(T)(R)(O)(S)"]]
    Tokens = [["Titulo","Numero","Boolean","Color","Filtro"]]
    TokensPatron = [["L={a-z,A-Z} L+","D={0-9} D+","((T)(R)(U)(E))|((F)(A)(L)(S)(E))","#DDDDDDD","(M)(I)(R)(R)(O)(R)(X)|(M)(I)(R)(R)(O)(R)(Y)|(D)(O)(U)(B)(L)(E)(M)(I)(R)(R)(O)(R)"]]

    AllPatrones = ["(T)(I)(T)(U)(L)(O)","(A)(N)(C)(H)(O)","(A)(L)(T)(O)","(F)(I)(L)(A)(S)","(C)(O)(L)(U)(M)(N)(A)(S)","(C)(E)(L)(D)(A)(S)","(F)(I)(L)(T)(R)(O)(S)","L={a-z,A-Z} L+","D={0-9} D+","((T)(R)(U)(E))|((F)(A)(L)(S)(E))","#DDDDDDD","(M)(I)(R)(R)(O)(R)(X)|(M)(I)(R)(R)(O)(R)(Y)|(D)(O)(U)(B)(L)(E)(M)(I)(R)(R)(O)(R)"]
    AllTokens= ["TITULO","ANCHO","ALTO","FILAS","COLUMNAS","CELDAS","FILTROS","Titulo","Numero","Boolean","Color","Filtro"]
    listaTokens= []
    
    """ for lista in TokensReservados:
        #print(lista)
        listaTokens.append(lista)"""
                        
    print("///////////////////////////////")

    """for lista in ReservadosPatron:
        #print(lista)
        listaTokens.append(lista)"""

    print("///////////////////////////////")
    for lista in listaTokens:
        print(lista)
         
    print("///////////////////////////////")
    #print(listaTokens)
    #print(AllTokens[0])

    for i in range (0,12):
        aux = []
        #print(AllTokens[i])
        #print(AllPatrones[i])
        aux.append(AllTokens[i])
        aux.append(AllPatrones[i])
        listaTokens.append(aux)
     
        #print(aux)

    print(listaTokens)



    
