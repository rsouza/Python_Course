import unittest

class Test(unittest.TestCase):

#Testes 1 Ampulheta:
    def test_1_ampulheta_3(self):
        resultado = calcula_tempo([3])
        self.assertEqual(resultado, 3)

    def test_1_ampulheta_5_nao_da(self):
        resultado = calcula_tempo([5])
        self.assertEqual(resultado, 'Não dá')
    
    def test_1_ampulheta_1(self):
        resultado = calcula_tempo([1])
        self.assertEqual(resultado, 3)

#Testes 2 Ampulhetas:        
    def test_2_ampulhetas_5_3(self):
        resultado = calcula_tempo([5, 3])
        self.assertEqual(resultado, 3)
        
    def test_2_ampulhetas_4_2(self):
        resultado = calcula_tempo([4, 2])
        self.assertEqual(resultado, 'Não dá')
        
    def test_2_ampulhetas_4_7(self):
        resultado = calcula_tempo([4, 7])
        self.assertEqual(resultado, 7)
    
    def test_2_ampulhetas_5_7(self):
        resultado = calcula_tempo([5, 7])
        self.assertEqual(resultado, 10)
        
    def test_2_ampulhetas_6_7(self):
        resultado = calcula_tempo([6, 7])
        self.assertEqual(resultado, 21)

    def test_2_ampulhetas_6_15(self):
        resultado = calcula_tempo([6, 15])
        self.assertEqual(resultado, 15)
        
    def test_2_ampulhetas_4_13(self):
        resultado = calcula_tempo([4, 13])
        self.assertEqual(resultado, 16)

    def test_2_ampulhetas_5_9(self):
        resultado = calcula_tempo([5, 9])
        self.assertEqual(resultado, 18)
    
    def test_2_ampulhetas_3_3(self):
        resultado = calcula_tempo([3,3])
        self.assertEqual(resultado, 3)
        
def calcula_tempo(ampulhetas):
    menor = min(ampulhetas)
    maior = max(ampulhetas)
    
    if 3 in ampulhetas or 1 in ampulhetas:
        return 3

    if len(ampulhetas) == 2:
        kmax = 3*(maior - menor)

        for k in range(0, kmax+1):
            for i in range(0, kmax+1):
                if abs(k*menor - i*maior) == 3:
                    return max(k*menor, i*maior)

    return 'Não dá'
            

unittest.main()
