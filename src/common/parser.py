import pyparsing as pp

# Define the grammar rules
variable_declaration = pp.Keyword("var") + pp.identifier + pp.equal + pp.expression
assignment = pp.identifier + pp.equal + pp.expression
expression = pp.forward()
expression << pp.infixNotation(pp.identifier | pp.number, [
    (pp.oneOf("+ - * /"), 1, pp.opAssoc.LEFT),
    (pp.oneOf("== != < > <= >="), 1, pp.opAssoc.LEFT),
])

# Define the parser
parser = pp.ZeroOrMore(variable_declaration | assignment | expression)

def parse_input(text):
    try:
        return parser.parseString(text, parseAll=True)
    except pp.ParseException as e:
        raise SyntaxError(f"Erro de sintaxe: {e}")