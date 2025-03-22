class FormaGeometrica:
    def __init__(self, area:float, perimeto:float):
        self.area = area
        self.perimeto = perimeto

    def calculararea(self):
         if isinstance(self, Retangulo):
            self.area = self.base * self.altura 
        
    def calcularperimeto(self):
        if isinstance(self, Triangulo):
            self.perimeto = self.area + self.perimeto + self.area + self.perimeto
                
class Retangulo(FormaGeometrica):
    def __init__(self, area, perimeto,altura:float, base:float):
        super().__init__(area, perimeto)
        self.base = base 
        self.altura = altura             
        

class Triangulo(FormaGeometrica):
    def __init__(self, lado1:float, lado2:float, lado3:float):
        super().__init__():
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3