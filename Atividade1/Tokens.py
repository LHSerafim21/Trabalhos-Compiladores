import re

tokens = [
    ('NUMBER', r'\d+'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('WHITESPACE', r'\s+'),
    ('MISMATCH', r'.')
]