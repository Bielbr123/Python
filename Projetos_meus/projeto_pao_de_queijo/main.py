#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:11:24 2022

@author: gabriel
GUI:
    1. Botão para selecionar entre os produtos disponíveis;
    2. Botão para checar o preço dos produtos;
    3. Botão para cadastrar novo produto;
    4. Botão para checar preço do novo produto;

"""

import PySimpleGUI as sg
import style 

sg.theme('DarkAmber')    # Keep things interesting for your users

items = ["item 1", "item 2", "item 3"]
#width = max(map(len, all_files))

layout = [
          [sg.Text('A melhor loja de pão de queijo mineiro')], # Nome central superior
          [sg.Text('Produto da venda: ')], # Mostra o estoque
          [sg.InputCombo(items, size=(20, 10), key="items_combobox")], # Lista produtos cadastrados
          [sg.Text('O preço do produto escolhido é:')], # 
          [sg.Text('Futuro valor dos produtos')], # Ainda irei integrar o valor do produto aqui.
          [sg.Text("Selecione a forma de pagamento:"), 
          sg.Radio("Crédito", "group1", key="Resolver_depois", default=True), 
          sg.Radio("Débito", "group1", key="Resolver_depois"),
          sg.Radio("Pix", "group1", key="Resolver_depois"),
          sg.Radio("Dinheiro", "group1", key="Resolver_depois")]
        ]

window = sg.Window('Sistema de vendas do Pedro', layout, size = (700, 500 ))

while True:                             # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
