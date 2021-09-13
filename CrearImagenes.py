import Operaciones as Op


def CrearImagenes():
    Op.lista_e.OptenerNames()
    Op.lista_e.VerificarFiltros()
   
    Op.lista_e.GenrarHTML()
    Op.lista_e.GeneararFiltroX()
    Op.lista_e.GeneararFiltroY()
    Op.lista_e.GeneararFiltroDouble()
    print("////////////////////////////////")

def Limpiar():
    Op.lista_e.limpiar()
    Op.lista_e.recorrer()