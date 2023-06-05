"""
Instalar Pillow: pip3 install Pillow
creditos: parzibyte.me/blog
"""
from esteganografia_imagen import Esteganografia
from leer_mensaje import Leer
from clear import Clear

class Main():
    def main():
        while True:
            Clear.clear()
            print("Esteganografia en una imagen\n")
            print("Seleccione una opcion:\n1. Ocultar mensaje en una imagen.\n2. Leer mensaje de una imagen.\n3. Salir.")
            opc = int(input("Opción: "))
            Clear.clear()
            if opc == 1:
                mensaje = input("Ingrese el mensaje: \n")
                img = input("Ingrese el nombre de la imagen: ")
                img2 = input("Ingrese el nombre que va a tener la imagen con el mensaje: ")
                e = Esteganografia()
                e.ocultar_texto(mensaje, img, img2)
                input("Presione enter para continuar...")
            if opc == 2:
                l = Leer()
                mensaje = l.leer(input("Ingrese nombre de la imagen: "))
                print("El mensaje oculto es:\n" + mensaje)
                input("Presione enter para continuar...")
            if opc == 3:
                print("\n¿Está seguro que desea salir?\n1. Si\n2. No.")
                close = int(input("> "))
                if close == 1:
                    break
                elif close == 2:
                    print("Regresando...")
                else:
                    print("\nOpción invalida, intente de nuevo.")
                    input("Presione enter para continuar...")
            else:
                print("Opción invalida, intente de nuevo.")
                input("Presione enter para continuar...")

if __name__ == "__main__":
    Main.main()
