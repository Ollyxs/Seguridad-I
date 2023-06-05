from PIL import Image

class Leer():
    terminacion = "11111111"
    def obtener_lsb(self, byte):
        return byte[-1]

    def obtener_binario(self, numero):
        return bin(numero)[2:].zfill(8)

    def binario_a_decimal(self, binario):
        return int(binario, 2)

    def caracter_desde_codigo_ascii(self, numero):
        return chr(numero)

    def leer(self, ruta_imagen):
        imagen = Image.open(ruta_imagen)
        pixeles = imagen.load()

        tamaño = imagen.size
        anchura = tamaño[0]
        altura = tamaño[1]

        byte = ""
        mensaje = ""

        for x in range(anchura):
            for y in range(altura):
                pixel = pixeles[x, y]

                rojo = pixel[0]
                verde = pixel[1]
                azul = pixel[2]


                byte += self.obtener_lsb(self.obtener_binario(rojo))
                if len(byte) >= 8:
                    if byte == self.terminacion:
                        break
                    mensaje += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""

                byte += self.obtener_lsb(self.obtener_binario(verde))
                if len(byte) >= 8:
                    if byte == self.terminacion:
                        break
                    mensaje += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""

                byte += self.obtener_lsb(self.obtener_binario(azul))
                if len(byte) >= 8:
                    if byte == self.terminacion:
                        break
                    mensaje += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""

            else:
                continue
            break
        return mensaje
