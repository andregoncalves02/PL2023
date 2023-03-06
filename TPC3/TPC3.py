import re
import json


def parser(file):
    dicts = []
    exp = r"(?P<dir>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nome_pai>[a-zA-Z ]+)::(?P<nome_mae>[a-zA-Z ]+)::(?P<obs>.*)::"
    rexp = re.compile(exp)
    f = open(file, 'r')
    for line in f:
        match = rexp.finditer(line)
        if match:
            for m in match:
                dicts = dicts + [m.groupdict()]

    return dicts


def freq_proc_ano(dicts):
    anos = {}
    for dict in dicts:
        if dict["ano"] not in anos:
            anos[dict["ano"]] = 1
        anos[dict["ano"]] += 1
    print("Frequencia de processos por ano: ")
    print(anos)


def nome_proprio(nome):
    nomes = re.split(r"\s+", nome)
    return nomes[0]


def apelido(nome):
    return re.search(r"\b\w+$", nome).group()


def top5_nomes(dicts, seculo):
    top5_nomes = {}
    top5_apelidos = {}
    for dict in dicts:
        if int(dict["ano"]) // 100 + 1 == seculo:
            if nome_proprio(dict["nome"]) not in top5_nomes:
                top5_nomes[nome_proprio(dict["nome"])] = 1
            top5_nomes[nome_proprio(dict["nome"])] += 1
    for dict in dicts:
        if int(dict["ano"]) // 100 + 1:
            if apelido(dict["nome"]) not in top5_apelidos:
                top5_apelidos[apelido(dict["nome"])] = 1
            top5_apelidos[apelido(dict["nome"])] += 1
    top5_nomes_ordenados = sorted(top5_nomes.items(), key=lambda x: x[1], reverse=True)[:5]
    top5_apelidos_ordenados = sorted(top5_apelidos.items(), key=lambda x: x[1], reverse=True)[:5]
    print(top5_nomes_ordenados)
    print(top5_apelidos_ordenados)


def top5_seculo(dicts):
    for i in range(17, 21):
        print("top nomes do secúlo " + str(i))
        top5_nomes(dicts, i)


def encontra_fam(linha):
    if len(linha) > 0:
        lista = re.findall(r"(?:,(([A-Z][a-z]+ )*([A-Z][a-z]+))\. Proc.\d+)", linha)
        for elem in lista:
            if elem:
                return elem[0]


def freq_parentesco(dicts):
    aux = {}
    for dict in dicts:
        parentesco = encontra_fam(dict["obs"])
        if parentesco != None:
            if parentesco not in aux:
                aux[parentesco] = 1
            aux[parentesco] += 1
    print("Frequencia de processos por grau de parentesco:")
    print(aux)


def converte_json(dicts, output):
    primeiros_20 = {}
    if ".json" not in output:
        output = output + ".json"

    file = open(output, "w")
    i = 0
    for dict in dicts:
        if i<20:
            primeiros_20[str(i)] = dict
        i += 1
    json.dump(primeiros_20, file, indent=3, separators=(',', ': '))
    file.close()


def main():
    dicts = parser("processos.txt")
    option = 0
    while option != -1:
        option = int(input("""
1 - Frequência de processos por ano
2 - TOP 5 nomes por seculo
3 - Frequência dos tipos de relação
4 - Converter em Formato Json
Escolha uma opção ou escreva exit para sair:"""))
        if option == 1:
            freq_proc_ano(dicts)
        elif option == 2:
            top5_seculo(dicts)
        elif option == 3:
            freq_parentesco(dicts)
        elif option == 4:
            converte_json(dicts, "output.json")
        elif str(option) == "exit":
            option = -1


if __name__ == "__main__":
    main()
