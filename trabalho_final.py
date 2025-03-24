import random

class Robo:
    nivel_critico = 0.60

    def __init__(self, nome: str):
        self.nome = nome
        self.vida = random.uniform(0, 1)

    def __repr__(self):
        return f"{self.__class__.__name__}(nome={self.nome}, vida={self.vida:.2f})"

    def __add__(self, outro):
        nome_pai = self.nome.split('-')[0]
        nome_mae = outro.nome.split('-')[0]
        novo_nome = f"{nome_pai}-{nome_mae}"
        return type(self)(novo_nome)

    def precisa_de_medico(self):
        return self.vida < self.nivel_critico

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        self._vida = max(0, min(1, value))
        
class RoboMedico(Robo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder_de_cura = random.uniform(0, 1)

    def curar(self, outro_robo: Robo):
        if self.vida >= outro_robo.vida and outro_robo.vida < 1:
            outro_robo.vida += self.poder_de_cura
            outro_robo.vida = min(outro_robo.vida, 1)
            print(f"{self.nome} curou {outro_robo.nome}!")
        else:
            print(f"{self.nome} não pode curar {outro_robo.nome}.")
            
class RoboLutador(Robo):
    dano_maximo = 0.2

    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder = random.uniform(self.dano_maximo, 1)

    def atacar(self, outro_robo: Robo):
        dano = 1 - self.poder
        outro_robo.vida *= dano
        print(f"{self.nome} atacou {outro_robo.nome}! Vida restante: {outro_robo.vida:.2f}")

        if isinstance(outro_robo, RoboLutador):
            outro_robo.contra_atacar(self)

    def contra_atacar(self, outro_robo: Robo):
        dano = 1 - self.poder
        outro_robo.vida *= dano
        print(f"{self.nome} contra-atacou {outro_robo.nome}! Vida restante: {outro_robo.vida:.2f}")
        
def main():
    robos = [Robo(f"Robo{i}") for i in range(3)]
    robos_medicos = [RoboMedico(f"Medico{i}") for i in range(2)]
    robos_lutadores = [RoboLutador(f"Lutador{i}") for i in range(2)]

    todos_robos = robos + robos_medicos + robos_lutadores

    for robo in todos_robos:
        print(robo)

    for i in range(5):
        atacante = random.choice(robos_lutadores)
        defensor = random.choice([r for r in todos_robos if r != atacante])
        atacante.atacar(defensor)

        if defensor.vida < 0.1:
            print(f"{defensor.nome} está em perigo! Chamando um médico...")
            medico = random.choice(robos_medicos)
            if random.random() < 0.5:
                medico.curar(defensor)
            else:
                print(f"{medico.nome} ignorou o chamado.")

    filho = robos_lutadores[0] + robos_medicos[0]
    print(f"Novo robô nascido: {filho}")

if __name__ == "__main__":
    main()
