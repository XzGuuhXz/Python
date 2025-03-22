class ContaCorrente:
  def __init__(self, numero:int, titular:str, saldo:float = 0.0, limite:float = 0.0):
    self.numero = numero
    self.titular = titular
    self.saldo = saldo
    self.limite = limite

  @property
  def numero(self):
    return self.__numero

  @numero.setter
  def numero(self, numero:int):
    self.__numero = numero
  
  @property
  def titular(self):
    return self.__titular
  
  @titular.setter
  def titular(self, titular):
    self.__titular = titular

  @property
  def saldo(self):
    return self.__saldo
  
  @saldo.setter
  def saldo(self, saldo):
    if(saldo < 0.0):
      print("o saldo não sera alterado, saldo minimo 0.0")
      return
    self.__saldo = saldo
  
  @property
  def limite(self):
    return self.__limite
  
  @limite.setter
  def limite(self, limite):
    if(limite < 0.0):
      print("o limite sera será 0.0")
      self.__limite = 0.0
      return
    self.__limite = limite
  
  def sacar(self, valor):
    if(self.saldo < valor):
      print('não é possivel efetuar o saque')
      return
    self.saldo -= valor

  def depositar(self, valor:float):
    self.saldo += valor
  
  def transferir(self, valor, destino: 'ContaCorrente'):
    if(self.saldo < valor or valor > self.limite):
      print('falha na transferencia:saldo insuficiente')
      return
    else:
      destino.saldo += valor
      self.saldo -= valor


um = ContaCorrente(1,'Fulano',4,2)
dois = ContaCorrente(2, 'Gustavo', 100, 100)

um.sacar(5)
um.transferir(5, dois)
um.transferir(2, dois)
um.depositar(9)
print(um.saldo)
print(dois.saldo)



    