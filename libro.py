from persona import Persona

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha):
        self._titulo = titulo
        self._autor = autor  # objeto Persona
        self._isbn = isbn
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._ciudad = ciudad
        self._pais = pais
        self._fecha = fecha 
