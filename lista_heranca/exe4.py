class ContaBancaria:
    def __init__(self, nome: str, saldo: float):
        self.nome = nome
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor: float) -> None:
        self.__saldo = valor
        
    def depositar(self, valor: float):
        if valor <= 0:
            print("Valor de depósito inválido!")
        else:
            self.saldo += valor
            print(f"Depósito de {valor}. Novo saldo: {self.saldo}")
    
    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor de saque inválido!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de {valor}. Novo saldo: {self.saldo}")
            
    def __str__(self):
        return f"(Nome da conta: {self.nome}, Saldo: {self.saldo})"
        

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo: float, nome: str, cheque: float):
        super().__init__(nome, saldo)
        self.__cheque = cheque
    
    @property
    def cheque(self):
        return self.__cheque
    
    @cheque.setter
    def cheque(self, valor: float) -> None:
        self.__cheque = valor
    
    def saldo_total(self):
        return self.saldo + self.cheque

    def sacar(self, valor: float):
        if valor > self.saldo_total():
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de {valor}. Novo saldo: {self.saldo}, Cheque especial restante: {self.cheque}")
    
    def __str__(self):
        return f"(Nome da conta: {self.nome}, Saldo: {self.saldo}, Cheque Especial: {self.cheque})"
        

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo: float, nome: str, taxa: float):
        super().__init__(nome, saldo)
        self.__taxa = taxa
        
    @property
    def taxa(self):
        return self.__taxa
    
    @taxa.setter
    def taxa(self, valor: float) -> None:
        self.__taxa = valor
    
    def aplicar_juros(self):
        self.saldo += self.saldo * (self.taxa / 100)
        print(f"Juros aplicados: {self.taxa}%. Novo saldo: {self.saldo}")
    
    def __str__(self):
        return f"(Nome da conta: {self.nome}, Saldo: {self.saldo}, Taxa de Juros: {self.taxa}%)"

lista_contas = [
    ContaBancaria("João", 1000),
    ContaBancaria("Maria", 500),
    ContaBancaria("Carlos", 0),
    ContaBancaria("Ana", -100),
    ContaCorrente(1500, "Lucas", 500),
    ContaCorrente(2000, "Pedro", 1000),
    ContaPoupanca(3000, "Fernanda", 5),
    ContaPoupanca(1000, "Gustavo", 10),
    ContaCorrente(800, "Juliana", 300),
    ContaPoupanca(2000, "Rodrigo", 3)
]

for conta in lista_contas:
    print(conta)
    if isinstance(conta, ContaBancaria):
        conta.depositar(500)
        conta.sacar(200)
    
    if isinstance(conta, ContaCorrente):
        conta.sacar(1000)
    
    if isinstance(conta, ContaPoupanca):
        conta.aplicar_juros()
    
    print("-" * 50)
