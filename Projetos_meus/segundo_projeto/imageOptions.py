#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 20:50:47 2022

@author: gabriel

Modified: 18/07/2022 
"""
from PIL import Image

from imageObject import ImageObject

class ImageOptions(ImageObject):
# Adicionando algumas opções de tratamento de imagem
# Atributos: openImage, showImage, checkSize, closeImage, showAtributes.
    
    def __init__(self, img_path):
        self.img_path = img_path
        self.img = Image.open(img_path)
        
        
    def checkSizeImage(self):
# Checa o tamanho da imagem
        try:
            width, height = self.img.size
            print(f'O comprimento da imagem é {width}, e o da altura é {height}, em pixels.')
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')

    
    def resizeImage(self, width = None, length = None):
# Modifica o tamanho da imagem
        new_size = (width, length)
        try:
            self.img = self.img.resize(new_size, Image.Resampling.LANCZOS)
            print('Foi possível efetuar o redimensionamento da imagem')
        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'Foi causado por: {erro.__cause__}')
    
    def thumbanilImage(self, width = None, length = None):
# Modifica o tamanho da imagem sem perder a qualidade
        new_size = (width, length)
        try:
            self.img = self.img.thumbnail(new_size)
            print('Foi possível efetuar o redimensionamento da imagem')
        except Exception as erro:
            print(f'O tipo do erro é {erro}')
            print(f'Foi causado por: {erro.__cause__}')

