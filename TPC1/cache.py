class Cache:
    tabela = []

    def add(self, str):
        lines = str.split(",")
        if (len(lines) > 5):
            if lines[0].isdigit():
                if lines[1] == "F" or lines[1] == "M":
                    if lines[2].isdigit() and int(lines[2]) > 0:
                        if lines[3].isdigit() and int(lines[3]) >= 0:
                            if lines[4].isdigit() and int(lines[4]) > 0:
                                if lines[5].isdigit() and (int(lines[5]) == 0 or int(lines[5]) == 1):
                                    self.tabela.append(lines)

    def print(self):
        for line in self.tabela:
            print(";".join(line))

    def exc1(self):
        homens = 0
        muheres = 0
        for pessoa in self.tabela:
            if pessoa[1] == "M" and pessoa[5] == "1":
                homens += 1
            elif pessoa[1] == "F" and pessoa[5] == "1":
                muheres += 1
        print("---------------------------------")
        print("|Distribuição da doença por sexo|\n|Homens| " + str(
            (homens / (homens + muheres)) * 100) + "%     |" + "\n|Mulheres| " + str(
            (muheres / (homens + muheres)) * 100) + "%   |")
        print("---------------------------------")

    def exc2(self):
        distribuicoes = []
        soma = 0
        for pessoa in self.tabela:
            if int(pessoa[0]) >= 30 and pessoa[5] == "1":
                for i in range(int(pessoa[0]) // 5 - len(distribuicoes) - 5):
                    distribuicoes.append(0)
                idade = int(pessoa[0])
                distribuicoes[idade // 5 - 6] += 1
                soma += 1
        print("---------------------------------------------")
        print("|Distribuição da doença por escalões etários|")
        i = 6
        for ele in distribuicoes:
            print("[" + str(5 * i) + "-" + str(5 * i + 4) + "]| " + str(round(((ele / soma) * 100), 2)) + "%                              |")
            i += 1
        print("---------------------------------------------")

    def exc3(self):
        distribuicoes = {}
        soma = 0
        for pessoa in self.tabela:
            if pessoa[5] == "1":
                colestrol = int(pessoa[3]) // 10
                if colestrol in distribuicoes:
                    distribuicoes[colestrol] += 1
                else:
                    distribuicoes[colestrol] = 1
                soma += 1
        print("-----------------------------------------------")
        print("|Distribuição da doença por nível de colestrol|")
        chaves = distribuicoes.keys()

        for ele in sorted(chaves):
            print("|[" + str(ele * 10) + "-" + str(10 * ele + 10) + "]| " + str(round(((distribuicoes[ele] / soma) * 100),2)) + "%                              |")
        print("-----------------------------------------------")
