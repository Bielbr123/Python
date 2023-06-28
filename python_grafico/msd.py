from os import getcwd
from glob import glob
import matplotlib.pyplot as plt

path = "/home/gabriel/mestrado/projeto/simulacao/cloreto_etil_amonia_resultados/resultados/python_grafico/"
directory= getcwd() + "/"

while True:
    inp=input("Deseja realizar os cálculos no diretório atual? [Sim] ou [Não]")

    if inp == '':
        print("Digite Sim ou Não (também pode ser em inglês) \n")
            
    elif inp.upper()[0] == 'S' or inp.upper()[0] == 'Y':
        path=directory
        print("\n")
        print("Lendo os arquivos .msd e csv para realizar o gráfico dos rdf's no diretório atual.")
        print("Caso não tenham arquivos compatíveis com as extensões do script, nada será retornado.", end='')
        print("Se houverem arquivos compatíveis com as extensões, mas não forem logs do rdf do lammps ou do travis, o script falhará.")
        print("Saindo do loop")
        break
    
    elif inp.upper()[0] == 'N':
        path=str(input("Digite o caminho até o arquivo desejado: ")) + "/"
        break

    else:
        print("Digite Sim ou Não (também pode ser em inglês)")

msdRdf = glob(path + "*.msd"); msdNames = [name.split("/")[-1] for name in msdRdf]
csvRdf = glob(path + "*.csv"); csvNames = [name.split("/")[-1] for name in csvRdf]
namesRdf=msdNames+csvNames
distRdf=[]; gRrdf=[]
#print(msdRdf)

with open(msdRdf[0], "r") as file:
    lines = file.readlines()
    data = lines[1:]
    strData = [num.split() for num in data]
    file.close()
print(strData)
