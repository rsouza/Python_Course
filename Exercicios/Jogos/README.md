# Programando Jogos Retro com a biblioteca Pyxel
A biblioteca Pyxel possui uma curva de aprendizagem extremamente suave para quem deseja começa com a programaçao de jogos. Os exercicios apresentados aqui tambem podem ser realizados na plataforma Repl.it.

Um jogo *Hello Pyxel* e muito simples:

```python
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


App()
```

## Exercicio:

Modifique o codigo acima para desenhar em ordem os numeros primos de *1* a *n*, em uma tabela de acordo com o algoritmo conhecido como crivo de Eratostenes. Primeiro desenhe uma tabela quadrada com os numeros de um a 100 e depois va apagando os nao-primos.

### Solução

```
```
[Full source](../Jogos/Crivo/eratostenes.py)
