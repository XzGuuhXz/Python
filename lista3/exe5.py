class pais:
  def __init__(self, codigo:str, nome:str, populacao:int, dimensao:float, fronteiras:list):
    self.codigo = codigo
    self.nome = nome
    self.dimensao = dimensao
    self.populacao = populacao
    self.fronteiras = fronteiras

  @property
  def codigo(self):
    return self.__codigo
  
  @codigo.setter
  def codigo(self, codigo:str):
    self.__codigo = codigo

  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome:str):
    self.__nome = nome
  
  @property
  def populacao(self):
    return self.__populacao
  
  @populacao.setter
  def populacao(self, populacao:int):
    self.__populacao = populacao
  
  @property
  def dimesao(self):
    return self.__dimensao
  
  @dimesao.setter
  def dimensao(self, dimensao:float):
    if(dimensao < 0.0):
      print('a dimensao nao pode ser menor que zero')
      self.__dimensao = 0.0
      return
    self.__dimensao = dimensao
  
  @property
  def fronteiras(self):
    return self.__fronteiras

  @fronteiras.setter
  def fronteiras(self, fronteiras:list):
    self.__fronteiras = fronteiras

  def densidade(self):
    return self.populacao/self.dimensao
  
  def vizinhos_comuns(self, pais: 'pais'):
    return list(set(self.fronteiras) & set(pais.fronteiras))
  

um = pais('BRA','brasil', 3, 2.0, ['argentina', 'paragui', 'chile'])
dois = pais('py', 'paraguai', 4, 1.0, ['argentina', 'brasil', 'bolivia'])
print(um.vizinhos_comuns(dois))
print(um.densidade())