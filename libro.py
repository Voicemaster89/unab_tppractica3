from persona import Persona

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._ciudad = ciudad
        self._pais = pais
        self._fecha = fecha

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        self._autor = autor

    def leer_la_informacion(self):
        self._titulo = input("Título: ")
        nombre_autor = input("Autor: ")
        self._autor = Persona(nombre_autor)
        self._isbn = input("ISBN: ")
        self._paginas = int(input("Páginas: "))
        self._edicion = input("Edición: ")
        self._editorial = input("Editorial: ")
        self._ciudad = input("Ciudad: ")
        self._pais = input("País: ")
        self._fecha = input("Fecha: ")

    def mostrar_la_informacion(self):
        print(f"Título: {self._titulo} {self._edicion}")
        print(f"Autor: {self._autor}")
        print(f"ISBN: {self._isbn}")
        print(f"{self._editorial}, {self._ciudad} ({self._pais})")
        print(f"{self._fecha}")
        print(f"{self._paginas} páginas")
