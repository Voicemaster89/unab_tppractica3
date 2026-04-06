class punto:
  def __int__:(self, x, y):
    self.x= x
    self.y= y
    
  def eje_X(self):
    return self.x

  def eje_y(self):
    return self.y

  def impresion(self):
    return f"{(self.x}, {self.y})"

  def opuesto(self):
    return punto(- self.x, -self.y) 

  def esta_en_eje_y(self):
    return self.y == 0
