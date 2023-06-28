from os import getcwd
from statistics import mean
import matplotlib.pyplot as plt

path=''
directory = getcwd() + "/log.lammps"

while True:
    inp=input("Deseja realizar os cálculos no diretório atual? [Sim] ou [Não]")

    if inp == '':
        print("Digite Sim ou Não (também pode ser em inglês) \n")
            
    elif inp.upper()[0] == 'S' or inp.upper()[0] == 'Y':
        path=directory
        print("\n")
        print("Lendo os arquivos .out e csv para realizar o gráfico dos rdf's no diretório atual.")
        print("Caso não tenham arquivos compatíveis com as extensões do script, nada será retornado.", end='')
        print("Se houverem arquivos compatíveis com as extensões, mas não forem logs do rdf do lammps ou do travis, o script falhará.")
        print("Saindo do loop")
        break
    
    elif inp.upper()[0] == 'N':
        path=str(input("Digite o caminho até o arquivo desejado: "))
        break

    else:
        print("Digite Sim ou Não (também pode ser em inglês)")

matrix=[]; labels=[]
data_y=[]; data_x=[]
list_density=[]; list_volume=[]
x_index=1; y_index=3

with open(path, "r") as file:
    for line in file:
        if 'Step' in line:
            labels=line.split()
            break
            
        else:
            pass

    for line in file:
        splited_line=line.strip().split()
        if len(splited_line) >= 2:
            if splited_line[0].isnumeric() == True:
                dados = [float(x) for x in splited_line]
                matrix.append(dados)
            else:
                pass
        else:
            pass
    file.close()

densi_index = labels.index("Lx")
volume_index = labels.index("Volume")

for density in matrix:
    list_density.append(density[densi_index])
avg_density = mean(list_density)

for volume in matrix:
    list_volume.append(volume[volume_index]) 
avg_volume = mean(list_volume)
lado_aumentado = ((avg_volume * 10 ) ** (1/3))

for data in matrix:
    data_y.append(data[y_index-1])
    data_x.append(data[x_index-1])

plt.plot(data_x, data_y)
plt.ylabel(labels[y_index-1])
plt.xlabel(labels[x_index-1])
plt.title('Gráfico Energia Potencial vs Passos \n EA_Br x1:2')
plt.show()

print(f'O valor médio da caixa de simulação é: {avg_density/2}')
print('-'*100)
print(f'O valor médio do lado para uma caixa 10x maior é: {lado_aumentado/2}')
print(f'Lembrar: nem sempre será necessário utilizar o valor acima, apenas quando for precisar criar um sistema 10x maior.')
