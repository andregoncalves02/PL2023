import sys


def main():
    for line in sys.stdin:
        if line== "exit":
            break
        calcula(line)

def calcula(string):
    res = 0
    on = True
    i = 0
    for x in string:
        if (x=='o' or x=='O') and (string[i+1]=='n' or string[i+1] == 'N'):
             on = True
        if x.isnumeric() and on:
            res = res +int(x)
        if (x=='o' or x=='O') and (string[i+1]=='f' or string[i+1] == 'F') and (string[i+2]=='f' or string[i+2] == 'F'):
            on = False
        if x=='=':
            print(res)
            res = 0
        i+=1
    print(res)

if __name__ == '__main__':
    main()
