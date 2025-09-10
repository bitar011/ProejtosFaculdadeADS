#Classe:
#class Pessoa:
#    def __init__(self, nome, idade, genero):
#        self.nome = nome
#        self.idade = idade
#        self.genero = genero
#    def cumprimentar(self):
#        return f"Olá, meu nome é {self.nome}."
#    def aniversario(self):
#        self.idade += 1

#pessoa1 = Pessoa("Victor", 19, "Masculino")

#print(pessoa1.cumprimentar())
#print(f"Idade: {pessoa1.idade}")
#pessoa1.aniversario()
#print(f"Nova idade: {pessoa1.idade}")

#------------------------------------------
#Heranças
#class Animal:
#    def __init__(self, nome):
#        self.nome = nome
#    def fazer_barulho(self):
#        pass
#class cachorro(Animal):
#    def fazer_barulho(self):
#        return "Latir"
#class gato(Animal):
#    def fazer_barulho(self):
#        return "Miar"

#Thor = cachorro("Thor")
#Bruce = gato("Bruce")
#print(f"{Thor.nome} faz: {Thor.fazer_barulho()}")
#print(f"{Bruce.nome} faz: {Bruce.fazer_barulho()}")

#-----------------------------------------------------
#Prática geral:
class Veiculo:#classe pai
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    def acelerar(self, incremento):
        self.velocidade += incremento
    def frear(self, decremento):
        self.velocidade -= decremento
    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, velocidade: {self.velocidade} km/h"
#classe filha1    
class carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia
    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia
#classe filha2
class bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo
    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, velocidade: {self.velocidade} km/h"
#objetos:
carro1 = carro("320i", "BMW", 2020, 120)
bicicleta1 = bicicleta("Trek", "Mountain Bike", 2021, "MTB")
#acelerando e verificanto status:
carro1.acelerar(60)
bicicleta1.acelerar(25)

print("Status do carro:")
print(carro1.status())
print("Status da bicicleta:")
print(bicicleta1.status())

#anotações gerais feitas em caderno