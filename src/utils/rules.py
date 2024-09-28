import re

# Definições de regras para tokens da linguagem C e LALG (modificadas)
token_specification = [
    (r'[ \t]+', 'WHITESPACE'),                # Espaços em branco
    (r'\n', 'NEWLINE'),                       # Quebras de linha
    (r'int|float|char', 'TYPE'),              # Tipos de dados (C)
    (r'printf|scanf', 'FUNCTION'),            # Funções reservadas
    (r'var', 'VAR'),                          # Palavra reservada 'var'
    (r':', 'COLON'),                          # Delimitador ':'
    (r';', 'SEMICOLON'),                      # Delimitador ';'
    (r',', 'COMMA'),                          # Delimitador ','
    (r'\(', 'LPAREN'),                        # Parêntese esquerdo '('
    (r'\)', 'RPAREN'),                        # Parêntese direito ')'
    (r'\{', 'LBRACE'),                        # Chave esquerda '{'
    (r'\}', 'RBRACE'),                        # Chave direita '}'
    (r'\[', 'LBRACKET'),                      # Colchete esquerdo '['
    (r'\]', 'RBRACKET'),                      # Colchete direito ']'
    (r'\+', 'PLUS'),                          # Operador '+'
    (r'-', 'MINUS'),                          # Operador '-'
    (r'\*', 'MULTIPLY'),                      # Operador '*'
    (r'/', 'DIVIDE'),                         # Operador '/'
    (r'=', 'ASSIGN'),                         # Operador '='
    (r'//.*', 'COMMENT'),                     # Comentário de linha
    (r'/\*[\s\S]*?\*/', 'MULTILINE_COMMENT'), # Comentário multilinha
    (r'"([^"\\]|\\.)*"', 'STRING'),          # Strings entre aspas duplas
    (r"'([^'\\]|\\.)*'", 'CHAR'),            # Caracteres entre aspas simples
    (r'[A-Za-z_][A-Za-z0-9_]*', 'IDENTIFIER'),# Identificadores
    (r'\d+(\.\d*)?', 'NUMBER'),               # Números (inteiros e reais)
    (r'.', 'ILLEGAL'),                        # Qualquer caractere ilegal
]

# Função para obter as regras
def get_rules(rule_set_name):
    if rule_set_name == "LALG":
        return token_specification
    else:
        raise ValueError(f"Conjunto de regras '{rule_set_name}' não encontrado.")
