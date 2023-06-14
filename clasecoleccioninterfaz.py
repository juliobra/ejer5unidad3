from abc import ABC, abstractmethod

class ColeccionInterfaz(ABC):
    @abstractmethod
    def insertar_elemento(self, elemento, posicion):
        pass

    @abstractmethod
    def agregar_elemento(self, elemento):
        pass

    @abstractmethod
    def mostrar_elemento(self, posicion):
        pass