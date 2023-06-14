from clasecoleccioninterfaz import ColeccionInterfaz
class MiColeccion(ColeccionInterfaz):
    def __init__(self):
        self.coleccion = []

    def insertar_elemento(self, elemento, posicion):
        try:
            self.coleccion.insert(posicion, elemento)
        except IndexError:
            print("La posición no es válida")

    def agregar_elemento(self, elemento):
        self.coleccion.append(elemento)

    def mostrar_elemento(self, posicion):
        try:
            elemento = self.coleccion[posicion]
            print("Datos del elemento en la posición", posicion)
            print(elemento)
        except IndexError:
            raise Exception("La posición no es válida")'''