
import math
import copy
from html2image import Html2Image
hti = Html2Image()

    
    
class ListaImagenes:
  def __init__(self,Titulo,Ancho,Alto,Filas,Columnas,CeldasNomrales,Filtros):
    title = Titulo[1:]
    title = title[:-1]
    self.Titulo=title
    self.Ancho=Ancho
    self.Alto=Alto
    self.Filas=Filas
    self.Columnas=Columnas
    self.Celdas= CeldasNomrales
    self.Filtros=Filtros
    self.Original=None
  
 
    self.Procesado = False
    self.ProcesadoX = False
    self.ProcesadoY = False
    self.ProcesadoDouble = False

    self.MIRRORX = False
    self.MIRRORY =False
    self.DOUBLEMIRROR =False

    self.ElementoORIGNINAL = 'Falta_filtro.png'
    self.ElementoMIRRORX = 'Falta_filtro.png'
    self.ElementoMIRRORYL = 'Falta_filtro.png'
    self.ElementoDOUBLEMIRROR = 'Falta_filtro.png'


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

  def OptenerNames(self):
    lista = []
    actual= self.primero
    while actual != None:
      lista.append(actual.Nodo.Titulo)
      actual = actual.siguiente
    return  lista

#--------------------------------------------------------------------------------------------------------------------------------------
  def buscar(self,Titulo):
    ListasDirecciones = []

    actual = self.primero
    anterior = None
    while actual and actual.Nodo.Titulo != Titulo:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("\nNo se encontro el Titulo:", Titulo)
        break
    if actual is not None:
      if actual.Nodo.Titulo == Titulo:
        ListasDirecciones.append('./IMG_generada/' + actual.Nodo.ElementoORIGNINAL)
        ListasDirecciones.append('./IMG_generada/' +actual.Nodo.ElementoMIRRORX)
        ListasDirecciones.append('./IMG_generada/' +actual.Nodo.ElementoMIRRORYL)
        ListasDirecciones.append('./IMG_generada/' +actual.Nodo.ElementoDOUBLEMIRROR)
        
        #print("\Titulo a procesar: ", actual.Nodo.Titulo)
        return ListasDirecciones


  def VerificarFiltros(self):
    actual= self.primero
    while actual != None:
      if actual.Nodo.Filtros != None:
        for Filtro in actual.Nodo.Filtros:
          
          if Filtro.__eq__("MIRRORX"):
            actual.Nodo.MIRRORX = True
          elif Filtro.__eq__("MIRRORY"):
            actual.Nodo.MIRRORY = True
          elif Filtro.__eq__("DOUBLEMIRROR"):
            actual.Nodo.DOUBLEMIRROR = True
        
      actual = actual.siguiente
 
  def GeneararFiltroDouble(self):
    Temp= []
    
     #Generar HTML---------------------------------------------------------------
      
    Contenido = htmlInicial
    actual= self.primero
    encontrado= False

    while actual != None:
      if actual.Nodo.ProcesadoDouble == False and actual.Nodo.DOUBLEMIRROR == True:
        
        
        actual.Nodo.ProcesadoDouble = True
        enY = int(actual.Nodo.Filas)-1
        enX = int(actual.Nodo.Columnas)-1

        Temp =  copy.deepcopy(actual.Nodo.Celdas)
        catindad = len(Temp)
        for i in range(0, int(catindad)): 
          Temp[i][0] = enX - int(Temp[i][0]) 
          Temp[i][1] = enY - int(Temp[i][1]) 

        width = float(int(actual.Nodo.Ancho)/ int(actual.Nodo.Columnas))
        width = math.ceil(width)
        height = float(int(actual.Nodo.Alto)/ int(actual.Nodo.Filas))
        height = math.ceil(height)
        Contenido +='.canvas {width:' +  actual.Nodo.Ancho  + 'px;   height:' +  actual.Nodo.Alto + 'px;}\n\n'
        Contenido += '.pixel{ width:' +  str(width) + 'px; height:' +  str(height) + 'px; float: left; box-shadow: 0px 0px 1px #fff; } \n\n\n'
        Contenido += '</style></head><body> \n <div class="canvas">\n'
        catindad = len(Temp)
        
        for y in range(0, int(actual.Nodo.Filas) ):
          for x in range(0, int(actual.Nodo.Columnas) ):
              for i in range(0, int(catindad)):
                if int(Temp[i][0]) == x and int(Temp[i][1]) == y:
                  if Temp[i][2].__eq__("TRUE"):
                    Contenido+='<div class="pixel" style="background-color:' +Temp[i][3] +  ';"></div>\n'
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
        if actual.Nodo.DOUBLEMIRROR == True:
          GenerarReportes(actual.Nodo.Titulo,Contenido,"DOUBLE",actual)
          
        
        Contenido = htmlInicial
      actual = actual.siguiente

  def GeneararFiltroY(self):
      Temp= []

      #Generar HTML---------------------------------------------------------------
      Contenido = htmlInicial
      actual= self.primero
      encontrado= False

      while actual != None:
        if actual.Nodo.ProcesadoY == False and actual.Nodo.MIRRORY == True:
          actual.Nodo.ProcesadoY = True
          enY = int(actual.Nodo.Filas)-1
          Temp = copy.deepcopy(actual.Nodo.Celdas)
          
          catindad = len(Temp)
          for i in range(0, int(catindad)): 
            Temp[i][1] = enY - int(Temp[i][1]) 
      


          width = float(int(actual.Nodo.Ancho)/ int(actual.Nodo.Columnas))
          width = math.ceil(width)
          height = float(int(actual.Nodo.Alto)/ int(actual.Nodo.Filas))
          height = math.ceil(height)

          Contenido +='.canvas {width:' +  actual.Nodo.Ancho  + 'px;   height:' +  actual.Nodo.Alto + 'px;}\n\n'
          Contenido += '.pixel{ width:' +  str(width) + 'px; height:' +  str(height) + 'px; float: left; box-shadow: 0px 0px 1px #fff; } \n\n\n'
          Contenido += '</style></head><body> \n <div class="canvas">\n'
          catindad = len(Temp)
          
          for y in range(0, int(actual.Nodo.Filas) ):
            for x in range(0, int(actual.Nodo.Columnas) ):
                for i in range(0, int(catindad)):
                  if int(Temp[i][0]) == x and int(Temp[i][1]) == y:
                    if Temp[i][2].__eq__("TRUE"):
                      Contenido+='<div class="pixel" style="background-color:' +Temp[i][3] +  ';"></div>\n'
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
          if actual.Nodo.MIRRORY == True:
            GenerarReportes(actual.Nodo.Titulo,Contenido,"MIRRORY",actual)
          Contenido = htmlInicial
        actual = actual.siguiente

  def GeneararFiltroX(self):
    Temp= []
 
      #Generar HTML---------------------------------------------------------------

    Contenido = htmlInicial

    actual= self.primero
    
    encontrado= False

    while actual != None:
      if actual.Nodo.ProcesadoX == False and actual.Nodo.MIRRORX == True:
        actual.Nodo.ProcesadoX = True
        Temp = copy.deepcopy(actual.Nodo.Celdas)
        enX = int(actual.Nodo.Columnas)-1
        
        
        catindad = len(Temp)
        for i in range(0, int(catindad)): 
          Temp[i][0] = enX - int(Temp[i][0]) 
        width = float(int(actual.Nodo.Ancho)/ int(actual.Nodo.Columnas))
        width = math.ceil(width)
        height = float(int(actual.Nodo.Alto)/ int(actual.Nodo.Filas))
        height = math.ceil(height)

        Contenido +='.canvas {width:' +  actual.Nodo.Ancho  + 'px;   height:' +  actual.Nodo.Alto + 'px;}\n\n'
        Contenido += '.pixel{ width:' +  str(width) + 'px; height:' +  str(height) + 'px; float: left; box-shadow: 0px 0px 1px #fff; } \n\n\n'
        Contenido += '</style></head><body> \n <div class="canvas">\n'
        catindad = len(Temp)
        
        for y in range(0, int(actual.Nodo.Filas) ):
          for x in range(0, int(actual.Nodo.Columnas) ):
              for i in range(0, int(catindad)):
                if int(Temp[i][0]) == x and int(Temp[i][1]) == y:
                  if Temp[i][2].__eq__("TRUE"):
                    Contenido+='<div class="pixel" style="background-color:' +Temp[i][3] +  ';"></div>\n'
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
        if actual.Nodo.MIRRORX == True:
          GenerarReportes(actual.Nodo.Titulo,Contenido,"MIRRORX",actual)
        Contenido = htmlInicial
      

      actual = actual.siguiente

  def GenrarHTML(self):

    Contenido = htmlInicial

    actual= self.primero
    encontrado= False

    while actual != None:
      # --------------------------------------------------------------------------------------------------
      if actual.Nodo.Procesado == False:
        actual.Nodo.Procesado = True
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
            

              for i in range(0, int(catindad)):
                if int(actual.Nodo.Celdas[i][0]) == x and int(actual.Nodo.Celdas[i][1]) == y:
                  if actual.Nodo.Celdas[i][2].__eq__("TRUE"):
                    Contenido+='<div class="pixel" style="background-color:' +actual.Nodo.Celdas[i][3] +  ';"></div>\n'
                  
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
      
        GenerarReportes(actual.Nodo.Titulo,Contenido,"ORIGINAL",actual)
        print("Lectura realizada:",actual.Nodo.Titulo)
        Contenido = htmlInicial
      
      actual = actual.siguiente
     # --------------------------------------------------------------------------------------------------

    def limpiar(self):
      cadena = []
      actual= self.primero
      while actual != None:
        if actual.siguiente is not None:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente
        else:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente 

      for teerrenoV in cadena:
        actual = self.primero
        anterior = None

        while actual and actual.Nodo.Titulo != teerrenoV:
          anterior = actual
          actual = actual.siguiente
        
        if anterior is None:
          self.primero = actual.siguiente
        elif actual:
          anterior.siguiente = actual.siguiente
          actual.siguiente = None

    def limpiar(self):
      cadena = []
      actual= self.primero
      while actual != None:
        if actual.siguiente is not None:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente
        else:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente 

      for teerrenoV in cadena:
        actual = self.primero
        anterior = None

        while actual and actual.Nodo.Titulo != teerrenoV:
          anterior = actual
          actual = actual.siguiente
        
        if anterior is None:
          self.primero = actual.siguiente
        elif actual:
          anterior.siguiente = actual.siguiente
          actual.siguiente = None

    def limpiar(self):
      cadena = []
      actual= self.primero
      while actual != None:
        if actual.siguiente is not None:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente
        else:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente 

      for teerrenoV in cadena:
        actual = self.primero
        anterior = None

        while actual and actual.Nodo.Titulo != teerrenoV:
          anterior = actual
          actual = actual.siguiente
        
        if anterior is None:
          self.primero = actual.siguiente
        elif actual:
          anterior.siguiente = actual.siguiente
          actual.siguiente = None

  def limpiar(self):
      cadena = []
      actual= self.primero
      while actual != None:
        if actual.siguiente is not None:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente
        else:
          cadena.append(actual.Nodo.Titulo)
          actual = actual.siguiente 

      for teerrenoV in cadena:
        actual = self.primero
        anterior = None

        while actual and actual.Nodo.Titulo != teerrenoV:
          anterior = actual
          actual = actual.siguiente
        
        if anterior is None:
          self.primero = actual.siguiente
        elif actual:
          anterior.siguiente = actual.siguiente
          actual.siguiente = None

