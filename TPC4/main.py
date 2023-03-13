import re
import json
dicts = []


def parserFile(file):
    exp = r"(\w+(?:{\d+}|{\d+,\d+})*(?:::\w+)*)"
    rexp = re.compile(exp)
    exp1 = r"(?P<param>\w+)({(\d+)}|{(\d+,\d+)})*(?:::(\w+))*"
    rexp1 = re.compile(exp1)
    f = open(file, "r")
    i = 0
    cabecalho = {}
    nomes = []
    lines = f.read().split('\n')
    for line in lines:
        if i == 0:
            for elem in rexp.findall(line):
                param = rexp1.search(elem).group(1)
                if rexp1.search(elem).group(3) is None and rexp1.search(elem).group(4) is not None:
                    if rexp1.search(elem).group(5) is not None:
                        cabecalho[param] = rexp1.search(elem).group(4).split(",")
                        cabecalho[param] = cabecalho[param] + [rexp1.search(elem).group(5)]
                    else:
                        cabecalho[param] = rexp1.search(elem).group(4).split(",")
                else:
                    cabecalho[param] = rexp1.search(elem).group(3)
                    if rexp1.search(elem).group(5) is not None:
                        aux3 = [rexp1.search(elem).group(3), rexp1.search(elem).group(5)]
                        cabecalho[param] = aux3

            for nome in cabecalho.keys():
                nomes.append(nome)
        else:
            aux = {}
            j = 0
            for elem in nomes:
                linha = line.split(",")
                aux[elem] = 0
                if cabecalho[elem] is None:
                    aux[elem] = linha[j]
                elif len(cabecalho[elem]) == 1:
                    num = int(cabecalho[elem][0])
                    for k in range(j, j + num):
                        aux[elem] = aux[elem] + [linha[k]]
                elif len(cabecalho[elem]) == 2:
                    lista_aux = []
                    if cabecalho[elem][1] == "sum":
                        num = int(cabecalho[elem][0])
                        for k in range(j, j + num):
                            lista_aux.append(linha[k])
                        aux[elem] = lista_aux
                        aux[elem + "_sum"] = soma(lista_aux)
                    elif cabecalho[elem][1] == "media":
                        num = int(cabecalho[elem][0])
                        for k in range(j, j + num):
                            lista_aux.append(linha[k])
                        aux[elem] = lista_aux
                        aux[elem + "_media"] = media(lista_aux)
                    else:
                        min = int(cabecalho[elem][0])
                        max = int(cabecalho[elem][1])
                        for k in range(j, j + min):
                            lista_aux.append(linha[k])
                        for k in range(j+min, j + max):
                                if linha[k].isdigit():
                                    lista_aux.append(linha[k])
                        aux[elem] = lista_aux
                elif len(cabecalho[elem]) == 3:
                    lista_aux = []
                    min = int(cabecalho[elem][0])
                    max = int(cabecalho[elem][1])
                    op = cabecalho[elem][2]
                    for k in range(j, j + min):
                        lista_aux.append(linha[k])
                    for k in range(j + min, j + max):
                        if linha[k].isdigit():
                            lista_aux.append(linha[k])
                    aux[elem] = lista_aux
                    if op == "sum":
                        aux[elem + "_sum"] = soma(lista_aux)
                    elif op == "media":
                        aux[elem + "_media"] = media(lista_aux)
                j += 1
            dicts.append(aux)
        i += 1
    print(cabecalho)
    print(dicts)


def soma(lista):
    soma = 0
    for num in lista:
        soma += int(num)
    return soma


def media(lista):
    soma = 0
    for num in lista:
        soma += int(num)
    return soma / len(lista)

def converte_json(output):
    if ".json" not in output:
        output = output + ".json"

    file = open(output, "w")
    json.dump(dicts, file, indent=3, separators=(',', ': '))
    file.close()


def main():
    parserFile("alunos1.txt")
    converte_json("output.json")


if __name__ == '__main__':
    main()
