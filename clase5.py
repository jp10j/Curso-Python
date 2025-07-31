import os
import platform
import sys
color_amarillo_brillante = "\033[93m"
color_reset = "\033[0m"
color_verde = "\033[32m"
color_verde_brillante = "\033[92m"
clear = lambda: os.system('cls' if platform.system() == 'Windows' else 'clear')
def limpiar_pantalla():
    clear()
    
#limpiar_pantalla()    
class Numero:
    def __init__(self, numero):
        self.numero = numero
    def evaluar_numero(self):
        if self.numero & 1:
            print(f"{color_amarillo_brillante}EL NUMERO INGRESADO ES IMPAR{color_reset}")
            if self.numero == 7:
                print(f"{color_amarillo_brillante}EL NUMERO INGRESADO ES UN COMODIN{color_reset}")
            
        else:
            print(f"{color_amarillo_brillante}EL NUMERO INGRESADO ES PAR{color_reset}")
            if self.numero == 10:
                print(f"{color_amarillo_brillante}EL NUMERO INGRESADO ES 10{color_reset}")
    def sumar(self, numeroasumar):
        return self.numero + numeroasumar

if __name__ == "__main__":
    def main():
        numeroaevaluar = Numero(int(input(f"{color_verde}INGRESE UN NUMERO: {color_reset}")))
        numeroaevaluar.evaluar_numero()
        sumarealizada = numeroaevaluar.sumar(2)   
        print(f"{color_amarillo_brillante}LA SUMA REALIZADA ES: {color_reset}{sumarealizada}")
        print(f"{color_amarillo_brillante}LINEA NUEVA {color_reset}")
    main()
