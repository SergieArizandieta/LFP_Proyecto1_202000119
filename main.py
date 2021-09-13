
from Operaciones import *
from reportes import *
import Grafica 

def abrir_ventana():
    Grafica.ventanas()

if __name__ == "__main__":
    
    try: 
        TablaTokens()

        abrir_ventana()
        
        #purificacionExtra()
        #ReporteTokens()
        #ReporteTErrores()

    except Exception:
        #print ("\nError vuelva a intentarlo\n", Exception)
        print()
