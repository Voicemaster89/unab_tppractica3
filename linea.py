from punto import punto 

class linea:
  def __init__(self , punto_a, punto_b):
    self._punto_a =punto_a
    self._punto_b =punto_b 

  def mueve_derecha(self, distancia):
    self._punta_a.x += distancia
    self._punta_b.x += distancia

  def mueve_izquierda(self, distancia):
    self._punto_a.x -= distancia
    self._puntoa_b.x -= distancia

  def mover_hacia_arriba(self, distancia):
    self._punto_a.y += distancia
    self._punto_b.y += distancia

  def mover_hacia_abajo(self, distancia):
    self._punto_a.y -= distancia
    self._punto_b.y -= distancia 
