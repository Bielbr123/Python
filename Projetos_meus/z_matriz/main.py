""" Ps.: no começo só eu e Deus sabíamos como este código funciona. Agora só Deus sabe. """

import math

# Padrão para importar em outros locais: from nome_pasta import nome_arquivo. Esse era o meu erro, eu vou precisar importar o arquivo todo.
# Na hora que eu for utilizar a função, terei de colocar ".", exemplo: dados_ligacoes.elem_raio_dict(). Acho que fazer isso será legal, pois
# a pasta do programinha está muito poluída. Olhe que eu nem comecei, e provavelmente nem farei, o tratamento de erro. Assim fica até melhor,
# pois eu deixo explícito a pasta de onde a função está vindo, resultando em uma organização melhor.
from dados_ligacoes import elem_raio_dict
from find_connections import get_from_xyz, atoms_combinations, lig_dist_from_atoms_combinations, real_dist, search_connect_atoms
from angles import find_angles, index_xyz, angles
from dihedrals import find_dihedrals, dihe_index_xyz, calc_dihedral, dihedral

# Pega as informações do arquivo xyz.
xyz_list, symbols, total_atoms, symbol_index = get_from_xyz("/home/gabriel/Modelos/estructures_pdynamo/fosfato/temp/", "fosfato_test.xyz")

# Pegar a distância calculada dos arquivos xyz.
atoms_real_dist = real_dist(xyz_list)

# listas com todas as combinações dos nomes e a distância padrão de todas as combinações possíveis da molécula xyz.
symbol_combi, dist_database = lig_dist_from_atoms_combinations(symbols)

# connected_atoms: todos os átomos conectados.
# atoms_infos: lista com listas dos átomos conectados, distância calculada do xyz e o índice dos átomos conectados.
connected_atoms, atoms_infos = search_connect_atoms(atoms_real_dist, symbol_combi, dist_database, symbol_index)

# Encontrando os índices dos átomos envolvidos nos ângulos.
angles_molecules = find_angles(connected_atoms)

# Retorna as distâncias de ligação no padrão da função "find_angles".
ordely_xyz = index_xyz(xyz_list, angles_molecules)

# Calcula os ângulos desejados da molécula.
angles = angles(ordely_xyz)
unsorted_index_angles = list(zip(angles_molecules, angles))
index_angles = sorted(unsorted_index_angles)

# Encontra os índices dos diedros
dihedrals_index = find_dihedrals(angles_molecules)

# Encontra as coordenadas dos átomos dos diedros, e os ordena no formato certo.
ordelyDihe_xyz = dihe_index_xyz(xyz_list, dihedrals_index)

# Os ângulos estão encontrados, agora eu preciso arrumar os quadrantes deles, ou seja, revisar trigonometria.
# Ps.: o resultado já está em graus.
dihedrals = dihedral(ordelyDihe_xyz)

"""
temp = []
for atom in range(len(connected_atoms)):
    temp.append(connected_atoms[atom][2])
print(temp)
#sorted_temp = sorted(temp)
#print(sorted_temp)
"""

# Ps.: todos os símbolos precisam ficar com 2 casas, a fim de formatar certinho a matriz z.
# Ps2.: coisa pra krl para fazer essa matriz-z.
def z_matrix(total_atoms, symbols, symbol_index, atoms_infos, connected_atoms, index_angles):
    """
    In: 1. Total_atoms: int com o número total de átomos. 
    Não sei ainda.

    Out: a matriz-z da molécula.
    """
    # Ps.: preciso de uma lista com todas as combinações que já ocorreram.
    # Iterando entre todos os átomos do sistema.
    combi_contadas = []
    connect_indices = [0, 0, 0]
    for atom in range(total_atoms):

        # Escrevendo o primeiro átomo.
        if atom == 0:
            print(symbols[atom])

        # Escrevendo o segundo átomo.
        elif atom == 1:
            print(symbols[atom], end='   ')
            print(symbol_index[atom-1], end=' ')
            print(format(atoms_infos[0][1], '.6f'))
            combi_contadas.append([1, 2])

        # Escrevendo o terceiro átomo.
        elif atom == 2: 
            temp = [ 1, 2, 3 ]
            print(symbols[atom], end='   ')
            print(symbol_index[atom-2], end=' ')
            print(format(atoms_infos[1][1], '.6f'), end='   ')
            print('2', end=' ')
            print(format(index_angles[0][1], '.6f'))
            combi_contadas.append([1,3])
        
        elif atom >= 3:


        # Dentro do loop atom > 3 da matriz-z.
            temp = [ ]
            dist = [ ]
            temp_possi = []
            actual_index = []
            indices_finais = 0
       

# Não tem como eu utilizar átomos que apareçam depois do meu atual! Um dos critérios para fazer a matriz-z.
            # Itero entre a quantidade total de átomos na molécula.
            for i in range(len(connected_atoms)):
                # Checo para saber em quais combinações esse átomo aparece.
                if atom in connected_atoms[i][2]:
                    #print("\n", connected_atoms[i][2])
                    # Adiciono as combinações na lista temp
                    temp.append(connected_atoms[i][2])
                else:
                    pass
            
            # Itero para remover as combinações que não podem ocorrer.
            for a in temp:
    # Removendo as que forem maior do que o número de átomo atual, as que não estão dispostas na matriz para serem referências.
                b = max(a)
                if b <= atom:
                    temp_possi.append(a)
                else:
                    pass
            
            # Removendo as combinações de índices que já foram contabilizadas.
            for combi in temp_possi:
                if combi not in combi_contadas:
                   indices_finais = combi 
                else:
                    pass

            for indice in indices_finais:
                if indice != atom:
                    connect_indices.append(indice)
                else:
                    pass
        print(symbols[atom], end='   ')
        print(connect_indices[atom])
            #print(connect_indices)


        # Finalmete consegui resolver o problema de conectividade da matriz z! Isso para quando os átomos estão conectados, agora eu preciso
        # pensar em como ficará, caso eles não estjam conectados. Ou seja, haja trabalho nesta porra eim.
            #print(indices_finais)



z_matrix(total_atoms, symbols, symbol_index, atoms_infos, connected_atoms, index_angles)
#print(connected_atoms)
#print(atoms_infos)

# Itero entre o total de átomos. Se atom > 2, ou seja, a partir do quarto átomo, eu devo ir na lista dos átomos conectados e ver em quais
# combinações o átomo está. Assim eu saberei quantas ligações ele fará. É uma boa ideia. A partir daí é começar a printar essas ligações, e ter
# cuidado com as repetidas. Precisarei de uma forma de mudar as ligações repetidas. Talvez criar uma lista temporária vazia e ir adicionando os
# índices os quais já foram feitas ligações antes. Ir adicionando as ligações de forma ordenada do menor para o maior, facilitando assim a minha
# vida na hora de procurar os índices e fazer comparações. Dessa forma, eu poderei comparar listas com listas. Exemplo: a lista [2, 6] será igu-
# al a lista [6, 2]. Sendo assim, quando eu estiver no atom = 6, eu irei ordenar a lista, virando [2, 6] e poderei checar se essa combinação já
# printada anteriormente. Nesse exemplo, sim, ela já foi. Legal, acho que já tenho toda a lógica para fazer a função que estou querendo.

