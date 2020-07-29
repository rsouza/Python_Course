import pyxel
from crivo import crivo
from random import choice

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Crivo de Eratostenes")
        n = 100
        self.primos = list(crivo(n))
        self.pintados = []
        # pyxel.image(0).load(0, 0, "Logo_FGV_EMAp.png")
        self.positions = [(x, y) for y in range(12, 112, 10) for x in range(22, 122, 10)]
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw_full_table(self):
        self.coords = {}
        for n in range(100):
            x, y = self.positions[n]
            self.coords[n] = (x, y)
            # cor = 8 if n in self.primos else 6
            if n in self.pintados:
                pyxel.text(x, y, str(n), pyxel.frame_count % 16)
            else:
                pyxel.text(x, y, str(n), 6)

    def pinta_primo(self, p):
        self.pintados.append(p)
        x, y = self.coords[p]
        pyxel.text(x, y, str(p), pyxel.frame_count % 16)
        self.primos.pop(self.primos.index(p))


    def draw(self):
        pyxel.cls(0)
        # pyxel.text(2,2,str(pyxel.frame_count),6)
        pyxel.text(20, 3, "Numeros primos", 10)
        pyxel.rectb(20,10,102, 102, 9)
        self.draw_full_table()
        if pyxel.frame_count % 10 == 0 and len(self.primos) > 0:
            self.pinta_primo(choice(self.primos))

    # pyxel.text(22, 22, "2", pyxel.frame_count % 16)

App()
