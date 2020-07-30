import re
import pygments
import os
from pygments.lexers import guess_lexer


class ProcessaTexto:
    """
    Processador de markdown para inserção de código.
    """

    def __init__(self, caminho):
        self.max_linhas = 15
        self.regex = re.compile("(```[\w\W]*\s```)\n(\[Full *source\]\([/*\w\W]+\)+)")  # Antigo: "\{([/\w+]+.*\w+.py)\}"
        self.caminho = caminho
        self.codigo = None
        self.caminho_codigo = None
        self.caminho_base = os.path.split(self.caminho)[0]
        self.markdown = ""
        self.marcações = []
        # self.nlinhas = len(self.linhas)
        self.__processa()

    def __processa(self):
        self.markdown = self.le_texto()
        refs = self.encontra_referencias(self.markdown)
        if refs:
            for pos, r in refs.items():
                cam = re.findall('source]\(([/\w\W+/]+)\)', r[1])[0]
                _, ling = self.carrega_codigo(cam)
                self.insere_codigo(posiçao=pos, codigo=self.codigo, linguagem=ling, caminho=cam)

    def le_texto(self):
        with open(self.caminho, 'r') as f:
            texto = f.read()
        return texto

    def encontra_referencias(self, texto):
        """
        Dada o texto returna marcações se existirem
        :param texto:  texto a ser analisada
        :return: lista com marcações.
        """
        marcações = re.findall(self.regex, texto)
        print(len(marcações))
        refs = {}
        pos = 0
        if marcações:
            for m in marcações:
                refs[texto[pos:].index(m[0])] = m
                pos += len(m)
        return refs

    def carrega_codigo(self, caminho):
        with open(os.path.join(self.caminho_base, caminho), 'r') as f:
            texto = f.read()
        self.codigo = texto
        linguagem = guess_lexer(texto).name
        return texto, linguagem

    def insere_codigo(self, posiçao, codigo, linguagem, caminho):
        linhas = codigo.split('\n')
        linhas = linhas[:self.max_linhas]
        codigo = '\n'.join(linhas)

        codigo = '```{}\n'.format(linguagem) + codigo + '\n```\n[Full source]({})'.format(caminho)
        self.markdown = re.sub(self.regex, codigo, self.markdown)
        print(self.markdown)
        # with open(self.caminho, 'w') as f:
        #     f.writelines(self.markdown)


if __name__ == "__main__":
    P = ProcessaTexto('../Jogos/README.md')
    # print(P.codigo)
