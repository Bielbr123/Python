"""Documento feito para armazenar os estilos do front-end do projeto."""

# Provavelmente eu deveria colocar o valor do produto a ser mostrado junto com a opção de mostrar o nome
show_products1 = [[sg.Text('Escolha o produto a ser vendido: ')],
                  [sg.InputCombo(items, size=(20, 10), key="temp")]
                 ]

define_weight
