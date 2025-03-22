class Fracao:
  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador
    self.simplifica()

  def simplifica(self):
    def mdc(a, b):
      while b:
        a, b = b, a % b
        return a

      divisor = mdc(self.numerador, self.denominador)
      self.numerador //= divisor
      self.denominador //= divisor

    def __add__(self, outro):
        novo_numerador = self.numerador * outro.denominador + outro.numerador * self.denominador
        novo_denominador = self.denominador * outro.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __sub__(self, outro):
        novo_numerador = self.numerador * outro.denominador - outro.numerador * self.denominador
        novo_denominador = self.denominador * outro.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __mul__(self, outro):
        novo_numerador = self.numerador * outro.numerador
        novo_denominador = self.denominador * outro.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __truediv__(self, outro):
        novo_numerador = self.numerador * outro.denominador
        novo_denominador = self.denominador * outro.numerador
        return Fracao(novo_numerador, novo_denominador)

    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"


f1 = Fracao(4, 8)
f2 = Fracao(1, 3)
print(f1 + f2)  
print(f1 - f2)  
print(f1 * f2)  
print(f1 / f2)  