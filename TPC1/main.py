from cache import Cache

def main():
    tabela = Cache()
    path="myheart.csv"
    file = open(path,"r")
    lines = file.read().split('\n')
    for line in lines:
        tabela.add(line)
    choice = -1
    while(choice != "0"):
        print("------------------MENU----------------")
        print("1-Distribuição da doença por genero")
        print("2-Distribuição da doença por escalão")
        print("3-Distribuição da doença por colestrol")
        print("0-Sair")
        choice = input("Escolha uma opção: ")
        if(choice == "1"):
            tabela.exc1()
        elif(choice == "2"):
            tabela.exc2()
        elif(choice == "3"):
            tabela.exc3()
        else:
            print("Escolha uma opção válida")


if __name__ == '__main__':
    main()