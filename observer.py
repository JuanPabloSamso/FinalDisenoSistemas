from abc import ABC, abstractmethod
from typing import List

# Interfaz Observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass

# Clase Blog (Sujeto Observable)
class Blog:
    def __init__(self, nombre: str):
        self._observadores: List[Observador] = []
        self._nombre = nombre

    def suscribir(self, observador: Observador):
        self._observadores.append(observador)

    def desuscribir(self, observador: Observador):
        self._observadores.remove(observador)

    def notificar(self, mensaje: str):
        for observador in self._observadores:
            observador.actualizar(mensaje)

    def publicar_articulo(self, titulo: str):
        mensaje = f"Nuevo artículo publicado en {self._nombre}: {titulo}"
        print(mensaje)
        self.notificar(mensaje)

# Observadores concretos
class SuscriptorEmail(Observador):
    def __init__(self, email: str):
        self._email = email

    def actualizar(self, mensaje: str):
        print(f"Enviando email a {self._email}: {mensaje}")

class SuscriptorSMS(Observador):
    def __init__(self, telefono: str):
        self._telefono = telefono

    def actualizar(self, mensaje: str):
        print(f"Enviando SMS al {self._telefono}: {mensaje}")

# Ejemplo de uso
def main():
    # Crear un blog
    mi_blog = Blog("Mi Blog de Tecnología")

    # Crear suscriptores
    suscriptor1 = SuscriptorEmail("usuario1@ejemplo.com")
    suscriptor2 = SuscriptorEmail("usuario2@ejemplo.com")
    suscriptor3 = SuscriptorSMS("+5492615374192")

    # Suscribir observadores
    mi_blog.suscribir(suscriptor1)
    mi_blog.suscribir(suscriptor2)
    mi_blog.suscribir(suscriptor3)

    # Publicar artículos
    mi_blog.publicar_articulo("Publicación1")
    mi_blog.publicar_articulo("Publicación2")

if __name__ == "__main__":
    main()