from tokens import Token, TokenType

WHITESPACE = ' \n\ty='
DIGITS = '0123456789'
VAR = 'x'


class Lexer:
    def __init__(self, text, value_x):
        #if list_x is None:
            #list_x = []
        #self.list_x = list_x
        self.value_x = value_x
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in VAR:
                yield self.generate_var()
            elif self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and self.current_char in DIGITS:
            number_str += self.current_char
            self.advance()

        return Token(TokenType.NUMBER, float(number_str))

    # x
    def generate_var(self):
        self.advance()
        return Token(TokenType.NUMBER, float(self.value_x))

    '''def Valuex(self):
        self.list_x.append(float(self.value_x))
        return self.list_x'''
