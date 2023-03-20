import sys
import re

class Programa:

    moedas = {"5c": 0, "10c": 0, "20c": 0, "50c": 0, "1e": 0, "2e": 0}
    saldo = 0
    estado = "pousado"

    def calculaSaldo(self):
        for key in self.moedas.keys():
            match = re.search(r'(\d+)([ce])', key)
            if match:
                valor = int(match.group(1))
                letra = match.group(2)
                if letra == "c":
                    self.saldo += valor * self.moedas[key] / 100
                elif letra == "e":
                    self.saldo += valor * self.moedas[key]

    def clearMoedas(self):
        for key in self.moedas.keys():
            self.moedas[key] = 0

    def run(self):
        expMoedas = r'MOEDA (?:(\d+[c|e]),* *)+'
        expTelefone = r'T=(\d{9})'
        erMoedas = re.compile(expMoedas)
        erTelefone = re.compile(expTelefone)
        for input in sys.stdin:
            input = input.strip()
            matchMoedas = erMoedas.fullmatch(input)
            matchTel = erTelefone.fullmatch(input)
            if input == "LEVANTAR":
                self.estado = "levantar"
                print("maq: Introduza Moedas")
            elif self.estado == "levantar" and matchMoedas:
                resposta = ""
                for elem in re.findall(r"(\d+[ce])", input):
                    if elem not in self.moedas.keys():
                        resposta += "Moeda invalida: " + elem + ";"
                    else:
                        self.moedas[elem] += 1
                self.calculaSaldo()
                respostaF = "maq: " + resposta + " O saldo total e: " + str(self.saldo)
                print(respostaF)
                self.estado = "Telefonar"
            elif self.estado == "Telefonar" and matchTel:
                num = erTelefone.search(input).group(1)
                if re.match(r'601(\d{6})', num) or re.match(r'641(\d{6})', num):
                    print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")
                elif re.match(r'2(\d{8})'):
                    


            else:
                print("introduza uma opcao valida")

if __name__ == '__main__':
    programa = Programa()
    programa.run()
