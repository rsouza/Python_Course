"""
O codigo recursivo abaixo, nao roda em Python
devido ao limite de recursao existente no interpretador.
Desafio: Implementar a curva de Peano de maneira iterativa.
descriçao do algoritmos manual:
https://www.wikihow.com/Draw-a-Hilbert-Curve
"""

from PIL import Image


def line(p1, p2):
    """
    desenha uma linha 'y = ax + b' do ponto p1 ao ponto p2
    :param p1: (x1,y1) coordenadas do ponto p1
    :param p2: (x2,y2) coordenadas do ponto p2
    """
    x1, y1 = p1
    x2, y2 = p2
    a = (y2 - y1) / (x2 - x1)
    b = y2 - a * x2
    for x in range(x1, x2 + 1):
        image.putpixel((x, int(a * x + b)), (255, 255, 255))


def Peano(x, y, lg, i1, i2):
    if lg == 1:
        line((x, y), (3 * x, 3 * y))
        return
    Peano(x + (2 * i1 * lg), y + (2 * i1 * lg), lg, i1, i2);
    Peano(x + ((i1 - i2 + 1) * lg), y + ((i1 + i2) * lg), lg, i1, 1 - i2);
    Peano(x + lg, y + lg, lg, i1, 1 - i2);
    Peano(x + ((i1 + i2) * lg), y + ((i1 - i2 + 1) * lg), lg, 1 - i1, 1 - i2);
    Peano(x + (2 * i2 * lg), y + (2 * (1 - i2) * lg), lg, i1, i2);
    Peano(x + ((1 + i2 - i1) * lg), y + ((2 - i1 - i2) * lg), lg, i1, i2);
    Peano(x + (2 * (1 - i1) * lg), y + (2 * (1 - i1) * lg), lg, i1, i2);
    Peano(x + ((2 - i1 - i2) * lg), y + ((1 + i2 - i1) * lg), lg, 1 - i1, i2);
    Peano(x + (2 * (1 - i2) * lg), y + (2 * i2 * lg), lg, 1 - i1, i2);


if __name__ == "__main__":
    dimx = 100
    dimy = 100
    image = Image.new("RGB", (dimx, dimy))
    Peano(0, 0, 100, 0, 0)

    # line((0, 0), (99, 99))
    image.show()
