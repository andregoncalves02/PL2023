import ply.lex as lex
import re

tokens = (
    'COMENTARIO',
    'COMENTARIO_LINHAS',
    'VARIAVEL_INICIALIZACAO',
    'OPERACAO',
    'FUNCAO',
    'PROGRAMA',
    'PARABRE',
    'PARFECHA',
    'CHAVABRE',
    'CHAVEFECHA',
    'FOR',
    'CONDICAO'
)

t_COMENTARIO = r'//(.*)\n'
t_COMENTARIO_LINHAS = r'/\*((.*)\n)*\*/'
t_VARIAVEL_INICIALIZACAO = r'int (\w+)((;|,)|= \d+(;|,)|= {(\d+,)*\d+)}(;|,))+'
t_OPERACAO = r'[\w\[\]]+ = [\w\[\]]+ ((\*|\-|\+|\/) [\w\[\]]+)*;'
t_FUNCAO = r'function \w+\(\w+\){(.*)}'
t_PROGRAMA = r'program \w+{(.*)}'
t_CHAVABRE = r'\{'
t_CHAVEFECHA = r'\}'
t_PARABRE = r'\('
t_PARFECHA = r'\)'
t_FOR = r'for \w+ in \[\d+..\d+\]{(.*)}'
t_CONDICAO = r'if (.*) (\<|\>|\==) (.*) {(.*)}'
t_ignore = "\n \t"


def t_error(t):
    print(f"Carater invalido -> {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

file = open('exemplo1.txt', 'r')
lines = file.read()
file.close()

lexer.input(lines)

while tok := lexer.token():
    print(tok)
