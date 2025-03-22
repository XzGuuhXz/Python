class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, ponto):
        return Ponto(self.x + ponto.x, self.y + ponto.y)

    def __sub__(self, ponto):
        return Ponto(self.x - ponto.x, self.y - ponto.y)

    def __mul__(self, ponto):
        return self.x * ponto.x + ponto.y * ponto.y

    def __rmul__(self, escalar):
        return Ponto(escalar * self.x, escalar * self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
print(p1 + p2)  
print(p1 - p2)  
print(p1 * p2)  
print(2 * p1)   