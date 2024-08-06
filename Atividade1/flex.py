import ply.lex as lex
import re

# Lista de nomes de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regras para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Regra para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco
t_ignore  = ' \t'

# Regra para rastrear números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Testar o lexer
data = "3 + 5 * ( 10 - 20 )"
lexer.input(data)
for tok in lexer:
    print(tok)
