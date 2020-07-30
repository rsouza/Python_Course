import unittest
import numpy
class Biblioteca:
    def __init__(self, artigos):
        self.artigos = artigos
        self.autores = self.get_autores()
        self.A = self.calc_adj()
    
    def calc_adj(self):  
        A = numpy.zeros((len(self.autores), len(self.autores)))
        A = numpy.matrix(A)
        for i,a in enumerate(self.autores):
            for j,b in enumerate(self.autores):
                A[i,j] = 1 if b in self.get_vizinhos(a) else 0
        return A
                
    def get_autores(self):
        autores = []
        for a in self.artigos:
            autores.extend(list(a))
        return set(autores)
    
    def get_vizinhos(self, autor):
        
        viz=[]
        art = [t for t in self.artigos if autor in t]
        for a in art:
            v = a[0] if a[0] != autor else a[1]
            viz.append(v)
        return viz
    
    def get_num_erdos(self, autor):
        i  = list(self.autores).index(autor)
        e = list(self.autores).index('erdos')
        for j in range(1, self.A.shape[0]):
            A = self.A**j
            print(A)
            if A[i,e] != 0:
                return j
        


class TestErdos(unittest.TestCase):
    def setUp(self):
        self.B = Biblioteca([('joão', 'pedro'),('joão','erdos'), ('erdos','flávio'),('pedro','ana'),('carol','pedro'),('carol','flávio')])
        
    def test_verifica_numero_artigos_maior_que_zero(self):
        B = Biblioteca(artigos=[('joão', 'pedro'), ('erdos','flávio')])
        self.assertGreater(len(B.artigos),0)
        
        

    def test_são_vizinhos(self):
        viz = self.B.get_vizinhos('joão')
        assert('pedro' in viz)
        assert('flávio' not in viz)
        
    def test_joão_tem_numero_1(self):
        autor = 'joão'
        self.assertEqual(self.B.get_num_erdos(autor),1)
        
    def test_pedro_tem_numero_2(self):
        autor = 'pedro'
        self.assertEqual(self.B.get_num_erdos(autor),2)
        
    def test_existe_lista_autores(self):
        assert('autores' in dir(self.B))
        
    def test_ana_tem_numero_3(self):
        self.assertEqual(self.B.get_num_erdos('ana'), 3)
        
if __name__=="__main__":
    unittest.main()

