import sys
import os
import tkinter as tk
from view.gui import App
from controller.lexer_manager import LexerManager  # Importar o LexerManager
from controller.parser import Parser  # Importar o Parser
from utils.rules import get_rules  # Importar as regras de tokenização

# Adiciona o diretório raiz ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    # Criação da interface gráfica
    root = tk.Tk()
    app = App(root)
    app.tokenize_button.config(command=app.parse_input)
    root.mainloop()

    # Exemplo de uso do Lexer e Parser (opcional para testes de linha de comando)
    lexer_manager = LexerManager()
    lexer_manager.add_lexer("LALG", get_rules("LALG"))  # Definir regras de LALG
    
    # Exemplo de entrada (pode ser substituído pelo texto inserido na GUI)
    input_text = "var x, y: integer"
    
    # Tokenização
    tokens = lexer_manager.tokenize("LALG", input_text)
    print("Tokens gerados:", tokens)
    
    # Análise sintática
    parser = Parser(lexer_manager.get_lexer("LALG"))
    try:
        parser.parse(tokens)
        print("Análise sintática concluída com sucesso!")
    except SyntaxError as e:
        print(f"Erro de sintaxe: {e}")
