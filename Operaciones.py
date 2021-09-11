from tkinter import filedialog, Tk
from tkinter.constants import FALSE
from ListaSimple import *

lista_e = lista_enlazada()

PalabrasReservadas = []
Tokens = []
Errores = []


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
    global Tokens
    Tokens = []
    global Errores
    Errores = []


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
                    print("ARROBA")

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
                    estado = 0
                    print("Error Lexico, se detecto " + txt + " en S6  F: " + str(fila) + ", C: " + str(columna))
                    txtTemp = ""
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
                    estado = 0
                    print("Error Lexico, se detecto " + txt + " en S8  F: " + str(fila) + ", C: " + str(columna))
                    txtTemp = ""
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
                    estado = 0
                    print("Error Lexico, se detecto " + txt + " en S10  F: " + str(fila) + ", C: " + str(columna))
                    txtTemp = ""
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
    ConfromacionEntrada()
    #print(Tokens[0])
    #print(Tokens[0][1])
    
    

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
    contarFiltros1= 0
    contarFiltros2= 0
    contarFiltros3= 0

    ValidacionPermante = True

    ValidacionOtro = False


    ValidacionUltimo = False
    ValidarUltimoFiltro = False
    ValidacionCerrarCeldas = False

    TextTemp = ""
    ValidacionPalbraReservada = False
    ValidacionData = False
    ValidarCerrarData = False
    ValidacionAsignacion = True

    ValidacionCeldas = False
    CeldasContador= 0
    ValidacionFinalizacionCeldas = False
    ValidarFiltros = False

    ListaColores= []
 

    for caracter in Tokens:    
        #print(caracter[0])
    
        #Buscar si es palabra reservada
        if caracter[0] == "RESERVADA" and ValidacionPalbraReservada == False:
     
            if caracter[1].__eq__("TITULO"):
                ValidacionPalbraReservada= True
                TextTemp = caracter[1]
                continue
                
            elif caracter[1].__eq__("ANCHO"):
                ValidacionPalbraReservada= True
                TextTemp = caracter[1]
                continue
                
            elif caracter[1].__eq__("ALTO"):
                ValidacionPalbraReservada= True
                TextTemp = caracter[1]
                continue
                
            elif caracter[1].__eq__("FILAS"):
                ValidacionPalbraReservada= True
                TextTemp = caracter[1]
                continue
                
            elif caracter[1].__eq__("COLUMNAS"):
                ValidacionPalbraReservada= True
                TextTemp = caracter[1]
                continue
                
            elif caracter[1].__eq__("CELDAS"):
                ValidacionPalbraReservada= True
                TextTemp = caracter[1]
                
                continue
                
            elif caracter[1].__eq__("FILTROS"):
                ValidacionUltimo = False
                ValidacionPalbraReservada= True
                TextTemp = caracter[1]
                continue
                
        #Desplegar 
        
        if ValidacionUltimo == True and ValidacionPermante == True:
            ValidacionPermante = False
            ValidacionUltimo = False
            ValidacionOtro = True
            print("///////////////////")
            print(ValidacionAsignacion, " Validacion")
            if ValidacionAsignacion == True :
                AsignarListado(True,Titulo,Ancho,Alto,Filas,Columnas,ListaColores,ListaFiltrosTemp)
               #print("Titulo:", Titulo,"Ancho:", Ancho,"Alto:", Alto,"Filas:", Filas,"Columnas:", Columnas)
                #print("Celdas:", ListaColores)
                #print("Filtros", ListaFiltrosTemp)
                print("///////////////////")
            

        if ValidacionOtro== True and caracter[1] == "@@@@":
            ValidacionPermante = True
            #print("sadSADASDDASASDDS")
            ValidacionOtro = False

            ValidacionUltimo = False
            ValidarUltimoFiltro = False
            ValidacionCerrarCeldas = False

            TextTemp = ""
            ValidacionPalbraReservada = False
            ValidacionData = False
            ValidarCerrarData = False
            ValidacionAsignacion = True

            ValidacionCeldas = False
            CeldasContador= 0
            ValidacionFinalizacionCeldas = False
            ValidarFiltros = False

            ListaColores= []
        elif  ValidacionOtro== False and caracter[1] == "@@@@":
            errortipo= 'No se esperaba "@@@@" ' 
            errortemp =[]
            errortemp.append(caracter[1])
            errortemp.append(errortipo)
            errortemp.append(caracter[2])
            errortemp.append(int(caracter[3]))
            Errores.append(errortemp)

        

        #RESERVADA VALIDACION =   
        if ValidacionPalbraReservada == True and ValidacionData==False:
            if caracter[1].__eq__("="):
                ValidacionData = True
                ValidacionPalbraReservada = False
                continue

            else:
           
                ValidacionAsignacion = False
                errortipo= 'Caracter inesperado, se esperaba "="' 
                errortemp =[]
                errortemp.append(caracter[1])
                errortemp.append(errortipo)
                errortemp.append(caracter[2])
                errortemp.append(int(caracter[3]))
                Errores.append(errortemp)
                continue
        
        #Finalizacion Validacion Celdas
        if ValidacionFinalizacionCeldas:
            if caracter[1].__eq__(","):
                ValidacionFinalizacionCeldas = False                
                continue
            else:
                if CeldasContador ==1:
                    ValidacionFinalizacionCeldas = False  
                elif contarFiltros1 != 0 or contarFiltros2 != 0 or contarFiltros3 != 0:
                    ValidarCerrarData = True
                    ValidarFiltros = False
                    ValidacionData =False
                    ValidarUltimoFiltro = True

                else:
                    ValidacionAsignacion = False
                    errortipo= 'Caracter inesperado, se esperaba ","' 
                    errortemp =[]
                    errortemp.append(caracter[1])
                    errortemp.append(errortipo)
                    errortemp.append(caracter[2])
                    errortemp.append(int(caracter[3]))
                    Errores.append(errortemp)
                    continue       

        #DATA VALIDACION Resevadas
        if ValidacionData:
            if TextTemp.__eq__("TITULO"):
                ValidarCerrarData = True
                ValidacionData = False
                cantidad = len(caracter[1])
                if caracter[1][0] == '"' and caracter[1][cantidad-1] == '"':
                    Titulo = caracter[1]
                    continue

                else:
                    ValidacionAsignacion = False
                    errortipo= 'Caracter inesperado, se esperaba el Patron de Titulo' 
                    errortemp =[]
                    errortemp.append(caracter[1])
                    errortemp.append(errortipo)
                    errortemp.append(caracter[2])
                    errortemp.append(int(caracter[3]))
                    Errores.append(errortemp)
                    continue

            elif TextTemp.__eq__("ANCHO") or TextTemp.__eq__("ALTO") or TextTemp.__eq__("FILAS") or TextTemp.__eq__("COLUMNAS"):
                ValidacionData = False
                ValidarCerrarData = True
                if str.isdigit(caracter[1]):
                    if TextTemp.__eq__("ANCHO"):
                        Ancho = caracter[1]
                        
                    elif TextTemp.__eq__("ALTO"):
                        Alto = caracter[1]
                        
                    elif TextTemp.__eq__("FILAS"):
                        Filas = caracter[1]
                        
                    elif TextTemp.__eq__("COLUMNAS"):
                        Columnas = caracter[1]
                    continue
                else:
                    ValidacionAsignacion = False
                    ValidacionAsignacion = False
                    errortipo= 'Caracter inesperado, se esperaba un digito ' 
                    errortemp =[]
                    errortemp.append(caracter[1])
                    errortemp.append(errortipo)
                    errortemp.append(caracter[2])
                    errortemp.append(int(caracter[3]))
                    Errores.append(errortemp)
                    continue
                     
            elif TextTemp.__eq__("CELDAS"):
                ValidacionData = False
                ValidacionCeldas = True
                
            elif TextTemp.__eq__("FILTROS"):
                ValidacionData = False
                ValidarFiltros = True
                ListaFiltrosTemp=[]
                contarFiltros1 = 0
                contarFiltros2 = 0
                contarFiltros3 = 0
                
        #Validar Filtros
        if ValidarFiltros:
            
            if caracter[1].__eq__("MIRRORX") and contarFiltros1==0 :                
                ListaFiltrosTemp.append("MIRRORX")
                contarFiltros1= 1
                ValidacionFinalizacionCeldas = True
                continue

            elif caracter[1].__eq__("MIRRORY") and contarFiltros2==0 :
                ListaFiltrosTemp.append("MIRRORY")
                contarFiltros2= 1
                ValidacionFinalizacionCeldas = True
                continue

            elif caracter[1].__eq__("DOUBLEMIRROR") and contarFiltros3==0 :
                ListaFiltrosTemp.append("DOUBLEMIRROR")
                contarFiltros3= 1
                ValidacionFinalizacionCeldas = True
                continue
            elif contarFiltros1!= 0 or contarFiltros2!= 0 or contarFiltros3!= 0:
                pass
            else:
                ValidacionAsignacion = False
                errortipo= 'Caracter inesperado, esperado, no cumple con el patro de Filtros' 
                errortemp =[]
                errortemp.append(caracter[1])
                errortemp.append(errortipo)
                errortemp.append(caracter[2])
                errortemp.append(int(caracter[3]))
                Errores.append(errortemp)
                
    

        #Validar si se cerro
        if ValidarCerrarData and ValidacionCeldas== False:
            ValidarCerrarData = False
            if caracter[1].__eq__(";"): 
                
                if ValidacionCerrarCeldas:
                    ValidacionCerrarCeldas = False
                    ValidacionUltimo = True

                if ValidarUltimoFiltro: 
                    ValidacionUltimo = True
                    ValidarUltimoFiltro = False

                if ValidarFiltros:
                    ValidarFiltros =False
                    

                ValidacionFinalizacionCeldas = False
                if ValidacionUltimo == True:
                    continue
                else:
                    continue
            else:
                ValidacionAsignacion = False
                errortipo= 'Caracter inesperado, se esperaba ";" ' 
                errortemp =[]
                errortemp.append(caracter[1])
                errortemp.append(errortipo)
                errortemp.append(caracter[2])
                errortemp.append(int(caracter[3]))
                Errores.append(errortemp)
                continue
        
        #Validar Elemntos de lista
        if ValidacionCeldas:
           
            if caracter[1].__eq__("{") and CeldasContador == 0:
                CeldasContador+=1

            elif caracter[1].__eq__("[") and CeldasContador == 1:
                CeldasContador+=1
                #tEMPORALES 
                TempListColores = []   
                TempX = 0
                TempY = 0
                TempBolean = ""
                TempColor = ""

            elif str.isdigit(caracter[1]) and CeldasContador == 2:
                CeldasContador+=1
                ValidacionFinalizacionCeldas = True
                TempX = caracter[1]
                TempListColores.append(TempX)                

            elif str.isdigit(caracter[1]) and CeldasContador == 3:
                CeldasContador+=1
                ValidacionFinalizacionCeldas = True
                TempY = caracter[1]
                TempListColores.append(TempY)
              

            elif (caracter[1] == "FALSE" or caracter[1] == "TRUE") and CeldasContador == 4:
                CeldasContador+=1
                ValidacionFinalizacionCeldas = True
                TempBolean = caracter[1]
                TempListColores.append(TempBolean)

            elif caracter[1][0] == '#' and CeldasContador == 5:
                cantidad = len(caracter[1])
                if cantidad == 7:
                    CeldasContador+=1
                    TempColor = caracter[1]
                    TempListColores.append(TempColor)
                    ListaColores.append(TempListColores)

            elif caracter[1].__eq__("]") and CeldasContador == 6:
                CeldasContador =1
                ValidacionFinalizacionCeldas = True

            elif caracter[1].__eq__("}") and CeldasContador == 1:
                CeldasContador= 0
                ValidarCerrarData = True
                ValidacionCeldas = False
                ValidacionCerrarCeldas = True
                
            else:
                ValidacionAsignacion = False

                if CeldasContador == 0:
                     errortipo= 'Caracter inesperado, se esperaba "{"' 
                elif CeldasContador == 1:
                    errortipo= 'Caracter inesperado, se esperaba "["' 
                elif CeldasContador == 2:
                    errortipo= 'Caracter inesperado, se un digito ' 
                elif CeldasContador == 3:
                    errortipo= 'Caracter inesperado, se esperaba un digito ' 
                elif CeldasContador == 4:
                    errortipo= 'Caracter inesperado, esperado, palabra reservada True|False ' 
                elif CeldasContador == 5:
                    errortipo= 'Caracter inesperado, esperado, palabra patron Color '
                elif CeldasContador == 6:
                    errortipo= 'Caracter inesperado, se espera "]"'
                CeldasContador= 0
                ValidacionCeldas = False
               
                errortemp =[]
                errortemp.append(caracter[1])
                errortemp.append(errortipo)
                errortemp.append(caracter[2])
                errortemp.append(caracter[3])
                Errores.append(errortemp)
                


        
    if ValidacionUltimo == True and ValidacionPermante == True:
            ValidacionUltimo = False
            ValidacionOtro = True
            print("///////////////////")
            print(ValidacionAsignacion, " Validacion")
            if ValidacionAsignacion == True :
                AsignarListado(True,Titulo,Ancho,Alto,Filas,Columnas,ListaColores,ListaFiltrosTemp)
                
                #print("Titulo:", Titulo,"Ancho:", Ancho,"Alto:", Alto,"Filas:", Filas,"Columnas:", Columnas)
                #print("Celdas:", ListaColores)
                #print("Filtros", ListaFiltrosTemp)
                print("///////////////////")
    lista_e.recorrer()
    
    print(Errores)
    print("///////////////////")

    """print(ValidacionAsignacion, " Validacion")
    if ValidacionAsignacion == True :
        print("Titulo:", Titulo,"Ancho:", Ancho,"Alto:", Alto,"Filas:", Filas,"Columnas:", Columnas)
        print("Celdas:", ListaColores)
        print("Filtros", ListaFiltrosTemp)"""

