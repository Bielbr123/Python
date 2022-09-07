import PySimpleGUI as sg      

items = ["item 1", "item 2", "item 3"]

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()],
                 [sg.InputCombo(items, size=(20, 1), key="items_combobox")]] 

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)
