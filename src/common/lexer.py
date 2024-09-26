from utils.rules import reserved_words

import re

import sys
import os

class Lexer:
    def __init__(self, rules):
        self.rules = [(re.compile(pattern), token_type) for pattern, token_type in rules]

    def tokenize(self, text):
        pos = 0
        tokens = []
        while pos < len(text):
            match = None
            for pattern, token_type in self.rules:
                match = pattern.match(text, pos)
                if match:
                    token = (token_type, match.group(0))
                    tokens.append(token)
                    pos = match.end()
                    break
            if not match:
                raise SyntaxError(f"Caráter ilegal no índice {pos}")
        return tokens
    
    def get_token_type(self, lexeme):
        if lexeme in reserved_words:
            return lexeme.upper()
        elif lexeme.isdigit():
            return "NUMBER"
        elif lexeme.startswith('"') or lexeme.startswith("'"):
            return "STRING"
        else:
            return "IDENTIFIER"
