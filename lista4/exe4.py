class SuperLista:
    def __init__(self):
        self.lista = []

    def __gt__(self, elemento):
        self.lista.append(elemento)

    def __repr__(self):
        if not self.lista:
            return "Lista vazia"
        return "\n".join(f"[{i}] = {elem}" for i, elem in enumerate(self.lista))


lis = SuperLista()
print(lis)  
lis > 10
lis > 'Adoro programar'
lis > 42
print(lis)
