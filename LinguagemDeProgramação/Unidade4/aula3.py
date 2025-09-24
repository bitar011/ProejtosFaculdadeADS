#Testes com Python
#Assertions

#def divide(x, y):
#    assert y != 0, "Divisão por zero!"
#    return x / y

#result = divide(6, 0)
#print(result)

#def calcular_media(notas):
#    assert len(notas) > 0, "A lista de notas não pode estar vazia"
#    soma = sum(notas)
#    media = soma / len(notas)
#    return(media)

#exemplo 1
#notas_vazias = []
#media = calcular_media(notas_vazias)

#exemplo 2
#notas_validas = [2, 5, 8, 6]
#media = calcular_media(notas_validas)
#print(media)

#--------------------------------------
#Doctests
#import doctest

#def square(x):
#    """
#    Retorna o quadrado de um número.

#    Exemplos:
#    >>> square(3)
#    9
#    >>> square(-2)
#    4
#    >>> square(0)
#    0
#    """
#    return x * x

#doctest.testmod()

#--------------------------------
#Unittest
#import unittest

#def add(a, b):
#    return a + b

#class TestAddition(unittest.TestCase):
#    def test_add_positive_numbers(self):
#       self.assertEqual(add(2, 3), 5)

#    def test_add_negative_numbers(self):
#        self.assertEqual(add(-2, -3), -5)

#if __name__ == '__main__':
#    import unittest
#    unittest.main(argv=['first-arg-is-ignored'], exit=False)
#    print("Os testes foram executados com sucesso!")

#--------------------------------------------------------
#Aplicação geral da aula
#Assert
#def sum_numbers(numbers):
#    assert sum([1, 2, 3, 4]) == 10
#    assert sum([-1, 0, 1]) == 0
#    assert sum([]) == 0
#    return sum(numbers)
#teste = sum_numbers([1, 2, 3, 5])
#print(teste)

#Doctest
#def sum_numbers(numbers):
#    """
#    Soma os números em uma lista

#    Exemplos:
#    >>> sum_numbers([1, 2, 3, 4])
#    10
#    >>> sum_numbers([-1, 0, 1])
#    0
#    >>> sum_numbers([])
#    0
#    """
#    return sum(numbers)


#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()

#Unittest
import unittest
def sum_numbers(numbers):
    return sum(numbers)

class TestAddition(unittest.TestCase):
    def test_sum_numbers_positive(self):
       self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)

    def test_sum_numbers_mixed(self):
       self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_sum_numbers_empty(self):
       self.assertEqual(sum_numbers([]), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)