class Funcionario:
    def __init__(self, nome, CPF, salario, departamento):
        self.nome = nome
        self.CPF = CPF
        self.salario = salario
        self.departamento = departamento
    
    def bonificar_Funcionario(self):
        self.salario = (self.salario + (self.salario * (10 / 100)))
        return self.salario

    def imprime(self):
        print(f"Nome: {self.nome} CPF: {self.CPF} Salário: {self.salario} Departamento: {self.departamento}")

class Gerente(Funcionario):
    def __init__(self, nome, CPF, salario, departamento, senha, funcionarios):
        super().__init__(nome, CPF, salario, departamento)
        self.senha = senha
        self.funcionarios = funcionarios

    def bonificar_Gerente(self):
        self.salario = (self.salario + (self.salario * (15 / 100)))
        return self.salario 
    
    def verificar_senha(self, senha_informada):
        if self.senha == senha_informada:
            return "Senha correta"
        else:
            return "Senha incorreta"

    def imprime(self):
        print(f"Nome: {self.nome} CPF: {self.CPF} Salário: {self.salario} Departamento: {self.departamento}")

funcionarios = [
    Funcionario('Ana Silva', '123.456.789-00', 3500.00, 'Vendas'),
    Gerente('Carlos Souza', '987.654.321-00', 4200.00, 'Marketing', 34556789, 5),
    Funcionario('Fernanda Oliveira', '555.666.777-88', 5000.00, 'TI'),
    Funcionario('João Pereira', '111.222.333-44', 3700.00, 'RH'),
    Gerente('Mariana Costa', '444.555.666-77', 4600.00, 'Financeiro', 34556789, 5)
]

senha_informada = 34556789

for funcionario in funcionarios:
    funcionario.imprime()
    
    if isinstance(funcionario, Gerente):
        print(funcionario.verificar_senha(senha_informada))
    print("-" * 80)
