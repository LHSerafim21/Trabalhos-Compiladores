# Definições de regras para diferentes tipos de lexers

# Regras simples para tokenizar espaços em branco, números, palavras e caracteres desconhecidos
simple_rules = [
    (r'[ \t]+', 'WHITESPACE'),
    (r'\n', 'NEWLINE'),
    (r'\d+', 'NUMBER'),
    (r'\w+', 'WORD'),
    (r'.', 'UNKNOWN'),
]

# Regras para uma linguagem de programação fictícia
programming_language_rules = [
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

def get_rules(rule_set_name):
    if rule_set_name == "simple":
        return simple_rules
    elif rule_set_name == "programming_language":
        return programming_language_rules
    else:
        raise ValueError(f"Conjunto de regras '{rule_set_name}' não encontrado.")
