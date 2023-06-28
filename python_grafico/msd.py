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
    csvData = []
    lines = file.readlines()
    strLine = lines[1:]
    strData = [num.split(';') for num in strLine]
    file.close()

    for strList in strData:
        templist = []
        for strNum in strList:
            templist.append(float(strNum))
        csvData.append(templist)
        templist = []

    time = []; msd = []; derivate = []
    for unfiData in csvData:
        time.append(round(unfiData[0]*3.337, 2))
        msd.append(round(unfiData[1]/100, 2))
        derivate.append(round(unfiData[2], 3))
"""
plt.plot(time, msd)
plt.legend("Temp")
plt.xlabel("Time (ns)")
plt.ylabel("MSD (Å²)")
plt.show()
"""
plt.plot(time, derivate)
plt.legend("Temp")
plt.xlabel("Time (ns)")
plt.ylabel("Coef. Difu")
plt.show()
