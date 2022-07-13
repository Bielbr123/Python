#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:04:28 2022

@author: gabriel
"""

from procurar_pdf import pdf_location, pdf_word_getter, directory_creation, txt_creator

palavra_desejada = input(str('Digite a palavra-chave a qual você quer buscar: '))
caminho = '/home/gabriel/Documentos/Testes'
#Localização dos pdf's
path_pdf = pdf_location(caminho)

#path_pdf = caminho até o pdf; segundo argumento é a palavra-chave que deseja
#que procure

pdf_word_getter(path_pdf, palavra_desejada)

#cria um diretório na pasta dos pdf's com o nome da palavra-chave usada na fun-
#ção anterior
directory_creation(caminho, palavra_desejada)

#cria um bloco de notas e salva os resultados nele
txt_creator()

