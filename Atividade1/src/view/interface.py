from controller.lexer_manager import LexerManager

class Interface:
    def __init__(self):
        self.manager = LexerManager()

    def create_lexer(self, name, rules):
        self.manager.add_lexer(name, rules)
        print(f"Lexema '{name}' criado.")

    def tokenize_input(self, lexer_name, text):
        try:
            tokens = self.manager.tokenize(lexer_name, text)
            print(f"Tokens: {tokens}")
        except ValueError as e:
            print(e)
        except SyntaxError as e:
            print(e)
