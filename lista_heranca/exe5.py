class Pagamento:
    def __init__(self, valor:float, data:str):
        self.valor = valor
        self.data = data
        
    def ppagamento(self):
        return print(f"Processando Pagamento Generico\n\nValor: {self.valor} Data: {self.data}\n")      
                
class PagamentoCartao(Pagamento):
    def __init__(self, ncartao:str, validade:str, valor:float, data:str):
        super().__init__(valor, data)
        self.ncartao = ncartao
        self.validade = validade

    @property
    def ncartao(self):
        return self.__ncartao
    
    @ncartao.setter
    def ncartao(self, ncartao) -> None:
        self.__ncartao = ncartao

    @property
    def valide(self):
        return self.__validade
    
    @valide.setter
    def validade(self, validade) -> None:
        self.__validade = validade
        
    def ppagamento(self):
        return print(f"Pagamento realizado via cartão\n\nNumero do cartão:{self.ncartao} Validade: {self.validade} Valor: {self.valor} Data: {self.data}\n")
                        
class PagamentoPix(Pagamento):
    def __init__(self, cpix:str, valor:float, data:str):
        super().__init__(valor, data)
        self.cpix = cpix
        
    def ppagamento(self):
        return print(f"Pagamento realizado via Pix\n\nPix: {self.cpix}Valor: {self.data}Data: {self.valor}\n")


def main():

    pagamento_generico = Pagamento(100.0, "01/01/2022")
    pagamento_generico.ppagamento()


    pagamento_cartao = PagamentoCartao("1234567890123456", "12/23", 150.0, "02/02/2022")
    pagamento_cartao.ppagamento()


    pagamento_pix = PagamentoPix("12345", 200.0, "03/03/2022")
    pagamento_pix.ppagamento()

if __name__ == "__main__":
    main()
