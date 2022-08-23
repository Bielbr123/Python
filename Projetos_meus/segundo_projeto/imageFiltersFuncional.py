#/usr/bin/env python3.9.7
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:47:16 2022

Código para utilizar os filtros da biblioteca PIL de forma simplificada.

@author: gabriel
"""

from PIL import Image, ImageFilter

from imageObject import ImageObject


def gaussBlur(path, radius=2):
    """
    Parameter.

    ----------
    imageObject : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    tempImg = Image.open(path)
    tempImg = tempImg.filter(
              ImageFilter.GaussianBlur(
                  radius)
        )
    return tempImg.show()


gaussBlur('t', 2) 
