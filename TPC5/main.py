import sys
import re

class programa:

    moedas={"5c": 0, "10c": 0, "20c": 0, "50c": 0, "1e": 0, "2e": 0}
    saldo = 0
    estado=""

    def calculaSaldo(self):
        for key in self.moedas.keys:
            self.saldo += int(re.fullmatch(r'(/d+)[ce]', key).group(1)) * self.moedas[key]

    def clearMoedas(self):
        for key in self.moedas.keys():
            self.moedas[key] = 0

    def run(self):
        expMoedas = r'MOEDA (?:(\d+[c|e]),*)+'
        erMoedas = re.compile(expMoedas)
        for input in sys.stdin:
            matchMoedas = erMoedas.fullmatch(input)
            input = input.strip()
            if input == "LEVANTAR":
                self.estado = "levantar"
                print("maq: Introduza Moedas")
            elif self.estado == "levantar" and matchMoedas:
                resposta = ""
                for elem in erMoedas.findall(input):
                    nome = erMoedas.search(elem).group(1)
                    if nome not in self.moedas.keys():
                        resposta += "Moeda invalida: " + nome + ";"
                    else:
                        self.moedas[nome] += 1
                self.calculaSaldo()
                respostaF = "maq: " + resposta + "O saldo total e: " + str(self.saldo)
                print(respostaF)

            else:
                print("introduza uma opcao valida")

if __name__ == '__main__':
    programa = programa()
    programa.run()