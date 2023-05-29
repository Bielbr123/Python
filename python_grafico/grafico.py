path='/home/gabriel/python_grafico/out2_50ns_nvt_x1_4_peq.out'
numbers=int
matriz=[]

with open(path, "r") as file:
    for l_no, line in enumerate(file):

        if 'Step' in line:
            step_number = l_no + 1; matriz.append(line.split())
            break
            
        else:
            pass

    for line in file:
        splited_line=line.strip().split()
        if len(splited_line) >= 2:
            if splited_line[0].isnumeric() == True:
                matriz.append(splited_line)
                #print(splited_line)
                #print(matriz)
            else:
                pass
        else:
            pass
    file.close()

