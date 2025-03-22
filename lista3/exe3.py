from math import sqrt, pi

class Ponto2D:
    def __init__(self, X: float = 0.0, Y: float = 0.0):
        self.x = X
        self.y = Y

    @property
    def X(self) -> float:
        return self.x
    
    @X.setter
    def X(self, X: float):
        self.x = X

    @property
    def Y(self) -> float:
        return self.y
    
    @Y.setter
    def Y(self, Y: float):
        self.y = Y

    def compara(self, ponto: 'Ponto2D') -> bool:
        return self.x == ponto.x and self.y == ponto.y
    
    def __str__(self) -> str:
        return f"Ponto({self.x}, {self.y})"
    
    def calcule(self, ponto: 'Ponto2D') -> float:
        return sqrt((ponto.x - self.x) ** 2 + (ponto.y - self.y) ** 2)
    
    def clone(self):
        return Ponto2D(self.x, self.y)

class Circulo:
    def __init__(self, raio: float, centro: Ponto2D = None):
        self.raio = raio
        self.centro = centro if centro else Ponto2D(0.0, 0.0)

    @property
    def raio(self) -> float:
        return self.__raio
    
    @raio.setter
    def raio(self, raio:float):
        self.__raio = raio

    @property
    def centro(self) -> Ponto2D:
        return self.__centro
    
    @centro.setter
    def centro(self, centro: Ponto2D):
        self.__centro = centro
    
    def inflar(self, valor: float):
        self.raio += valor

    def desinflar(self, valor: float):
        self.raio -= valor

    def mover_para_origem(self):
        self.centro = Ponto2D(0.0, 0.0)

    def mover_para_ponto(self, ponto: Ponto2D):
        self.centro = ponto

    def retorne_area(self) -> float:
        return pi * self.raio ** 2
        
    def __str__(self) -> str:
        return f"Circulo(Centro: {self.centro}, Raio: {self.raio})"

def main():
    ponto1 = Ponto2D(3, 4)
    ponto2 = Ponto2D(5, 6)

    circulo1 = Circulo(1)
    print("Círculo 1:", circulo1)

    circulo1.mover_para_ponto(ponto1)
    print("Círculo 1 movido para ponto1:", circulo1)

    area1 = circulo1.retorne_area()
    print("Área do Círculo 1:", area1)

    circulo2 = Circulo(2, ponto2)
    print("Círculo 2:", circulo2)

    circulo2.mover_para_origem()
    print("Círculo 2 movido para a origem:", circulo2)

    area2 = circulo2.retorne_area()
    print("Área do Círculo 2:", area2)

if __name__ == "__main__":
    main()