def PalabraReservaVerificacion(data):
    if data == "=":
        return True

def AsignarListado(Asignar,Titulo,Ancho,Alto,Filas,Columnas,Celdas,Filtros):

    if Asignar == True:
        e1 = ListaImagenes(Titulo,Ancho,Alto,Filas,Columnas,Celdas,Filtros)
        
        lista_e.insertar(e1)
        
    else:
        pass

#Crea la tabla de tokens
def TablaTokens():
    
    global PalabrasReservadas
    PalabrasReservadas = ["TITULO","ANCHO","ALTO","FILAS","COLUMNAS","CELDAS","FILTROS","MIRRORX","MIRRORY","DOUBLEMIRROR","TRUE","FALSE"]
    #print(PalabrasReservadas)
    
"""    
 elif caracter[1].__eq__("MIRRORX"):
                print(caracter[1])
                Mirrorx = caracter[1]
                
            elif caracter[1].__eq__("MIRRORY"):
                print(caracter[1])
                Mirrory = caracter[1]
                
            elif caracter[1].__eq__("DOUBLEMIRROR"):
                print(caracter[1])
                DoubleMirror = caracter[1]
                
            elif caracter[1].__eq__("TRUE"):
                print(caracter[1])
                verdadero = caracter[1]
                
            elif caracter[1].__eq__("FALSE"):
                print(caracter[1])
                falso = caracter[1]"""