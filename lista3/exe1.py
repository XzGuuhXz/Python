class datas:
    def __init__ (self, dia:int, mes:int, ano:int):
        self.mes = mes
        self.ano = ano
        self.dia = dia

    @property
    def dia(self) -> int:
        return self.__dia

    @dia.setter
    def dia(self, dia:int):
        if (((dia < 1) or (dia > 31)) or ((self.mes == 2) and (dia > 28))):
            self.__dia = 0
        else:
            self.__dia = dia

    @property
    def mes(self) -> int:
        return self.__mes

    @mes.setter
    def mes(self, mes:int):
        if((mes < 1) or (mes > 12)):
            self.__mes = 0
        else:
            self.__mes = mes
    
    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano:int):
        if(ano < 1):
            self.__ano = 0
        else:
            self.__ano = ano

    def __str__(self) -> str:
        return f"{self.dia}/{self.mes}/{self.ano}"


    def avanca(self):
        if(self.dia < 27):
            self.dia += 1
        if((self.mes == 2) or (self.dia == 28)):
            self.dia = 1
            self.mes += 1
        if((self.mes == 12) or (self.dia > 31)):
            self.dia = 1
            self.mes = 1
            self.ano +=1
        return 
    

datas_teste =[
    datas(31, 1, 2024),
    datas(15, 3, 2023), 
    datas(30, 4, 2025), 
    datas(1, 12, 2020), 
    datas(31, 8, 2021), 
    datas(28, 2, 2022),
    datas(15, 6, 2019),  
    datas(31, 10, 2023), 
    datas(1, 9, 2020),   
]

for data in datas_teste:
    print(f"Data inicial: {data}")
    data.avanca()  
    print(f"Data após avanço: {data}\n")