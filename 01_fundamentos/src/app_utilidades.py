from utilidades.calculos import sumar
from utilidades.formatos import formater_euros

if __name__ == "__main__":
    total = sumar(100,50)
    print("Total:", formater_euros(total))

