from unittest import TestCase, main
from errors import CloseCharError, EmptyError, NoneError, NotNumbersError, OpenCharError, SeparatorError
from rang import Range
class TestRange(TestCase):
    def test_parameter_none(self,):
        parameter = None
        try:
            a = Range(parameter)
        except NoneError:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Parametro Nulo")

    def test_parameter_empty(self,):
        parameter = ""
        try:
            a = Range(parameter)
        except EmptyError:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Parametro vacio")

    def test_parameter_open_char(self,):
        parameter = "^ 5,5)"
        try:
            a = Range(parameter)
        except OpenCharError:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Carater Inicial incorrecto")

    def test_parameter_close_char(self,):
        parameter = "(5,5 ["
        try:
            a = Range(parameter)
        except CloseCharError:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Caracter final incorrecto")

    def test_parameter_separator(self,):
        parameter = "(55)"
        try:
            a = Range(parameter)
        except SeparatorError:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Falta separador")

    def test_parameter_not_numbers(self,):
        parameter = "(5,A5)"
        try:
            a = Range(parameter)
        except NotNumbersError:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Numero incorrecto")

    def test_parameter_not_numbers(self,):
        parameter = "(5,5)"
        a = Range(parameter)
        self.assertTrue(True)

if __name__ == "__main__":
    main()