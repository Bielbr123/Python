#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:47:16 2022

Código para utilizar os filtros da biblioteca PIL de forma simplificada.

@author: gabriel
"""

from PIL import Image, ImageFilter

# from imageObject import ImageObject

filters = {'gaussBlur': 'radius',
           'boxBlur': 'radius',
           'unsharpMask': 'radius',
           'rankFilter': ['size', 'rank'],
           'modeFilter': 'size',
           'contourFilter': None,
           'edgeEnhanceFilter': None
           }


def printFilters(filters):

    print('Os filtros disponíves são:')
    j = 1
    for i in filters.keys():
        print(f'{j}. {i}')
        j += 1
    j = 1


printFilters(filters)
x = input('Digite o filtro desejado: ')


def selectFilters(filters):
    for i in filters.keys():
        pass


'''
a = Image.open('t')
a.filter(ImageFilter.CONTOUR())
a.show()
'''
