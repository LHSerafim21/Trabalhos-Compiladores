# Definições de regras para diferentes tipos de lexers

Semantica_Serafim = [
    (r'[ \t]+', 'WHITESPACE'),
    (r'\n', 'NEWLINE'),
    (r'\d+', 'NUMBER'),
    (r'\w+', 'IDENTIFIER'),
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

Semantica_Ikeda = [
    
]

Semantica_Menezes = [
    
]

def get_rules(rule_set_name):
    if rule_set_name == "Semantica_Serafim":
        return Semantica_Serafim
    elif rule_set_name == "Semantica_Ikeda":
        return Semantica_Ikeda
    elif rule_set_name == "Semantica_Menezes":
        return Semantica_Menezes
    else:
        raise ValueError(f"Conjunto de regras '{rule_set_name}' não encontrado.")
