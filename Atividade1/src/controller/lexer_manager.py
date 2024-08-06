from common.lexer import Lexer

class LexerManager:
    def __init__(self):
        self.lexers = {}

    def add_lexer(self, name, rules):
        self.lexers[name] = Lexer(rules)

    def get_lexer(self, name):
        return self.lexers.get(name, None)

    def tokenize(self, lexer_name, text):
        lexer = self.get_lexer(lexer_name)
        if lexer is None:
            raise ValueError(f"Nenhum lexer encontrado com o nome {lexer_name}")
        return lexer.tokenize(text)
