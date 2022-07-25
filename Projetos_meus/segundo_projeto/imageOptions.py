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
"""


class ImageOptions(ImageObject):
    """Class: base options for a program that treat image."""

    def __init__(self, img_path):
        self.img_path = img_path
        self.img = Image.open(img_path)

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
            self.img = self.img.resize(new_size, Image.Resampling.LANCZOS)
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
            self.img = self.img.thumbnail(new_size)
            print('Foi possível efetuar o redimensionamento da imagem')
        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'Foi causado por: {erro.__cause__}')

    def test(self, letra=None):
        self.__letra = letra
        print(letra)
