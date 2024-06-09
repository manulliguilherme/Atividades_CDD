class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormindo = False
        self.falando = False

    def comer(self, alimento = " "):
        if self.dormindo:
            print(f"{self.nome} está dormindo, logo não está comendo")
        elif self.falando:
            print(f"{self.nome} está falando, logo não está comendo")
        else:
            self.comendo = True
            self.dormindo = False
            self.falando = False
            print(f"{self.nome} está comendo {alimento}")

    def falar(self,falar = " "):
        if self.comendo:
            print(f"{self.nome} está comendo, logo não está falando")
        elif self.dormindo:
            print(f"{self.nome} está dormindo, logo não está falando")
        else:
            self.falando = True
            self.comendo = False
            self.dormindo = False
            print(f"{self.nome} está falando '{falar}' ")
    def dormir(self):
        if self.comendo:
            print(f"{self.nome} está comendo, logo não está dormindo")
        elif self.falando:
            print(f"{self.nome} está falando, logo não está dormindo")
        else:
            self.dormindo = True
            self.comendo = False
            self.falando = False
            print(f"{self.nome} está dormindo")

p1 = Pessoa("Alice", 68, 36)


p1.dormir()
p1.falar("Au revoir")
p1.comer("Pizza")






