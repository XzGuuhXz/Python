class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def __lt__(self, outro):
        return self.area() < outro.area()

    def __gt__(self, outro):
        return self.area() > outro.area()

    def __eq__(self, outro):
        return self.area() == outro.area()

    def __repr__(self):
        return f"Retangulo(largura={self.largura}, altura={self.altura})"


r1 = Retangulo(3, 4)  
r2 = Retangulo(2, 6)  
r3 = Retangulo(5, 2)  
print(r1 == r2)  
print(r1 > r3)   
print(r3 < r2)   
