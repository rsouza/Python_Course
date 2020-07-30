import unittest

#Identificando os caracteres em romanos:
dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#Só conseguiremos trabalhar até 3999

#Meu programa:
def romanos(entrada):

    soma = 0
    for i in range(len(entrada)-1):
        if dic[entrada[i]] < dic[entrada[i+1]]:
            soma -= dic[entrada[i]]
        else:
            soma += dic[entrada[i]]  
    soma = soma + dic[entrada[-1]]
    return soma

#Testes

class TestRomanos(unittest.TestCase):
    
    def test_I(self):
        resultado = romanos('I')
        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = romanos('II')
        self.assertEqual(resultado, 2)
        
    def test_V(self):
        resultado = romanos('V')
        self.assertEqual(resultado, 5)

    def test_X(self):
        resultado = romanos('X')
        self.assertEqual(resultado, 10)
        
    def test_XX(self):
        resultado = romanos('XX')
        self.assertEqual(resultado, 20)
        
    def test_L(self):
        resultado = romanos('L')
        self.assertEqual(resultado, 50)
        
    def test_C(self):
        resultado = romanos('C')
        self.assertEqual(resultado, 100)
               
    def test_D(self):
        resultado = romanos('D')
        self.assertEqual(resultado, 500)
        
    def test_M(self):
        resultado = romanos('M')
        self.assertEqual(resultado, 1000)
        
    def test_XV(self):
        resultado = romanos('XV')
        self.assertEqual(resultado, 15)
        
    def test_IV(self):
        resultado = romanos('IV')
        self.assertEqual(resultado, 4)
    def test_MDIX(self):
        resultado = romanos('MDIX')
        self.assertEqual(resultado, 1509)
    def test_MDXXXIV(self):
        resultado = romanos('MDXXXIV')
        self.assertEqual(resultado, 1534)

unittest.main()
