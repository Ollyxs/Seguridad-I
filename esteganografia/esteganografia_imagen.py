from PIL import Image
import math 

class Esteganografia():
    
    terminacion = [1,1,1,1,1,1,1,1]

    def obtener_ascii(self, caracter):
        return ord(caracter)

    def obtener_binario(self, numero):
        return bin(numero)[2:].zfill(8)

    def cambiar_ultimo_bit(self, byte, nuevo_bit):
        return byte[:-1] + str(nuevo_bit)

    def binario_a_decimal(self, binario):
        return int(binario, 2)

    def modificar_color(self, color_original, bit):
        color_binario = self.obtener_binario(color_original)
        color_modificado = self.cambiar_ultimo_bit(color_binario, bit)
        return self.binario_a_decimal(color_modificado)

    def obtener_lista_de_bits(self, texto):
        lista = []
        for letra in texto:
            representacion_ascii = self.obtener_ascii(letra)
            representacion_binaria = self.obtener_binario(representacion_ascii)
            for bit in representacion_binaria:
                lista.append(bit)
        for bit in self.terminacion:
            lista.append(bit)
        return lista

    def ocultar_texto(self, mensaje, ruta_imagen_original, ruta_imagen_salida):
        print("Ocultando mensaje...".format(mensaje))
        imagen = Image.open(ruta_imagen_original)
        pixeles = imagen.load()

        tamaño = imagen.size
        anchura = tamaño[0]
        altura = tamaño[1]

        lista = self.obtener_lista_de_bits(mensaje)
        contador = 0
        longitud = len(lista)
        print("                       R    G    B")
        for x in range(anchura):
            for y in range(altura):
                if contador < longitud:
                    pixel = pixeles[x, y]

                    rojo = pixel[0]
                    verde = pixel[1]
                    azul = pixel[2]

                    if contador < longitud:
                        rojo_modificado = self.modificar_color(rojo, lista[contador])
                        contador += 1
                    else:
                        rojo_modificado = rojo

                    if contador < longitud:
                        verde_modificado = self.modificar_color(verde, lista[contador])
                        contador += 1
                    else:
                        verde_modificado = verde

                    if contador < longitud:
                        azul_modificado = self.modificar_color(azul, lista[contador])
                        contador += 1
                    else:
                        azul_modificado = azul

                    pixeles[x, y] = (rojo_modificado, verde_modificado, azul_modificado)
                    print("Colores originales:  ({}, {}, {})".format(rojo, verde, azul))
                    print("Colores modificados: ({}, {}, {})".format(rojo_modificado, verde_modificado, azul_modificado))
                else:
                    break
            else:
                continue
            break

        if contador >= longitud:
            print("Mensaje escrito correctamente.")
        else:
            print("Advertencia: no se pudo escribir todo el mensaje, sobraron {} caracteres.".format(math.floor((longitud - contador)/8)))
        
        print("Caracteres escritos {}".format(contador))
        imagen.save(ruta_imagen_salida)
