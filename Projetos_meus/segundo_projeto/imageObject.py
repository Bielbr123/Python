'''
Created on Sat Jul 15 20:17:38 2022

@author: gabriel

Modified: 16/07/2022
'''
from PIL import Image

class ImageObject(object):
# Classe com propriedades básicas de imagens.


    def __init__(
                 self, img_path):
        self.img_path = img_path
        self.img = Image.open(img_path)
        
        
    def openImage(
                 self, img_path):
# Abre a imagem dada pelo img_path, mas não a fecha.
# Eu posso tentar colocar a opção para fechar a função no arquivo "main"
        try:
            self.img = Image.open(img_path) 
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            
            
    def showImage(self):
# Mostra a imagem aberta     
        try:
            return self.img.show() # Achar uma foram de fechar a imagem
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            
            
    def checkSize(self):
# Checa o tamanho da imagem
        try:
            width, height = self.img.size
            print(f'O comprimento da imagem é {width}, e o da altura é {height}, em pixels.')
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            
    
    def closeImage(self):
# Tenta fechar a imagem aberta. Pode ser que não seja útil, vamos ver.
        try:
            self.img.close()
            self.img = None
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            
            
    def showAtributes(self):
# Utilizado para debuggar
        print("Imagem = ", self.img_path)
        print("Mostrar imagem", self.img.show())
        
