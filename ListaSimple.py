from tkinter.constants import PROJECTING, X
import math

class ListaImagenes:
  def __init__(self,Titulo,Ancho,Alto,Filas,Columnas,Celdas,Filtros):
    title = Titulo[1:]
    title = title[:-1]
    self.Titulo=title
    self.Ancho=Ancho
    self.Alto=Alto
    self.Filas=Filas
    self.Columnas=Columnas
    self.Celdas=Celdas
    self.Filtros=Filtros
    self.Original=None
    self.MIRRORX =None
    self.MIRRORY =None
    self.DOUBLEMIRROR =None


class nodo:
    def __init__(self,Nodo =None,siguiente=None):
      self.Nodo=Nodo
      self.siguiente=siguiente

class lista_enlazada:
  def __init__(self):
    self.primero = None

  def insertar(self, Nodo):
    if self.primero is None:
      self.primero = nodo(Nodo=Nodo)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(Nodo=Nodo)
    
  def recorrer(self):
    print("\n")
    actual= self.primero
    while actual != None:
      print("Titulo:", actual.Nodo.Titulo,"Ancho:", actual.Nodo.Ancho,"Alto:", actual.Nodo.Alto,"Filas:", actual.Nodo.Filas,"Columnas:", actual.Nodo.Columnas,"Celdas:", actual.Nodo.Celdas,"Filtros",actual.Nodo.Filtros)
      actual = actual.siguiente


  def buscar(self,Titulo):
    actual = self.primero
    anterior = None
    while actual and actual.Titulo.Titulo != Titulo:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("\nNo se encontro el Titulo:", Titulo)
        break
    if actual is not None:
      if actual.Titulo.Titulo == Titulo:
        print("\Titulo a procesar: ", actual.Titulo.Titulo)
     #FILTROS-----------------------------------------------------
  def VerificarFiltros(self):
    
    print("\n")
    actual= self.primero
    while actual != None:
      for filtro in actual.Nodo.Filtros:
        print(filtro)
      actual = actual.siguiente
      
  def GeneararFiltroDouble(self):
    
    actual= self.primero
    enX = int(actual.Nodo.Columnas)-1
    actual= self.primero
    enY = int(actual.Nodo.Filas)-1

    while actual != None:
      actual.Nodo.DOUBLEMIRROR =  actual.Nodo.Celdas
      catindad = len(actual.Nodo.DOUBLEMIRROR)
      for i in range(0, int(catindad)): 
        actual.Nodo.DOUBLEMIRROR[i][0] = enX - int(actual.Nodo.DOUBLEMIRROR[i][0]) 
        actual.Nodo.DOUBLEMIRROR[i][1] = enY - int(actual.Nodo.DOUBLEMIRROR[i][1]) 
      actual = actual.siguiente

     #Generar HTML---------------------------------------------------------------
      
    Contenido = htmlInicial
    actual= self.primero
    encontrado= False

    while actual != None:
      width = float(int(actual.Nodo.Ancho)/ int(actual.Nodo.Columnas))
      width = math.ceil(width)
      height = float(int(actual.Nodo.Alto)/ int(actual.Nodo.Filas))
      height = math.ceil(height)
      Contenido +='.canvas {width:' +  actual.Nodo.Ancho  + 'px;   height:' +  actual.Nodo.Alto + 'px;}\n\n'
      Contenido += '.pixel{ width:' +  str(width) + 'px; height:' +  str(height) + 'px; float: left; box-shadow: 0px 0px 1px #fff; } \n\n\n'
      Contenido += '</style></head><body> \n <div class="canvas">\n'
      catindad = len(actual.Nodo.DOUBLEMIRROR)
      
      for y in range(0, int(actual.Nodo.Filas) ):
        for x in range(0, int(actual.Nodo.Columnas) ):
            for i in range(0, int(catindad)):
              if int(actual.Nodo.DOUBLEMIRROR[i][0]) == x and int(actual.Nodo.DOUBLEMIRROR[i][1]) == y:
                if actual.Nodo.DOUBLEMIRROR[i][2].__eq__("TRUE"):
                  Contenido+='<div class="pixel" style="background-color:' +actual.Nodo.DOUBLEMIRROR[i][3] +  ';"></div>\n'
                else:
                  Contenido+='<div class="pixel" style="background-color: transparent;"></div>\n'  
                encontrado = True
                break

            if encontrado == False:  
              Contenido+='<div class="pixel" ></div>\n'   
            else:
              encontrado = False
              continue        
     
      Contenido += '</div>\n</body></html>'
     
      GenerarReportes(actual.Nodo.Titulo,Contenido,"DOUBLE")
      Contenido = htmlInicial
      actual = actual.siguiente

  def GeneararFiltroY(self):
      
      actual= self.primero
      enY = int(actual.Nodo.Filas)-1

      while actual != None:
        actual.Nodo.MIRRORY =  actual.Nodo.Celdas
        catindad = len(actual.Nodo.MIRRORY)
        for i in range(0, int(catindad)): 
          actual.Nodo.MIRRORY[i][1] = enY - int(actual.Nodo.MIRRORY[i][1]) 
        actual = actual.siguiente

      #Generar HTML---------------------------------------------------------------
        
      Contenido = htmlInicial
      actual= self.primero
      encontrado= False

      while actual != None:

        width = float(int(actual.Nodo.Ancho)/ int(actual.Nodo.Columnas))
        width = math.ceil(width)
        height = float(int(actual.Nodo.Alto)/ int(actual.Nodo.Filas))
        height = math.ceil(height)

        Contenido +='.canvas {width:' +  actual.Nodo.Ancho  + 'px;   height:' +  actual.Nodo.Alto + 'px;}\n\n'
        Contenido += '.pixel{ width:' +  str(width) + 'px; height:' +  str(height) + 'px; float: left; box-shadow: 0px 0px 1px #fff; } \n\n\n'
        Contenido += '</style></head><body> \n <div class="canvas">\n'
        catindad = len(actual.Nodo.MIRRORY)
        
        for y in range(0, int(actual.Nodo.Filas) ):
          for x in range(0, int(actual.Nodo.Columnas) ):
              for i in range(0, int(catindad)):
                if int(actual.Nodo.MIRRORY[i][0]) == x and int(actual.Nodo.MIRRORY[i][1]) == y:
                  if actual.Nodo.MIRRORY[i][2].__eq__("TRUE"):
                    Contenido+='<div class="pixel" style="background-color:' +actual.Nodo.MIRRORY[i][3] +  ';"></div>\n'
                  else:
                    Contenido+='<div class="pixel" style="background-color: transparent;"></div>\n'  
                  encontrado = True
                  break
              if encontrado == False:  
                Contenido+='<div class="pixel" ></div>\n'   
              else:
                encontrado = False
                continue        
      
        Contenido += '</div>\n</body></html>'
        GenerarReportes(actual.Nodo.Titulo,Contenido,"MIRRORY")
        Contenido = htmlInicial
        actual = actual.siguiente

  def GeneararFiltroX(self):
    
    actual= self.primero
    enX = int(actual.Nodo.Columnas)-1
    while actual != None:
      actual.Nodo.MIRRORX =  actual.Nodo.Celdas
      catindad = len(actual.Nodo.MIRRORX)
      for i in range(0, int(catindad)): 
        actual.Nodo.MIRRORX[i][0] = enX - int(actual.Nodo.MIRRORX[i][0]) 
      actual = actual.siguiente

     #Generar HTML---------------------------------------------------------------
      
    Contenido = htmlInicial
    actual= self.primero
    encontrado= False

    while actual != None:

      width = float(int(actual.Nodo.Ancho)/ int(actual.Nodo.Columnas))
      width = math.ceil(width)
      height = float(int(actual.Nodo.Alto)/ int(actual.Nodo.Filas))
      height = math.ceil(height)

      Contenido +='.canvas {width:' +  actual.Nodo.Ancho  + 'px;   height:' +  actual.Nodo.Alto + 'px;}\n\n'
      Contenido += '.pixel{ width:' +  str(width) + 'px; height:' +  str(height) + 'px; float: left; box-shadow: 0px 0px 1px #fff; } \n\n\n'
      Contenido += '</style></head><body> \n <div class="canvas">\n'
      catindad = len(actual.Nodo.MIRRORX)
      
      for y in range(0, int(actual.Nodo.Filas) ):
        for x in range(0, int(actual.Nodo.Columnas) ):
            for i in range(0, int(catindad)):
              if int(actual.Nodo.MIRRORX[i][0]) == x and int(actual.Nodo.MIRRORX[i][1]) == y:
                if actual.Nodo.MIRRORX[i][2].__eq__("TRUE"):
                  Contenido+='<div class="pixel" style="background-color:' +actual.Nodo.MIRRORX[i][3] +  ';"></div>\n'
                else:
                  Contenido+='<div class="pixel" style="background-color: transparent;"></div>\n'  
                encontrado = True
                break

            if encontrado == False:  
              Contenido+='<div class="pixel" ></div>\n'   
            else:
              encontrado = False
              continue        
     
      Contenido += '</div>\n</body></html>'
     
      GenerarReportes(actual.Nodo.Titulo,Contenido,"MIRRORX")
      Contenido = htmlInicial
      actual = actual.siguiente

  def GenrarHTML(self):

    Contenido = htmlInicial

    actual= self.primero
    encontrado= False

    while actual != None:
      width = float(int(actual.Nodo.Ancho)/ int(actual.Nodo.Columnas))
      width = math.ceil(width)

      height = float(int(actual.Nodo.Alto)/ int(actual.Nodo.Filas))
      height = math.ceil(height)

      Contenido +='.canvas {width:' +  actual.Nodo.Ancho  + 'px;   height:' +  actual.Nodo.Alto + 'px;}\n\n'
      Contenido += '.pixel{ width:' +  str(width) + 'px; height:' +  str(height) + 'px; float: left; box-shadow: 0px 0px 1px #fff; } \n\n\n'
      Contenido += '</style></head><body> \n <div class="canvas">\n'
      catindad = len(actual.Nodo.Celdas)
      
      for y in range(0, int(actual.Nodo.Filas) ):
        for x in range(0, int(actual.Nodo.Columnas) ):
            print(x,",",y)
            for i in range(0, int(catindad)):
              if int(actual.Nodo.Celdas[i][0]) == x and int(actual.Nodo.Celdas[i][1]) == y:
                if actual.Nodo.Celdas[i][2].__eq__("TRUE"):
                  Contenido+='<div class="pixel" style="background-color:' +actual.Nodo.Celdas[i][3] +  ';"></div>\n'
                  print(actual.Nodo.Celdas[i])
                else:
                  #print(actual.Nodo.Celdas[i])
                  Contenido+='<div class="pixel" style="background-color: transparent;"></div>\n'  
                encontrado = True
                break

            if encontrado == False:  
              Contenido+='<div class="pixel" ></div>\n'   
            else:
              encontrado = False
              continue        
      #print(pixeles, "Cantidas")
      Contenido += '</div>\n</body></html>'
     
      GenerarReportes(actual.Nodo.Titulo,Contenido,"ORIGINAR")
      Contenido = htmlInicial
      actual = actual.siguiente

def GenerarReportes(Titulo,Contenido,tipo):
    try: 
        FileHTML=open("./HTML_Generados/" +Titulo + "_" +tipo+".HTML","w") 
        FileHTML.write(Contenido) 
        FileHTML.close() 
    except:
        print("La creación del Reporte falló")
    else:
        print("Se ha creado el Reporte" )

htmlInicial = """  <!DOCTYPE html><html>
<head><style >
  body { background:#333333; height: 100vh; display:flex; justify-content:center; align-items:center;}\n"""




       
