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
    (r'<', 'LT'),
    (r'>', 'GT'),
    (r'<=', 'LE'),
    (r'>=', 'GE'),
    (r'!=', 'NE'),
    (r'&&', 'AND'),
    (r'\|\|', 'OR'),
    (r'!', 'NOT'),
    (r'\+\+', 'INCREMENT'),
    (r'--', 'DECREMENT'),
    (r';', 'SEMICOLON'),
    (r',', 'COMMA'),
    (r'"[^"]*"', 'STRING_DOUBLE'),
    (r"'[^']*'", 'STRING_SINGLE'),
    (r'//.*', 'COMMENT'),
    (r'/\*[\s\S]*?\*/', 'MULTILINE_COMMENT'),
]


def get_rules(rule_set_name):
    if rule_set_name == "Semantica_principal":
        return token_specification
    else:
        raise ValueError(f"Conjunto de regras '{rule_set_name}' não encontrado.")
