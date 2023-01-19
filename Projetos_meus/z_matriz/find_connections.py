"""
Trabalho final de Python
"""

import os.path
from numpy import genfromtxt
from math import dist
from itertools import combinations
from dados_ligacoes import elem_raio_dict

def get_from_xyz(path, archive_name):
    """
    In: o caminho para o arquivo; nome do arquivo.

    Out: 1. coordinates: uma numpy array contendo as coordenadas xyz do arquivo.
         2. symbols: uma lista que contém os símbolos dos átomos.
         3. total_atoms: um inteiro contendo o total de átomos do sistema.
         4. symbol_index: uma lista com todos os índices dos átomos.

    """
    ###############################################################

    total_atoms = 0 # Variável para guardar o número total de átomos
    symbols = [] # Lista para guardar os symbols
    float_xyz=[]
    symbol_index = []
    index = 0

    ###############################################################

    xyz_path = os.path.join(path, archive_name) # Abrindo arquivo
    xyz_file = genfromtxt (fname=xyz_path, skip_header=2, dtype='unicode') # Puxando para o np
    symbols_desorganized = xyz_file[:,0] # Pega os símbolos em uma linha
    
    for atom in symbols_desorganized: # Laço para conseguir o n° total de átomos.
        total_atoms += 1

    np_symbols = symbols_desorganized.reshape(total_atoms, 1) # Transforma a matriz em coluna

    for np_symbol in np_symbols: # Faz uma lista de str
        symbols.append(str(np_symbol[0]))

    #x_coordinates = (xyz_file[:,1]) deixo essas 3 como opções, caso
    #y_coordinates = (xyz_file[:,2]) queiram uma coordenada específica.
    #z_coordinates = (xyz_file[:,3])
    coordinates = (xyz_file[:,1:]) # Pegando as coordenadas
    coordinates = coordinates.tolist() # Transformando-as em float
    for np_list in coordinates:
        float_xyz.append(list(map(float, np_list)))

    for atom in symbols:
        index +=1
        symbol_index.append(index)
    index = 0

    return (float_xyz, symbols, total_atoms, symbol_index)

def atoms_combinations(list_name):
    """
    In: uma lista.

    Out: todas as combinações possíveis entre 2 átomos.
    """ 
    #list_names=list(name_dist_dict.keys()) # Pega só os nomes no dicionário
    return list(combinations(list_name, 2))

def real_dist(xyz_vec_list):

    """
    In: uma lista com listas de coordenadas.

    Out: uma lista com as distâncias entre esses átomos.
    """
    real_dist_list = []
    xyz_vec_comb_list = []

    xyz_vec_combination = atoms_combinations(xyz_vec_list)
    for combination in xyz_vec_combination:
        real_dist_list.append(dist(combination[0], combination[1]))
    return real_dist_list 


# Por que eu não facilito a minha vida e diminuo a quantidade de dados, já que eu tenho
# a relação de átomos utilizados.

def lig_dist_from_atoms_combinations(symbol_list):
    """
    In: uma lista com os símbolos dos átomos.

    Out: duas listas. 
    1. sym_combi_list: lista com todas as combinações dos nomes dos átomos possíveis.
    2. dist_database: lista com as distâncias padrões de todas as combinações possíveis da molécula xyz.

    Ps.: depois mudar o nome desta função, pois está muito grande.
    """
    cov_rad_molecules=[] # Lista para guardar todas as combinações das distâncias padrões dos átomos.
    dist_database = [] # Lista para guardar as 1.3x a distância padrão dos átomos.
    sym_combi_list = []

    for working_atoms in range(len(symbol_list)): # Iterando entre os átomos da molécula problema
        for database_atoms in list(elem_raio_dict.keys()): # Iterando entre os elementos da lista padrão
            if symbol_list[working_atoms][0] == database_atoms: # Comparando os dois
                #print(f"O elemento {symbol_list[working_atoms][0]} é igual a {database_atoms}")
                #print(f"O raio do elemento {database_atoms} é: {elem_raio_dict.get(database_atoms)}")
                cov_rad_molecules.append(elem_raio_dict.get(database_atoms)) # Add o valor padrão ligação em uma lista
    combined_atoms = atoms_combinations(cov_rad_molecules) 

    for combi in combined_atoms: # loop para fazer a soma das distâncias padrões 
        soma = combi[0] + combi[1] # dos atomos, corrigidos para ser 1.3x maior
        soma = (soma * 1.3)
        dist_database.append(round(soma, 4))
    
    # Fazendo uma lista com todas as combinações de átomos possíveis.
    sym_combi = atoms_combinations (symbol_list)
    for i in sym_combi:
        sym_combi_list.append(list(i))

    return sym_combi_list, dist_database

def search_connect_atoms(real_atoms_list, sym_combi_list, dist_database_list, atom_index):
    """
    In: três listas.
    1. real_atoms_list: lista com as distâncias reais dos átomos.
    2. sym_combi_list: lista com todas os símbolos de todas as combinações possíveis.
    3. dist_database_list: lista com 1.3x de toda as combinações de distância possíveis.

    Out: uma lista que contém tuples dos átomos ligados e suas distâncias.
    """
    
    connected_atoms = []
    suffled_index_list = []
    connected_atoms_list = []
    all_infos_list = []
    
    #print(atom_index)
    suffled_index = atoms_combinations(atom_index)    
    for i in suffled_index:
       suffled_index_list.append(list(i)) 
    #print(suffled_index_list)

    atoms_info_tupple = list(zip(sym_combi_list, real_atoms_list, suffled_index_list)) 

    for atoms in range(len(atoms_info_tupple)):
        if (atoms_info_tupple[atoms][1] < dist_database_list[atoms]):
            connected_atoms.append(atoms_info_tupple[atoms])
    for i in connected_atoms:
        connected_atoms_list.append(list(i))

    for i in atoms_info_tupple:
        all_infos_list.append(list(i))

    return connected_atoms_list, atoms_info_tupple 

if __name__ == "__main__":
    pass
