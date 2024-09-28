class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = []
        self.pos = 0
    
    def parse(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self._funcoes()  # Começa pela declaração de funções ou variáveis
    
    def _match(self, expected_token_type):
        """Compara o token atual com o tipo esperado e avança"""
        self._skip_whitespace()  # Pula tokens de espaço em branco e nova linha
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Erro de sintaxe: esperado {expected_token_type}, encontrado {self.tokens[self.pos]}")
    
    def _skip_whitespace(self):
        """Ignora tokens de espaços em branco e novas linhas"""
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('WHITESPACE', 'NEWLINE'):
            self.pos += 1
    
    def _funcoes(self):
        """Reconhece funções do tipo: int main() { ... }"""
        self._match('TYPE')        # Exemplo: 'int'
        self._match('IDENTIFIER')  # Exemplo: 'main'
        self._match('LPAREN')      # Abre parênteses '('
        self._match('RPAREN')      # Fecha parênteses ')'
        self._bloco()
    
    def _bloco(self):
        """Reconhece o bloco de código: { ... }"""
        self._match('LBRACE')  # Abre o bloco '{'
        while self.tokens[self.pos][0] != 'RBRACE':
            self._stmt()
        self._match('RBRACE')  # Fecha o bloco '}'

    def _stmt(self):
        """Reconhece declarações ou expressões dentro de um bloco"""
        self._skip_whitespace()  # Ignorar espaços ou novas linhas antes de analisar
        if self.tokens[self.pos][0] == 'TYPE':  # Declaração de variável
            self._decl_var()
        elif self.tokens[self.pos][0] == 'IDENTIFIER':  # Expressões
            self._expressao()
        elif self.tokens[self.pos][0] == 'FUNCTION':  # Chamada de função
            self._chamada_funcao()
        elif self.tokens[self.pos][0] == 'STRING':  # Ignorar strings (se necessário)
            self.pos += 1
        elif self.tokens[self.pos][0] == 'CHAR':  # Ignorar caracteres
            self.pos += 1
        else:
            raise SyntaxError(f"Declaração ou expressão esperada, encontrado {self.tokens[self.pos]}")
    
    def _decl_var(self):
        """Reconhece declarações de variáveis do tipo: int x, y;"""
        self._match('TYPE')
        self._lista_identificadores()
        self._match('SEMICOLON')

    def _lista_identificadores(self):
        """Reconhece uma lista de identificadores separados por vírgula"""
        self._match('IDENTIFIER')
        while self.tokens[self.pos][0] == 'COMMA':
            self._match('COMMA')
            self._match('IDENTIFIER')
    
    def _expressao(self):
        """Reconhece expressões do tipo: x = (y + z);"""
        self._match('IDENTIFIER')
        self._match('ASSIGN')
        self._exp()
        self._match('SEMICOLON')
    
    def _exp(self):
        """Expressão aritmética simples"""
        self._skip_whitespace()  # Ignorar espaços ou novas linhas dentro da expressão
        if self.tokens[self.pos][0] in ('NUMBER', 'IDENTIFIER', 'STRING'):
            self.pos += 1
        else:
            raise SyntaxError(f"Expressão esperada, encontrado {self.tokens[self.pos]}")
        
        # Operadores aritméticos
        while self.tokens[self.pos][0] in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'):
            self.pos += 1
            self._exp()
    
    def _chamada_funcao(self):
        """Reconhece chamadas de funções do tipo: printf(...);"""
        self._match('FUNCTION')  # Exemplo: 'printf'
        self._match('LPAREN')     # Abre parênteses '('
        
        # Processa os argumentos da função, se necessário.
        while self.tokens[self.pos][0] != 'RPAREN':
            if self.tokens[self.pos][0] in ('IDENTIFIER', 'NUMBER', 'STRING'):  # Aceita ID, NUM e STRING
                self.pos += 1  # Avança para o próximo argumento
            if self.tokens[self.pos][0] == 'COMMA':
                self._match('COMMA')  # Avança se houver mais argumentos
        self._match('RPAREN')     # Fecha parênteses ')'
        self._match('SEMICOLON')  # Termina com ';'
