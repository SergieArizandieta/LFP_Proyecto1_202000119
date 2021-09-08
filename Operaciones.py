from tkinter import filedialog, Tk
from ListaSimple import *

lista_e = lista_enlazada()

PalabrasReservadas = []
Tokens = []
Errores = []
Asignar = True

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
        texto += "~"
        return texto

#Obtiene la cadena de texto
def purificacionExtra():
    verificacion = True
    errortipo=""

    estado = 0
    txtTemp = ""
    columna = 1
    fila = 1
    opcion = True

    text = openExtra()
    #print(text)

    for txt in text:
        opcion = True
        while opcion != False:
            if estado == 0:
                verificacion = True
                if isLetra(txt):
                    txtTemp += txt
                    estado =1
                    opcion = False

                elif isNumero(txt):
                    txtTemp += txt
                    estado =4
                    opcion = False

                elif ord(txt) == 35: # #
                    txtTemp += txt
                    estado = 5
                    opcion = False

                elif isSimbolo(txt): 
                    txtTemp += txt    
                    estado = 2

                elif ord(txt) == 34: # "
                    txtTemp += txt
                    estado = 3
                    opcion = False

                elif ord(txt) == 64: # @
                    txtTemp += txt
                    estado = 6
                    opcion = False

                else:

                    if ord(txt) == 32 or ord(txt) == 10 or ord(txt) == 9 or txt == '~':
                        
                        opcion = False
                        pass
                    else: 
                        print("Error Lexico, se detecto " + txt + " en S0  F: " + str(fila) + ", C: " + str(columna))
                        errortipo= 'Caracter inesperado, esperaba L|D|#|S|"|@' 
                        errortemp =[]
                        errortemp.append(txt)
                        errortemp.append(errortipo)
                        errortemp.append(fila)
                        errortemp.append(columna)
                        Errores.append(errortemp)
                        
                        opcion = False

            elif estado == 1:
                opcion = False
                if (isLetra(txt)):
                    txtTemp += txt
                    estado = 1
                
                elif (ord(txt) == 95 ): # _
                    txtTemp += txt
                    estado = 1
                
                elif (isNumero(txt)):
                    txtTemp +=   txt
                    estado = 1

                else:
                    if verificacion == True:
                        print("Se reconocio en S1: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                        TokensTemp = []
                        acces = 0
                        for reservadas in PalabrasReservadas:
                            if txtTemp.__eq__(reservadas):
                                TokensTemp.append("RESERVADA")
                                acces =1
                                break

                        if acces == 0:
                            TokensTemp.append("IDENTIFICADOR")
                        else:
                            acces = 0

                        TokensTemp.append(txtTemp)
                        TokensTemp.append(fila)
                        TokensTemp.append(str(columna - len(txtTemp)))

                        Tokens.append(TokensTemp)

                        txtTemp = ""
                        estado = 0
                        opcion = True
                    else:
                        print("No se reconocio en S1: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                        txtTemp = ""
                        estado = 0
                        opcion = True


            elif estado == 2:
                if verificacion == True:
                    if len(txtTemp)>1:
                        print("Se reconocio en S2: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                        TokensTemp = []

                        cantidad = len(txtTemp)
                        if txtTemp[0] == '"' and txtTemp[cantidad-1] == '"':
                            TokensTemp.append("TITULO")
                        elif txtTemp[0] == '#':
                            TokensTemp.append("COLOR")
                        else:
                            TokensTemp.append("IDENTIFICADOR")
                            
                        TokensTemp.append(txtTemp)
                        TokensTemp.append(fila)
                        TokensTemp.append(str(columna - len(txtTemp)))

                        Tokens.append(TokensTemp)

                        if(txtTemp == "@@@@"):
                            opcion = False
                        else:
                            opcion = True
                            
                  
                    else:
                        print("Se reconocio en S2: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna ))
                        TokensTemp = []
                        TokensTemp.append("SIMBOLO")
                        TokensTemp.append(txtTemp)
                        TokensTemp.append(fila)
                        TokensTemp.append(str(columna))

                        Tokens.append(TokensTemp)

                        opcion = False
                else:
                    if len(txtTemp)>1:
                        print("No se reconocio en S2: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                    else:
                        print("No se reconocio en S2: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna ))
                    txtTemp = ""
                    estado = 0
                    opcion = True

                txtTemp = ""
                estado = 0
            
            elif estado == 3:
                if ord(txt) != 34:
                    txtTemp += txt
                    opcion = False
                else:
                    txtTemp += txt
                    estado = 2
                    opcion = False
                    
                 
            elif estado == 4:
                opcion = False
           
                if (isNumero(txt)):
                    txtTemp += txt
                    estado = 4

                else:
                    if verificacion == True:
                        print("Se reconocio en S4: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                        TokensTemp = []
                        TokensTemp.append("DIGITO")
                        TokensTemp.append(txtTemp)
                        TokensTemp.append(fila)
                        TokensTemp.append(str(columna - len(txtTemp)))

                        Tokens.append(TokensTemp)

                        txtTemp = ""
                        estado = 0
                        opcion = True
                    else:
                        print("No se reconocio en S4: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                        txtTemp = ""
                        estado = 0
                        opcion = True

            elif estado == 5:
                opcion = False
           
                if (isNumero(txt)):
                    txtTemp += txt
                    estado = 7
                else:
                    errortipo= 'Caracter inesperado, esperaba D'
                    verificacion = False
                    txtTemp += txt
                    estado = 7
                    print("Error Lexico, se detecto " + txt + " en S7  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)

            elif estado == 7:
                opcion = False
           
                if (isNumero(txt)):
                    txtTemp += txt
                    estado = 9
                else:
                    errortipo= 'Caracter inesperado, esperaba D'
                    verificacion = False
                    txtTemp += txt
                    estado = 9
                    print("Error Lexico, se detecto " + txt + " en S7  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)
                        
            
            elif estado == 9:
                opcion = False
           
                if (isNumero(txt)):
                    txtTemp += txt
                    estado = 11
                else:
                    errortipo= 'Caracter inesperado, esperaba D' 
                    verificacion = False
                    txtTemp += txt
                    estado = 11
                    print("Error Lexico, se detecto " + txt + " en S9  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)

            elif estado == 11:
                opcion = False
           
                if (isNumero(txt)):
                    txtTemp += txt
                    estado = 12
                else:
                    errortipo= 'Caracter inesperado, esperaba D'
                    verificacion = False
                    txtTemp += txt
                    estado = 12
                    print("Error Lexico, se detecto " + txt + " en S11  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)
            
            elif estado == 12:
                opcion = False
           
                if (isNumero(txt)):
                    txtTemp += txt
                    estado = 13
                else:
                    errortipo= 'Caracter inesperado, esperaba D'
                    verificacion = False
                    txtTemp += txt
                    estado = 13
                    print("Error Lexico, se detecto " + txt + " en S12  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)

            elif estado == 13:
                opcion = False
           
                if (isNumero(txt)):
                    txtTemp += txt
                    estado = 2
                else:
                    errortipo= 'Caracter inesperado, esperaba D'
                    verificacion = False
                    txtTemp += txt
                    estado = 2
                    print("Error Lexico, se detecto " + txt + " en S13  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)

            elif estado == 6:
                opcion = False
           
                if (ord(txt) == 64):
                    txtTemp += txt
                    estado = 8
                else:
                    errortipo = 'Caracter inesperado, esperaba @'
                    verificacion = False
                    txtTemp += txt
                    estado = 8
                    print("Error Lexico, se detecto " + txt + " en S6  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)

            elif estado == 8:
                opcion = False
           
                if (ord(txt) == 64):
                    txtTemp += txt
                    estado = 10
                else:
                    errortipo= 'Caracter inesperado, esperaba @'
                    verificacion = False
                    txtTemp += txt
                    estado = 10
                    print("Error Lexico, se detecto " + txt + " en S8  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)
            
            elif estado == 10:
                opcion = False
           
                if (ord(txt) == 64):
                    txtTemp += txt
                    estado = 2
                else:
                    errortipo = 'Caracter inesperado, esperaba @'
                    verificacion = False
                    txtTemp += txt
                    estado = 2
                    print("Error Lexico, se detecto " + txt + " en S10  F: " + str(fila) + ", C: " + str(columna))
                    errortemp =[]
                    errortemp.append(txt)
                    errortemp.append(errortipo)
                    errortemp.append(fila)
                    errortemp.append(columna)
                    Errores.append(errortemp)
                

        # Control de filas y columnas
        # Salto de Linea
        if (ord(txt) == 10):
            columna = 1
            fila += 1
            continue
        # Tab Horizontal
        elif (ord(txt) == 9):
            columna += 4
            continue
        # Espacio
        elif (ord(txt) == 32):
            columna += 1
            continue
        
        columna += 1

    print("///////////////////")
    print(Tokens)
    print("///////////////////")
    #print(Tokens[0])
    #print(Tokens[0][1])
    #print(Errores)
    

    #print(txtTemp)

def isLetra(txt):
    if((ord(txt) >= 65 and ord(txt) <= 90) or (ord(txt) >= 97 and ord(txt) <= 122) or ord(txt) == 164 or ord(txt) == 165):
        return True
    else:
        return False

def isSimbolo(txt):
    
    if(ord(txt) == 61 or ord(txt) == 59 or ord(txt) == 123 or ord(txt) == 125  or ord(txt) == 91 or ord(txt) == 93 or ord(txt) == 44):
        return True
    else:
        return False

def isNumero(txt):
    if ((ord(txt) >= 48 and ord(txt) <= 57)):
        return True
    else:
        return False


def ConfromacionEntrada():
    for caracter in Tokens:
        
        #print(caracter[0])
        if caracter[0] == "RESERVADA":
     
            for reservadas in PalabrasReservadas:
                        if caracter[1].__eq__("TITULO"):
                            #print(caracter[1])
                            Titulo = caracter[1]
                            break
                        elif caracter[1].__eq__("ANCHO"):
                            #print(caracter[1])
                            Ancho = caracter[1]
                            break
                        elif caracter[1].__eq__("ALTO"):
                            #print(caracter[1])
                            Alto = caracter[1]
                            break
                        elif caracter[1].__eq__("FILAS"):
                            #print(caracter[1])
                            Filas = caracter[1]
                            break
                        elif caracter[1].__eq__("COLUMNAS"):
                            #print(caracter[1])
                            Columnas = caracter[1]
                            break
                        elif caracter[1].__eq__("CELDAS"):
                            #print(caracter[1])
                            Celdas = caracter[1]
                            break
                        elif caracter[1].__eq__("FILTROS"):
                            print(caracter[1])
                            Filtros = caracter[1]
                            break
                        elif caracter[1].__eq__("MIRRORX"):
                            print(caracter[1])
                            Mirrorx = caracter[1]
                            break
                        elif caracter[1].__eq__("MIRRORY"):
                            print(caracter[1])
                            Mirrory = caracter[1]
                            break
                        elif caracter[1].__eq__("DOUBLEMIRROR"):
                            print(caracter[1])
                            DoubleMirror = caracter[1]
                            break
                        elif caracter[1].__eq__("TRUE"):
                            print(caracter[1])
                            verdadero = caracter[1]
                            break
                        elif caracter[1].__eq__("FALSE"):
                            print(caracter[1])
                            falso = caracter[1]
                            break

    print("Titulo:", Titulo,"Ancho:", Ancho,"Alto:", Alto,"Filas:", Filas,"Columnas:", Columnas,"Celdas:", Celdas)
        


def AsignarListado(Asignar,Titulo,Ancho,Alto,Filas,Columnas,Celdas):

    if Asignar == True:
        e1 = ListaImagenes(Titulo,Ancho,Alto,Filas,Columnas,Celdas)
        
        lista_e.insertar(e1)
        lista_e.recorrer()
    else:
        pass

#Crea la tabla de tokens
def TablaTokens():
    
    global PalabrasReservadas
    PalabrasReservadas = ["TITULO","ANCHO","ALTO","FILAS","COLUMNAS","CELDAS","FILTROS","MIRRORX","MIRRORY","DOUBLEMIRROR","TRUE","FALSE"]
    #print(PalabrasReservadas)
    



    
