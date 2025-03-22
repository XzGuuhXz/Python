from math import sqrt
class Ponto2D:
    def __init__(self, X:float = 0.0, Y:float = 0.0):
        self.x = X
        self.y = Y

    @property
    def X(self) -> float:
        return self.__x
    
    @X.setter
    def X(self, X:float):
        self.__x = X

    @property
    def Y(self) -> float:
        return self.__y
    
    @Y.setter
    def Y(self, Y:float):
        self.__y = Y

    def compara(self, ponto:'Ponto2D'):
        if((self.x == ponto.x) and (self.y == ponto.y)):
            return True
        return False
    
    def __str__(self) -> str:
        return f"{self.x},{self.y}"
    
    def calcule(self, ponto: 'Ponto2D') -> float:
        return (sqrt(((ponto.x - self.x) ** 2) + ((ponto.y - self.y)**2)))
    
    def clone(self):
        return Ponto2D(self.x, self.y)
    
    def __str__(self) -> str: 
        return f"Ponto({self.x}, {self.y})"
    
def main():
    ponto1 = Ponto2D(2, 3) 
    ponto2 = Ponto2D(5, 7) 

    print("Ponto 1:", ponto1)
    print("Ponto 2:", ponto2) 

    distancia = ponto1.calcule(ponto2)
    print("Distância entre Ponto 1 e Ponto 2:", distancia) 

    ponto_clonado = ponto1.clone()
    print("Ponto Clonado:", ponto_clonado)

    iguais = ponto1.compara(ponto_clonado)
    print("Ponto 1 é igual ao Ponto Clonado?", iguais) 

    diferentes = ponto1.compara(ponto2)
    print("Ponto 1 é igual ao Ponto 2?", diferentes)

if __name__ == "__main__":
    main()