def GenerarReportes(Titulo,Contenido,tipo,Actual):
    try: 
        FileHTML=open("./HTML_Generados/" +Titulo + "_" +tipo+".HTML","w") 
        FileHTML.write(Contenido) 
        FileHTML.close() 

        hti = Html2Image(output_path='./IMG_generada')
        hti.screenshot(other_file='./HTML_Generados/' +Titulo + "_" +tipo+".HTML",save_as= Titulo + "_" +tipo+'.png')

        if tipo.__eq__("ORIGINAL"):
          #print(Actual.Nodo.Titulo,tipo)
          Actual.Nodo.ElementoORIGNINAL = Titulo + "_" +tipo+'.png'
        elif tipo.__eq__("MIRRORX"):
          #print(Actual.Nodo.Titulo,tipo)
          Actual.Nodo.ElementoMIRRORX =  Titulo + "_" +tipo+'.png'
        elif tipo.__eq__("MIRRORY"):
          #print(Actual.Nodo.Titulo,tipo)
          Actual.Nodo.ElementoMIRRORYL =  Titulo + "_" +tipo+'.png'
        elif tipo.__eq__("DOUBLE"):
          #print(Actual.Nodo.Titulo,tipo)
          Actual.Nodo.ElementoDOUBLEMIRROR =  Titulo + "_" +tipo+'.png'
    except:
        print("La creación del Reporte falló")
    #else:
        #print("Se ha creado el Reporte de",Titulo,"Filtro:",tipo )


htmlInicial = """  <!DOCTYPE html><html>
<head><style >
  body { background:#333333; height: 100vh; display:flex; justify-content:center; align-items:center;}\n"""




       
