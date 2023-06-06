import math
from Carro import Carro

#TODO:validar placa!
#TODO:Verificar se o lugar esta vago

brasil = {
    "Mato Grosso do Sul": [["HQF", "HTW"], ["NRF", "NSD"], ["OOG", "OOU"], ["QAA", "QAZ"], ["REW", "REZ"], ["RWA", "RWJ"]],
    "Mato Grosso":[["JXZ", "KAU"], ["NIY", "NJW"], ["NPC", "NPQ"], ["NTX", "NUG"], ["OAP", "OBS"], ["QBA", "QCZ"], ["RAK", "RAZ"], ["RI", "RRZ"]],
    "Tocantins":[["MVL", "MXG"], ["OLH", "OLN"], ["OYA", "OYC"], ["QKA", "QKM"], ["QWA", "QWF"], ["RSA", "RSF"]]
}

    
alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Convert(string):
    total = 0
    posicao = len(string)-1
    for i in string:
        total+=alf.index(i)
        len(alf)*posicao
        posicao -= 1
    return total

def SearchState(plaque):
    value = Convert(plaque[:3])
    for state in brasil:
        for limit in brasil[state]:
            min_value, max_value = Convert(limit[0]), Convert(limit[1])
            if min_value <= value <= max_value:
                return state
    return None

class Estacionamento:
    contador = 0
    carros = [[]]
    placaReg = {}
    
    def __init__(self, m, n):
        self.contador = m * n
        self.carros = [[0] * n]*m
        print(self.carros)
        
    
    def registrarCarro(self):
        #TODO:validar placa!
        #validador(placa)
        posX = int(input("Informe a posição na fileira: "))
        posY = int(input("Informe a posição na coluna: "))
        if (posX * posY) < self.contador:
            if self.carros[posX -1][posY - 1] != 0:
                print("Lugar Ocupado!")
                return
            carroNome = input("Modelo do carro: ")
            placa = input("Placa do carro: ").upper()
            estado = ""
            estado = SearchState(placa)
            if SearchState(placa) == None:
                 estado = "Fora da zona 4"
            temp = Carro(carroNome, posX , posY, placa, estado)
            self.placaReg.update({placa:temp})
            self.carros[posX - 1][posY - 1] = temp
        elif posX < 0 or posY < 0:
            print("ERROR: POSIÇÂO NÂO EXISTE")
        else:
            print("ERROR: POSIÇÂO NÂO EXISTE")
        
    def retirarCarro(self, placa):
        horas = int(input("Quantas horas: "))
        minutos = float(input("Quantos minutos: "))
        
        if horas < 0 or minutos < 0:
            print("ERROR:Valor invalido!")
            return
        
        while(minutos > 59):
            horas = horas + 1
            minutos = minutos - 60
        
        minutos = minutos * 0.01
        tempoTotal = horas + minutos
        print(tempoTotal)
        if tempoTotal <= 0.15:
            print("Preço a se pagar: R$ 0,00")
        elif tempoTotal > 0.15 and tempoTotal < 3:
            print("Preço a se pagar: R$ 5,00")
        elif tempoTotal > 3:
            val = 5 + (10 * (math.ceil(tempoTotal) - 3))
            print("VALOR A SE PAGAR: ", val)
            self.printCarros(placa)
        
        self.carros[self.placaReg[placa].posX - 1][self.placaReg[placa].posY - 1] = 0
        temp = self.placaReg.pop(placa)
        return temp
        
    def printCarros(self, placa):
        print("PLACA: ", self.placaReg[placa].placa)
        print("CARRO: ", self.placaReg[placa].nome)
        print("POS DA VAGA: X(", self.placaReg[placa].posX , "), Y(" , self.placaReg[placa].posY ,")")
        print("ESTADO: ", self.placaReg[placa].estado)
        
    def ApresentarCarros(self):
         for carro in self.placaReg:
             print(carro)
        
    pass