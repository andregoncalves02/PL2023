import re


def parser(file):
    dicts = []
    exp = r"(?P<dir>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nome_pai>[a-zA-Z ]+)::(?P<nome_mae>[a-zA-Z ]+)::(?P<obs>.*)::"
    rexp = re.compile(exp)
    f = open(file, 'r')
    for line in f:
        match = rexp.finditer(line)
        for m in match:
            if match:
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
    nomes = re.split(r"\s+", nome)
    return nomes[len(nomes)-1]


def top5_nomes(dicts, seculo):
    top5_nomes = {}
    top5_apelidos = {}
    for dict in dicts:
        if int(dict["ano"]) // 100 + 1 == seculo:
            if nome_proprio(dict["nome"]) not in top5_nomes:
                top5_nomes[nome_proprio(dict["nome"])] = 1
            top5_nomes[nome_proprio(dict["nome"])] += 1
            if apelido(dict["nome"]) not in top5_apelidos:
                top5_apelidos[apelido("nome")] = 1
            top5_apelidos[apelido("nome")] += 1
    top5_nomes_ordenados = sorted(top5_nomes.items(), key=lambda x: x[1], reverse=True)[:5]
    top5_apelidos_ordenados = sorted(top5_apelidos.items(), key=lambda x: x[1], reverse=True)[:5]
    print(top5_nomes_ordenados)
    print(top5_apelidos_ordenados)


def main():
    dicts = parser("processos.txt")
    freq_proc_ano(dicts)
    top5_nomes(dicts, 20)


if __name__ == "__main__":
    main()
