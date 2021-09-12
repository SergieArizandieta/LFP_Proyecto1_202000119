class ListaImagenes:
  def __init__(self,Titulo,Ancho,Alto,Filas,Columnas,Celdas,Filtros):
    self.Titulo=Titulo
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

  def GenrarHTMLOrginal(self):

    print("\n")
    actual= self.primero

    while actual != None:
      
      
      print( actual.Nodo.Celdas[0][1])
      actual = actual.siguiente













































htmlInicial = """<!DOCTYPE html>
<html>

<!--Encabezado-->
<head>
<meta charset="UTF-8">
<meta name="name" content="Reporte">
<meta name="description" content="name">
<meta name="keywods" content="python,dos,tres">
<meta name="robots" content="Index, Follow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="css/styles.css"/>
<title>Reporte</title>
</head>
<!----Curerpo--->
<body>
   <center><h6 class=\"titulos\" ><b> Reportes </b></h6>"""

htmlFinal = """<br><footer style="background-color:white;">Creado por: Sergie Daniel Arizandieta Yol - 202000119</footer>
</center></body>
</html>"""


       
"""if __name__ == "__main__":

    e1 = ListaImagenes('"EStrella"',1,2,3,4,"[CELDAS]")
    e2 = ListaImagenes('"BRilla"',1,2,3,4,"[CELDAS]")
    lista_e = lista_enlazada()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.recorrer()
      """
    