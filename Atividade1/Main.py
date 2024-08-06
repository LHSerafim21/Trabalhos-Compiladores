import tokenize
import re


if __name__ == "__main__":
    code = "3 + 5 * ( 10 - 20 )"
    tokens = tokenize(code)
    for token in tokens:
        print(token)


def tokenize(text):
    pos = 0
    tokens_found = []
    while pos < len(text):
        match = None
        for token_type, pattern in tokens:
            regex = re.compile(pattern)
            match = regex.match(text, pos)
            if match:
                if token_type != 'WHITESPACE':
                    token = (token_type, match.group(0))
                    tokens_found.append(token)
                pos = match.end(0)
                break
        if not match:
            raise RuntimeError(f'Unexpected character: {text[pos]}')
    return tokens_found
