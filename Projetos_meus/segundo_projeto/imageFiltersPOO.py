"""
Created on Sat Jul 18 1:00:00 2022.

@author: gabriel

Modified: 18/07/2022
Aqui estarão os filtros que serão utilizados para o meu programa. Aparentemente
utilizei apenas a biblioteca Pillow para isso, mas, provavelmente eu tenha
finde
usando a OpenCV ou a Keras.
"""

from PIL import Image, ImageFilter

from imageObject import ImageObject


class ImageFilterObject(ImageObject):
    """
    Class: coloca filtros na imagem.

    img_path: caminho até a imagem desejada;
    img = a imagem desejada.
    """

    def __init__(self, img_path):
        self.img_path = img_path
        self.img = Image.open(img_path)
        self.tempImg = None

    def gaussBlur(self, radius=2):
        """
        Return.

        -------
        radius: INT. Size of the box in one direction. Radius 0 does not blur,
        returns an identical image. Radius 1 takes 1 pixel in each direction,
        i.e. 9 pixels in total.
        """
        print(f"O tipo de tempImg é {type(self.tempImg)}")
        if self.tempImg is not None:
            # A condição acima é para qualquer tipo fora None
            # é muito geral, depois restringir.

            self.tempImg = self.tempImg.filter(
                        ImageFilter.GaussianBlur(
                                    radius)
                        )
            print(f'Dentro do if. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

        else:
            self.tempImg = self.img.filter(
                    ImageFilter.GaussianBlur(
                                    radius)
                    )
            print(f'Dentro do else. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

    def boxBlur(self, radius=2):
        """
        Parameter.

        ----------
        radius : INT.Size of the box in one direction. Radius 0 does not blur,
        returns an identical image. Radius 1 takes 1 pixel in each direction,
        i.e. 9 pixels in total.

        Returns
        -------
        None.

        """
        if self.tempImg is not None:
            # A condição acima é para qualquer tipo fora None
            # é muito geral, depois restringir.

            print(f'O tipo do tempImg é {type(self.tempImg)}')
            self.tempImg = self.img.filter(
                        ImageFilter.BoxBlur(
                                    radius)
                        )
            print(f'Dentro do if. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

        else:
            self.tempImg = self.img.filter(
                        ImageFilter.BoxBlur(
                                   radius)
                        )
            print(f'Dentro do else. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

    def unsharpMask(self, radius=2,
                    percent=150, trheshold=3
                    ):
        """
        Parameter.

        ----------
        radius : INT, optional
            DESCRIPTION. The default is 2. Blur radius.
        percent : INT, optional
            DESCRIPTION. The default is 150. Unsharp strength, in percent.
        trheshold : INT, optional
            DESCRIPTION. The default is 3. Control the minimum brigthness ex-
            planation that will be sharpened.

        Returns
        -------
        None.
        """
        if self.tempImg is not None:
            # A condição acima é para qualquer tipo fora None
            # é muito geral, depois restringir.

            print(f'O tipo do tempImg é {type(self.tempImg)}')
            self.tempImg = self.img.filter(
                ImageFilter.UnsharpMask(
                            radius, percent,
                            trheshold)
                                          )
            print(f'Dentro do if. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

        else:
            self.tempImg = self.img.filter(
                ImageFilter.BoxBlur(
                            radius, percent,
                            trheshold)
                                          )
            print(f'Dentro do else. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

    def rankFilter(self, size=9, rank=2):
        """
        Parameter.

        ----------
        size : INT, optional
            DESCRIPTION. The default is 9.T he kernel size, in pixels.
        rank : INT, optional
            DESCRIPTION. The default is 2.What pixel value to pick. Use 0 for
            a min filter, size * size / 2 for a median filter,
            size * size - 1 for a max filter, etc.
        Return.
        -------
        None.
        """
        if self.tempImg is not None:
            # A condição acima é para qualquer tipo fora None
            # é muito geral, depois restringir.

            print(f'O tipo do tempImg é {type(self.tempImg)}')
            self.tempImg = self.img.filter(
                ImageFilter.RankFilter(
                            size, rank)
                                          )
            print(f'Dentro do if. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

        else:
            self.tempImg = self.img.filter(
                ImageFilter.RankFilter(
                            size, rank)
                                          )
            print(f'Dentro do else. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

    def modeFilter(self, size=3):
        """
        Parameter.

        ----------
        size : INT, optional
            DESCRIPTION. The default is 9.T he kernel size, in pixels.
        Return.
        -------
        None.
        """
        if self.tempImg is not None:
            # A condição acima é para qualquer tipo fora None
            # é muito geral, depois restringir.

            print(f'O tipo do tempImg é {type(self.tempImg)}')
            self.tempImg = self.img.filter(
                ImageFilter.ModeFilter(size))
            print(f'Dentro do if. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

        else:
            self.tempImg = self.img.filter(
                ImageFilter.ModeFilter(size))
            print(f'Dentro do else. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

    def contourFilter(self):
        """
        Return.

        -------
        None.

        """
        if self.tempImg is not None:
            # A condição acima é para qualquer tipo fora None
            # é muito geral, depois restringir.

            print(f'O tipo do tempImg é {type(self.tempImg)}')
            self.tempImg = self.img.filter(
                ImageFilter.CONTOUR())
            print(f'Dentro do if. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()
        else:
            self.tempImg = self.img.filter(
                ImageFilter.CONTOUR())
            print(f'Dentro do else. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()

    def edgeEnhanceFilter(self):
        """
        Return.

        -------
        None.

        """
        if self.tempImg is not None:
            # A condição acima é para qualquer tipo fora None
            # é muito geral, depois restringir.

            print(f'O tipo do tempImg é {type(self.tempImg)}')
            self.tempImg = self.img.filter(
                ImageFilter.EDGE_ENHANCE_MORE())
            print(f'Dentro do if. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()
        else:
            self.tempImg = self.img.filter(
                ImageFilter.EDGE_ENHANCE_MORE())
            print(f'Dentro do else. O tipo de tempImg é {type(self.img)}')
            self.tempImg.show()
