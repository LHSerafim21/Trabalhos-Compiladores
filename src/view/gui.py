import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from utils.rules import get_rules
from controller.lexer_manager import LexerManager
from controller.parser import Parser  # Importa o Parser
import threading  # Importa a biblioteca de threading

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de analisadores léxicos")
        self.manager = LexerManager()

        self.root.configure(bg="#2E2E2E")  # Cor de fundo escura

        # Estilo para tema escuro
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#2E2E2E")
        style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF")
        style.configure("TButton", background="#3C3F41", foreground="#FFFFFF")
        style.configure("Treeview", background="#3C3F41", foreground="#FFFFFF", fieldbackground="#3C3F41")
        style.map("TButton", background=[("active", "#555555")])

        # Frame superior - Editor de texto
        self.top_frame = ttk.Frame(root)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.line_numbers = tk.Text(self.top_frame, width=4, padx=3, takefocus=0, border=0, background='#3C3F41', foreground="#FFFFFF", state='disabled')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.input_text = tk.Text(self.top_frame, wrap=tk.WORD, undo=True, background='#3C3F41', foreground="#FFFFFF", insertbackground="#FFFFFF")
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.input_text.bind("<KeyRelease>", self.update_line_numbers)
        
        self.scrollbar = ttk.Scrollbar(self.top_frame, command=self.sync_scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.input_text.config(yscrollcommand=self.scrollbar.set)
        self.line_numbers.config(yscrollcommand=self.scrollbar.set)

        # Frame inferior - Tabela de tokens
        self.bottom_frame = ttk.Frame(root)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.bottom_frame, columns=("Lexema", "Token", "Erro", "Linha", "Coluna inicial", "Coluna final"), show="headings", height=8)
        self.tree.heading("Lexema", text="Lexema")
        self.tree.heading("Token", text="Token")
        self.tree.heading("Erro", text="Erro")
        self.tree.heading("Linha", text="Linha")
        self.tree.heading("Coluna inicial", text="Coluna Inicial")
        self.tree.heading("Coluna final", text="Coluna Final")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para os botões
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        self.inner_button_frame = ttk.Frame(self.button_frame)
        self.inner_button_frame.pack(side=tk.TOP, expand=True)

        self.open_button = ttk.Button(self.inner_button_frame, text="Abrir", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5)

        self.save_button = ttk.Button(self.inner_button_frame, text="Salvar", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.tokenize_button = ttk.Button(self.inner_button_frame, text="Tokenizar", command=self.tokenize_input_threaded)
        self.tokenize_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.inner_button_frame, text="Limpar", command=self.clear_text, bg='#d9534f', fg='white', activebackground='#c9302c', activeforeground='white')
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def update_line_numbers(self, event=None):
        """Atualiza os números das linhas no editor de texto."""
        line_count = self.input_text.index('end').split('.')[0]
        self.line_numbers.config(state='normal')
        self.line_numbers.delete(1.0, tk.END)
        for i in range(1, int(line_count)):
            self.line_numbers.insert(tk.END, f"{i}\n")
        self.line_numbers.config(state='disabled')

    def sync_scroll(self, *args):
        """Sincroniza a rolagem entre o editor de texto e os números das linhas."""
        self.input_text.yview(*args)
        self.line_numbers.yview(*args)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.input_text.get(1.0, tk.END)
                file.write(content)

    def tokenize_input(self):
        """Tokeniza o texto de entrada e exibe os tokens na tabela."""
        lexer_name = "current_lexer"
        input_text = self.input_text.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Aviso", "O texto de entrada não pode ficar vazio.")
            return

        try:
            rules = get_rules("LALG")  # Usando o conjunto de regras "LALG"
            self.manager.add_lexer(lexer_name, rules)
            tokens = self.manager.tokenize(lexer_name, input_text)

            # Limpa a tabela de tokens antes de inserir novos
            for item in self.tree.get_children():
                self.tree.delete(item)

            current_line = 1
            current_column = 1
            for token_type, lexeme in tokens:
                line = current_line
                col_start = current_column
                col_end = col_start + len(lexeme) - 1

                # Atualizar a posição atual
                current_column = col_end + 1
                if '\n' in lexeme:
                    lines = lexeme.split('\n')
                    current_line += len(lines) - 1
                    current_column = len(lines[-1]) + 1  # Resetar para a próxima linha

                error = "" if token_type != "UNKNOWN" else "Erro"
                self.tree.insert("", "end", values=(lexeme, token_type, error, line, col_start, col_end))
            
            # Análise sintática após tokenização
            parser = Parser(self.manager.get_lexer(lexer_name))
            parser.parse(tokens)  # Análise dos tokens gerados

            messagebox.showinfo("Sucesso", "Análise sintática concluída com sucesso!")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except SyntaxError as e:
            messagebox.showerror("Error", str(e))

    def tokenize_input_threaded(self):
        """Inicia a tokenização em um thread separado para evitar bloquear a GUI."""
        threading.Thread(target=self.tokenize_input).start()

    def clear_text(self):
        """Limpa o editor de texto e a tabela."""
        self.input_text.delete("1.0", tk.END)
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.update_line_numbers()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
