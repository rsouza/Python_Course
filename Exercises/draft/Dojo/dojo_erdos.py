import unittest
from collections import defaultdict


class Test(unittest.TestCase):
    def test_Erdos_é_zero(self):
        artigos = [('Erdos',)]
        biblioteca = Biblioteca(artigos)
        self.assertEqual(
            biblioteca.numero_de_erdos('Erdos'), 0)

    def test_Flávio_é_1(self):
        artigos = [('Erdos', 'Flávio')]
        b = Biblioteca(artigos)
        self.assertEqual(
            b.numero_de_erdos('Flávio'), 1)

    def test_José_é_2(self):
        artigos = [('Erdos', 'Flávio'), ('Flávio', 'José')]
        b = Biblioteca(artigos)
        self.assertEqual(
            b.numero_de_erdos('José'), 2)

    def test_José_tem_2_artigos_e_é_1(self):
        artigos = [('Erdos', 'Flávio'), ('Flávio', 'José'), ('Erdos', 'José')]
        b = Biblioteca(artigos)
        self.assertEqual(
            b.numero_de_erdos('José'), 1)

    def test_Ana_é_3(self):
        artigos = [('Erdos', 'Flávio'), ('Flávio', 'José'), ('Ana', 'José')]
        b = Biblioteca(artigos)
        self.assertEqual(
            b.numero_de_erdos('Ana'), 3)


class Biblioteca:

    def __init__(self, artigos):
        self.artigos = artigos
        self.autores = {}
        self.viz = {}
        for artigo in self.artigos:
            for autor in artigo:
                self.autores[autor] = 999
                self.viz[autor] = set([i for art in self.artigos for i in art if i != autor and autor in art])

        self.autores['Erdos'] = 0

        for autor in self.autores:
            if autor != 'Erdos':
                self.autores[autor] = min([self.autores[n] for n in self.viz[autor]]) + 1

    def numero_de_erdos(self, nome):
        return self.autores[nome]


unittest.main()
