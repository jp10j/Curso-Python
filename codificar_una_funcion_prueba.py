import os
import platform
numero = []
color_amarillo = "\033[33m"
color_reset = "\033[0m"
COLOR_RESET = "\033[0m"
color_verde = "\033[32m"
color_verde_brillante = "\033[92m"
color_amarillo_brillante = "\033[93m"
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def ingresar_numero():
    numero = int(input(f"{color_verde}INGRESE UN NUMERO: {color_reset}"))
    return numero

def evaluar_numero(numero):
    if numero == 10:
        print(f"{color_amarillo_brillante}EL NUMERO INGRESADO ES 10{color_reset}")
    elif numero == 7:
        print(f"{color_amarillo_brillante}SE HA INGRESADO UN COMODIN{color_reset}")
    elif (numero % 2) == 0:
        print(f"{color_amarillo_brillante}EL NUMERO INGRESADO ES PAR{color_reset}")
    else:
        print(f"{color_amarillo_brillante}EL NUMERO INGRESADO ES IMPAR{color_reset}")
def main():
    clear()
    while True:
        numero = ingresar_numero()
        evaluar_numero(numero) 
        opcion = input(f"{color_verde}INGRESAR OTRO NUMERO (S/N): {color_reset}")
        if opcion.upper() == "N":
            break
        #clear()
    print(f"{color_verde_brillante}CLASES POR PROFESOR{color_reset}{color_amarillo_brillante} JONATHAN{color_reset}{color_verde_brillante} DESDE {COLOR_RESET}{color_amarillo_brillante}COLOMBIA{color_reset}")
    print(f"{color_verde_brillante}GRACIAS POR USAR ESTE PROGRAMA{color_reset}{color_amarillo_brillante} JUANPABLO {color_reset}{color_verde_brillante}DESDE{color_reset} {color_amarillo_brillante}VENEZUELA{color_reset}") 
if __name__ == "__main__":
    main()