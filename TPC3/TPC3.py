import re


def parser(file):
    dicts = []
    exp = r"(?P<dir>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nome_pai>[a-zA-Z ]+)::(?P<nome_mae>[a-zA-Z ]+)::(?P<obs>.*)::"
    rexp = re.compile(exp)
    f = open(file, 'r')
    for line in f:
        match = rexp.finditer(line)
        for m in match:
            if match :
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
def nomes(nome):
    return re.match(r"/w+", nome), re.search(r"/w+$", nome)



def main():
    dicts = parser("processos.txt")
    freq_proc_ano(dicts)


if __name__ == "__main__":
    main()
