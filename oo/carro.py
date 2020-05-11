"""Voce deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes :

1) Motor
2) Direção

O Motor tera a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que devera incrementar a velocidade de uma unidade
3) Metodo frear que devera decrementar a velocidade em duas unidades

A Direção tera a responsabilidade de controlar a direção.Ela oferece os seguintes atributos:
1) Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste
2) Metodo girar a direita
3) Metodo girar a esquerda
   N
L    O
   S
   Exemplo:
   >>> #Testando motor
   >>> motor = Motor()
   >>> motor.velocidade
   0
   >>> motor.acelerar()
   >>> motor.velocidade
   1
   >>> motor.acelerar()
   >>> motor.velocidade
   2
   >>> motor.acelerar()
   >>> motor.velocidade
   3
   >>> motor.frear()
   >>> motor.velocidade
   1
   >>> motor.frear()
   >>> motor.velocidade
   0
   >>> #Testando direção
   >>> direção = Direção()
   >>> direção.valor
   'Norte'
   >>> direção.girar_a_direita()
   >>> direção.valor
   'Leste'
   >>> direção.girar_a_direita()
   >>> direção.valor
   'Sul'
   >>> direção.girar_a_direita()
   >>> direção.valor
   'Oeste'
   >>> direção.girar_a_direita()
   >>> direção.valor
   'Norte'
   >>> direção.girar_a_esquerda()
   >>> direção.valor
   'Oeste'
   >>> direção.girar_a_esquerda()
   >>> direção.valor
   'Sul'
   >>> direção.girar_a_esquerda()
   >>> direção.valor
   'Leste'
   >>> direção.girar_a_esquerda()
   >>> direção.valor
   'Norte'
   >>> carro = Carro (direção, motor)
   >>> carro.calcular_velocidade()
   0
   >>> carro.acelerar()
   >>> carro.calcular_velocidade()
   1
   >>> carro.acelerar()
   >>> carro.calcular_velocidade()
   2
   >>> carro.frear()
   >>> carro.calcular_velocidade()
   0
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.girar_a_direita()
   >>> carro.calcular_direcao()
   'Leste'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   'Oeste'
"""
class Carro:
    def __init__(self, direção, motor):
        self.motor = motor
        self.direção = direção

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direção.valor

    def girar_a_direita(self):
        self.direção.girar_a_direita()

    def girar_a_esquerda(self):
        self.direção.girar_a_esquerda()

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
class Direção:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade+=1
    def frear(self):
        self.velocidade-=2
        self.velocidade = max(0, self.velocidade)
