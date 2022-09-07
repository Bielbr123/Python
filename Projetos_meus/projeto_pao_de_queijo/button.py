import PySimpleGUI as sg



def a(products,
      normal_input=False,
      description='Selecione o produto que irá vender',
      list_to_append=[], 
      show_products = True):
    """
    Parameter.
    ----------
    description : INT.
        DESCRIPTION. The name that will apear above the searchbar.'.
    products : LIST.
        DESCRIPTION. The list of available products.
    show_products : BOOL.
        DESCRIPTION.  If true, shows a list of available products will appear 
        when the seller try to search for one.
    Returns
    -------
    None.

    """
    list_to_append.append(sg.Text(description))
    
    # Colocar o id que ficará vinculado ao nome do produto.
    if normal_input==True:
        list_to_append.append([sg.Input('', expand_x=True, 
                   enable_events=True, key='-INPUT-')])
    else:
        pass
        
    # Mostra a lista de produtos disponíveis
    if show_products == True:
        width = max(map(len, products.values()))
        list_to_append.append([sg.Listbox(products, size=(width, 7),
                   enable_events=True, key='-LISTBOX-')]
            )
    else:
        print("Ocorreu um erro")
        
    return [list_to_append]
