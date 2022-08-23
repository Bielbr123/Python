"""
!/usr/bin/envpython3.

 -*- coding: utf-8 -*-

Created on Sat Jul 16 20:50:47 2022

@author: gabriel

Modified: 18/07/2022
"""
from PIL import Image

from imageObject import ImageObject
"""
Adicionando algumas opções de tratamento de imagem
Atributos herdados: openImage, showImage, checkSize, closeImage, showAtributes.
Usar o comando dir para mostrar os atributos de uma classe.
"""


class ImageOptions(ImageObject):
    """Class: base options for a program that treat image."""

    def __init__(self, img_path):
        self.img_path = img_path
        self.img = Image.open(img_path)
        self.tempImg = None

    def checkSizeImage(self):
        """Return Check the dimensions of a image."""
        try:
            width, height = self.img.size
            print(f'O comprimento da imagem é {width}, e o da altura ', end='')
            print('é {height}, em pixels.')

        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'O erro encontrado foi {erro.__cause__}')

    def resizeImage(self, width, length):
        """
        Parameters.

        ----------
        width : INT. The new width of the image.
        length : INT. The new length of the image.

        Returns
        -------
        None.
        """
        new_size = (width, length)
        try:
            if self.tempImg is not None:
                self.tempImg = self.tempImg.resize(new_size,
                                                   Image.Resampling.LANCZOS)
                print('Foi possível efetuar o redimensionamento da imagem')

            else:
                self.tempImg = self.img.resize(new_size,
                                               Image.Resampling.LANCZOS)
                print('Foi possível efetuar o redimensionamento da imagem')

        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'Foi causado por: {erro.__cause__}')

    def thumbanilImage(self, width=None, length=None):
        """
        Parameters.

        ----------
        width : INT. The new width of the image.
        length : INT. The new length of the image.

        Returns
        -------
        Modifica o tamanho da imagem sem perder a qualidade
        """
        new_size = (width, length)
        try:
            if self.tempImg is not None:
                self.tempImg = self.tempImg.thumbnail(new_size)
                print('Foi possível efetuar o redimensionamento da imagem')

            else:
                self.tempImg = self.img.thumbnail(new_size)
                print('Foi possível efetuar o redimensionamento da imagem')

        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'Foi causado por: {erro.__cause__}')

    def saveFinalImage(self, final_image_name, image_format):
        """
        Return a saved image after the editions that the user has done.

        -------
        It doesn't overrid the original image, only creates another one and
        save it.
        final_image_name = the name given to the image before the filters and
        modifications.
        image_format = the format that the users wants to save the image. The
        core available options: JPEG and PNG.
        """
        image_format_upper = image_format.upper()
        try:
            imagemFinal = self.tempImg
            print(f'O tipo de tempImg é {type(imagemFinal)}')
            return imagemFinal.save(final_image_name, image_format_upper)

        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'O erro encontrado foi {erro.__cause__}')
