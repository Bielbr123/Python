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

sg.theme('DarkGrey13')    # Keep things interesting for your users

items = [1, 2, 3, 4]
#width = max(map(len, all_files))

# Make the welcome upper texts
upper_texts = [
    [sg.Push(), # Centered Text 
     sg.Text('A melhor loja de pão de queijo do Brasil.',
            font=('', 13, 'bold'),
            text_color='CornFlowerBlue'), 
     sg.Push()
    ], 
    [sg.Text('Selecione o que você quer fazer:', font=('', 11, 'bold'))]
              ]

# Product manager buttons, more products lixtbox
buttons_more_Product_box=[    
     [sg.vtop(sg.Button('Selecionar Produto (F1)')), # Button 1 alligned top
     sg.vtop(sg.Button('Alterar Produto (F2)')), # Button 2
     sg.vtop(sg.Button('Retirar produto (F3)')), # button 3
     sg.Push(), sg.Text('Produtos disponíveis: ', font=('', 10, 'bold'))], # Right listbox text
    [sg.Push(), sg.Listbox(items, default_values=None, # Listbox alligned right 
                           key="a",size=(20, 5) # Depois mudar esse "5" para um valor automático e que dependa da quantidade de items.
                           )
     ]
                         ]

# Show, input and check price
products_and_price = [
    [sg.Text('Insira a quantidade de produto em:', font=('', 10, 'bold')),
     sg.Radio("Kg", "group1", key="gramatura"), 
     sg.Radio("Gramas", "group1", key="gramatura", 
              default=True)
    ],
    [sg.InputText(key="source")],
    [sg.Text('')],
    [sg.Text('Carrinho: \n', font=('', 10, 'bold'))] # Ainda irei integrar o valor do produto aqui.
        ]

payment_type = [
          [sg.Text("Selecione a forma de pagamento:", font=('', 10, 'bold')), 
          sg.Radio("Crédito", "group2", key="Resolver_depois", default=True), 
          sg.Radio("Débito", "group2", key="Resolver_depois"),
          sg.Radio("Pix", "group2", key="Resolver_depois"),
          sg.Radio("Dinheiro", "group2", key="Resolver_depois")],
               ]

deliver_product = [
            [sg.Text("Entrega ou compra presencial?", font=('', 10, 'bold')),
             sg.Radio("Entrega", "group3", key="Delivery", default=True),
             sg.Radio("Retirada", "group3", key="Delivery")]
                  ]

layout = upper_texts + buttons_more_Product_box + products_and_price + payment_type + deliver_product

window = sg.Window('Sistema de vendas do Pedro', layout , size = (800, 500 ))

while True:                             # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
