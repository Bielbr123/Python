"""Created on Sat Jul 15 20:17:38 2022.

@author: gabriel

Modified: 16/07/2022
Ps.: a melhor forma de tratar error é criar uma classe que utilize as Excep-
tios padrões do Python e gere um erro programado por nós que seja de mais fácil
leitura. Provavelmente será um incremento futuro ao programa.
Ps2.: utilizei set e get para obter as imagens, porque elas são variáveis da
classe, logo é uma boa prática colocar esses nomes.
"""
from PIL import Image


class ImageObject(object):
    """
    Class: Propriedades básicas das imagens.

    img_path: caminho até a imagem;
    img: a imagem.
    """

# Classe com propriedades básicas de imagens.

    def __init__(
                 self, img_path,
                 img=None):
        self.img_path = img_path
        self.img = Image.open(img_path)

    def setImage(
                 self, img_path):
        """
        Parameters.

        ----------
        img_path :STRING. Caminho até a imagem.

        Returns
        -------
        None.

        """
# Abre a imagem dada pelo img_path, mas não a fecha.
# Eu posso tentar colocar a opção para fechar a função no arquivo "main"
        try:
            self.img = Image.open(img_path)
        except Exception as erro:  # Cuidado com esses Exceptions geneŕicos.
            print(f'O tipo do erro é {erro}')
            print(f'O erro encontrado foi {erro.__cause__}')

    def getImage(self):
        """
        Return None.

        -------
        TYPE
            Mostra a imagem aberta anteriormente.

        """
        try:
            return self.img.show()  # Achar uma foram de fechar a imagem
        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'O erro encontrado foi {erro.__cause__}')

    def closeImage(self):
        """
        Return None.

        -------
        None.

        """
        try:
            self.img.close()
            self.img = None
        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'O erro encontrado foi {erro.__cause__}')

    def showAtributes(self):
        """
        Return None.

        -------
        None.

        """
        print("Imagem = ", self.img_path)
        print("Mostrar imagem", self.img.show())
