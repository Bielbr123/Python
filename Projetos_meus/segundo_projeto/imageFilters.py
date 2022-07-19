"""
Created on Sat Jul 18 1:00:00 2022.

@author: gabriel

Modified: 18/07/2022
Aqui estarão os filtros que serão utilizados para o meu programa. Aparentemente
utilizei apenas a biblioteca Pillow para isso, mas, provavelmente eu tenha
finde
usando a OpenCV ou a Keras.
"""

from PIL import Image

from imageObject import ImageObject


class ImageFilters(ImageObject):
    """
    Class: coloca filtros na imagem.

    img_path: caminho até a imagem desejada;
    img = a imagem desejada.
    """

    def __init__(
                 self, img_path,
                 img=None):
        self.img_path = img_path
        self.img = Image.open(img_path)
