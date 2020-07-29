# Desenvolvimento de utilitarios interativos para terminal
Nestes exercicios, o objetivo e o desenvolvimento de apliocaçoes que resolvam tarefas simples apartir de uma interface simples no terminal do SO.

1. Desenvolver um preprocessador de Markdown que procura por links para arquivos fonte, em um documento markdown e substitui os mesmos por uma versao do codigo embutida no markdown. 
**Requisitos:** 

    - Definir uma sintaxe para inclusao do link. por exemplo: {/codigo/source.py}
    - Reconhecer a linguagem do codigo fonte.
    - se o codigo tiver mais que *x* linhas, trunca-lo e adicionar um link para o arquivo original do tipo :"Ver o arquivo..."
    - Utilizar Bibliotecas como a [click](https://click.palletsprojects.com/en/7.x/) e a [Pygments](http://pygments.org/)
