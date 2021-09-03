from tkinter import filedialog, Tk

AllPatrones = []
AllTokens = []

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
        print('\n"Lectura exitosa"\n')
        return texto

#Obtiene la cadena de texto
def purificacionExtra():
    Entrada = False

    text = openExtra()
    Etiquetas = ""
    EntradaEtiqueta = ""
    for txt in text:
        #print(txt)
        if txt != " " and Entrada == False and txt != "\n" and txt != "@":
            
            if txt == "=" :
                Entrada = True
   

                for Tokens in AllTokens:
                    if Etiquetas.__eq__(Tokens): 
                        print(Etiquetas)
                        Etiquetas = ""
                        break
                
            else:
                Etiquetas+=txt


        if (txt != " " and Entrada == True) or (txt == "\n") :
            if txt != "=" :
                if txt == ";":
                    Entrada = False
                else:
                    EntradaEtiqueta+=txt
                
    print('\n\n\nOtro')
    #print(Etiquetas)
    print('\n\n\nOtro')
    #print(EntradaEtiqueta)

#Crea la tabla de tokens
def TablaTokens():
    global AllPatrones
    AllPatrones = ["(T)(I)(T)(U)(L)(O)","(A)(N)(C)(H)(O)","(A)(L)(T)(O)","(F)(I)(L)(A)(S)","(C)(O)(L)(U)(M)(N)(A)(S)","(C)(E)(L)(D)(A)(S)","(F)(I)(L)(T)(R)(O)(S)","L={a-z,A-Z} L+","D={0-9} D+","((T)(R)(U)(E))|((F)(A)(L)(S)(E))","#DDDDDDD","(M)(I)(R)(R)(O)(R)(X)|(M)(I)(R)(R)(O)(R)(Y)|(D)(O)(U)(B)(L)(E)(M)(I)(R)(R)(O)(R)"]
    global AllTokens
    AllTokens= ["TITULO","ANCHO","ALTO","FILAS","COLUMNAS","CELDAS","FILTROS","Titulo","Numero","Boolean","Color","Filtro"]
    listaTokens= []
    

    for i in range (0,12):
        aux = []
        #print(AllTokens[i])
        #print(AllPatrones[i])
        aux.append(AllTokens[i])
        aux.append(AllPatrones[i])
        listaTokens.append(aux)
        #print(aux)

    #print(listaTokens)
    #print(listaTokens[0])
    #print(listaTokens[0][0])



    