#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:11:02 2022

@author: gabriel
"""

import requests
from tkinter import *

from procurar_pdf import *

janela = Tk()
janela.title("Procurar PDF's")

texto_orientacao = Label(janela, text ="Clique para abrir a pasta de procura")
texto_orientacao.grid(column = 0, row = 0)

texto_orientacao2 = Label(janela, text ="Clique aqui agora")
texto_orientacao2.grid(column = 1, row = 0)

botao = Button(janela, text="Buscar pdf's", command = pdf_location)
botao.grid(column = 0, row = 1)


janela.mainloop()   