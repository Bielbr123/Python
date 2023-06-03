from os import getcwd
import matplotlib.pyplot as plt
from glob import glob

path = "/home/gabriel/mestrado/projeto/simulacao/cloreto_etil_amonia_resultados/resultados/python_grafico/"
directory= getcwd() + "/"
"""
inp=input("Deseja realizar os cálculos no diretório atual? [Sim] ou [Não]")
if inp.upper()[0] == 'S' or 'Y':
    path=directory
    print("Lendo os arquivos .out e csv para realizar o gráfico dos rdf's no diretório atual.")
    print("Caso não tenham arquivos compatíveis com as extensões do script, nada será retornado.", end='')
    print("Se houverem arquivos compatíveis com as extensões, mas não forem logs do rdf do lammps ou do travis, o script falhará.")
else:
    pass
"""
outRdf = glob(path + "*.out"); outNames = [name.split("/")[-1] for name in outRdf]
csvRdf = glob(path + "*.csv"); csvNames = [name.split("/")[-1] for name in csvRdf]
namesRdf=outNames+csvNames
distRdf=[]; gRrdf=[]

# Obtendo datas dos rdfs do lammps
for outFile in range(len(outNames)):
    floatRdf=[]
    floatGr=[]
    with open(outRdf[outFile], "r") as file:
        lines = file.readlines()
        last_lines = lines[-150:]
        strData = [num.split() for num in last_lines] 
        file.close()

    for strList in strData:
        templist = []
        for strNum in strList:
            templist.append(float(strNum))
        floatRdf.append(templist[1:2][0])
        floatGr.append(templist[2:3][0])
        templist=[]
    distRdf.append(floatRdf)
    gRrdf.append(floatGr)

# Obtendo data dos rdfs do travis
# Ps.: melhorar o entendimento das variáveis abaixo
for csvFile in range(len(csvNames)):
    csvData=[]
    with open(csvRdf[csvFile], "r") as file:
        allLines = file.readlines()
        lines = allLines[1:]
        strData = [num.split(";") for num in lines]
        file.close()

    for strList in strData:
        templist = []
        for strNum in strList:
            templist.append(float(strNum))
        csvData.append(templist)
        templist = []

    a=[]
    for data in csvData:
        if data[0]/100 <= 12.0:
            data[0]=round(data[0]/100, 2)
            data[1]=round(data[1], 4)
            data[2]=round(data[2], 4)
            a.append(data)
        else:
            pass

    temp=[]; temp2=[]
    for i in a:
        temp.append(i[:1][0])
        temp2.append(i[1:2][0])
    distRdf.append(temp)
    gRrdf.append(temp2)
    temp=[]; temp2=[]

# Realizando o plot dos dados
# Ps.: talvez seja mais fácil utilizar a biblioteca Pandas.
for rdf in range(len(namesRdf)):
    x=distRdf[rdf]
    y=gRrdf[rdf]
    plt.plot(x, y)
plt.legend(namesRdf, loc=0, frameon=True)
plt.title("Função de distribuição radial das\n frações molares do DES cloreto de etilamônio com uréia")
plt.xlabel("Distância (Å)")
plt.ylabel("g(R)")
plt.show()
