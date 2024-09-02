# Definições de regras para diferentes tipos de lexers
import regex as re

reserved_words = ['if', 'else', 'while', 'return', 'printf']
token_specification = [
    (r'[ \t]+', 'WHITESPACE'),
    (r'\n', 'NEWLINE'),
    (r'\d+(\.\d*)?', 'NUMBER'),
    (r'[A-Za-z_]\w*', 'IDENTIFIER'),
    (r'if', 'IF'),
    (r'else', 'ELSE'),
    (r'while', 'WHILE'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'==', 'EQUALS'),
    (r'=', 'ASSIGN'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
    (r'.', 'UNKNOWN'),
]


def get_rules(rule_set_name):
    if rule_set_name == "Semantica_principal":
        return token_specification
    else:
        raise ValueError(f"Conjunto de regras '{rule_set_name}' não encontrado.")
