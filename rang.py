from errors import CloseCharError, EmptyError, NoneError, NotNumbersError, OpenCharError, SeparatorError

class Range:
    separator = ","

    def validate_initial_begin_chars(self, text):
        if text[0] != "(" and text[0] != "[":
            raise OpenCharError("")

        if text[-1] != "]" and text[-1] != ")":
            raise CloseCharError("")

        self.initial_char = text[0]
        self.final_char = text[-1]

        return text[1: -1]

    def __init__(self, p):
        if p is None:
            raise NoneError("")
        
        p_trim = p.rstrip()
        if len(p_trim) == 0:
            raise EmptyError("")

        p_clean = self.validate_initial_begin_chars(p_trim)

        values = p_clean.split(self.separator)
        if len(values) == 1:
            raise SeparatorError("")

        try:
            self.a = int(values[0])
            self.b = int(values[1])
        except:
            raise NotNumbersError()
    
    def __str__(self,):
        return f'{self.initial_char} {self.a}, {self.b} {self.final_char}'