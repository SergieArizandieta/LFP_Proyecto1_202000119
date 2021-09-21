from Operaciones import *
from reportes import *
import Grafica 

def abrir_ventana():
    Grafica.ventanas()

if __name__ == "__main__":
    
    try: 
        TablaTokens()
        abrir_ventana()
        

    except Exception:
        
        print("Error, m")
