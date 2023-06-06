import matplotlib.pyplot as plt
from statistics import mean

path='/home/gabriel/python_grafico/out2_x1_3_peq.lmp'
matrix=[]; labels=[]
data_y=[]; data_x=[]
list_density=[]
x_index=1; y_index=2

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
for density in matrix:
    list_density.append(density[densi_index])
avg_density = mean(list_density)

for data in matrix:
    data_y.append(data[y_index-1])
    data_x.append(data[x_index-1])

plt.plot(data_x, data_y)
plt.ylabel(labels[y_index-1])
plt.xlabel(labels[x_index-1])
plt.title('Temp')
plt.show()

print(f'O valor médio da caixa de simulação é: {avg_density}')
