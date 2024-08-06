import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from utils.rules import get_rules
from controller.lexer_manager import LexerManager

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador Lexico (FLEX)")

        self.manager = LexerManager()

        # Configurações da janela
        self.root.geometry("800x800")
        
        # Seletor de conjuntos de regras
        self.rule_set_label = ttk.Label(root, text="Selecione o conjunto de regras:")
        self.rule_set_label.pack(pady=5)
        
        self.rule_set_var = tk.StringVar()
        self.rule_set_combobox = ttk.Combobox(root, textvariable=self.rule_set_var)
        self.rule_set_combobox['values'] = ("simple", "programming_language")
        self.rule_set_combobox.current(0)
        self.rule_set_combobox.pack(pady=5)
        
        # Botão para criar lexer
        self.create_button = ttk.Button(root, text="Criar Lexema", command=self.create_lexer)
        self.create_button.pack(pady=5)

        # Área de entrada de texto
        self.input_label = ttk.Label(root, text="Inserir Texto:")
        self.input_label.pack(pady=5)
        
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
        self.input_text.pack(pady=5)
        
        # Botão para tokenizar o texto
        self.tokenize_button = ttk.Button(root, text="Tokenizar", command=self.tokenize_input)
        self.tokenize_button.pack(pady=5)
        
        # Área para exibir os tokens
        self.output_label = ttk.Label(root, text="Tokens:")
        self.output_label.pack(pady=5)
        
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
        self.output_text.pack(pady=5)

    def create_lexer(self):
        rule_set_name = self.rule_set_var.get()
        lexer_name = "current_lexer"
        try:
            rules = get_rules(rule_set_name)
            self.manager.add_lexer(lexer_name, rules)
            messagebox.showinfo("Sucesso", f"Lexema criado com o conjunto de regras'{rule_set_name}'.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def tokenize_input(self):
        lexer_name = "current_lexer"
        input_text = self.input_text.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Aviso", "O texto de entrada não pode estar vazio.")
            return

        try:
            tokens = self.manager.tokenize(lexer_name, input_text)
            self.output_text.delete("1.0", tk.END)
            for token in tokens:
                self.output_text.insert(tk.END, f"{token}\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except SyntaxError as e:
            messagebox.showerror("Error", str(e))
