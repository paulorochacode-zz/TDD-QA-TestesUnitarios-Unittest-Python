from unittest import TestCase, main

from src.programaIdade import defineIdade

#teste com Framework nativo unittest

#teste Case a seguir:
class Testes(TestCase):
    #teste 1
    def test_defineIdade(self):
        self.assertEqual(defineIdade(12), 'Voce e menor de idade')
    #teste 2
    def test_defineIdade2(self):
        self.assertEqual(defineIdade(19), 'Voce e maior de idade')

if __name__ == '__main__':
    main()    
