from itertools import combinations
from numpy import linalg, dot, array, arccos, degrees

def find_angles(connected_atoms_info):
    """
    In: uma lista contendo iteráveis com as informações dos átomos.
    Out: uma lista contendo listas com os índices dos átomos.
    """

    angles_index = [ ] # Lista com booleanos. Servirá para dizer se há um ângulo entre os 3 átomos ou não.
    suffled_angles = [ ] # Tupple que virará lista
    suffled_angles_list = [ ] # Todas as combinações de ângulos possíveis
    index = 0

    for i in connected_atoms_info:
        suffled_angles.append(connected_atoms_info[index][2])
        index += 1 
    a = list(combinations(suffled_angles, 2)) 
    index = 0

    for i in a:
        suffled_angles_list.append(list(i))

    for atom in range(len(suffled_angles_list)):

        id_atoms1 = suffled_angles_list[atom][0]
        id_atoms2 = suffled_angles_list[atom][1] 
        is_connected = bool(set(id_atoms1).intersection(set(id_atoms2)))
        if is_connected == True:
            lista = set ( id_atoms1 + id_atoms2 )
            angles_index.append( list(lista) )

    return angles_index

def index_xyz(xyz_list, angles_index):
    """
    In: 1. xyz_list: uma lista com o os símbolos dos átomos.
        2. angles_list: uma lista contendo listas com os índices dos átomos. 
                        É o output da função a cima.
    Out: 1. ordely_list: guarda as distâncias em 3D, coincidindo com o formato que vem da função "find_angles".
    """
    oneD_index = []
    oneD_xyz_ordened = []

    for atom_connected in angles_index:
        for index in atom_connected:
            oneD_index.append(index)
    #print(oneD_index)

    for index in oneD_index:
        oneD_xyz_ordened.append(xyz_list[index-1])
    #print(oneD_xyz_ordened)

    ordely_xyz = []
    temp_ordely = []
    
    # Criando uma lista com os átomos ordenadas da mesma maneira que os átomos dos átomos que compoem os ângulos.
    for atom in range(len(oneD_xyz_ordened)):
        if atom == 0:
            temp_ordely.append(oneD_xyz_ordened[atom])
        elif (atom%3 != 0):
            temp_ordely.append(oneD_xyz_ordened[atom])
        elif (atom%3 == 0):
            ordely_xyz.append(temp_ordely)
            temp_ordely = []
            temp_ordely.append(oneD_xyz_ordened[atom])
        else:
            print(f"Tem um bug no programa na linha 64 do programa Angles.py.")

    return ordely_xyz 

def angles(ordely_xyz):
    """
    In: ordely_xyz da função anterior.

    Out: angles_list: lista que contém os ângulos entre os átomos que fazem sentido.
    """
    angles_list = []
    count = 0
    
    for xyz_list in range(len(ordely_xyz)):
        v = array(ordely_xyz[xyz_list][count  ])
        u = array(ordely_xyz[xyz_list][count+1])
        z = array(ordely_xyz[xyz_list][count+2])
        uv = u - v
        zv = z - v
        cos = ( dot (uv, zv) / ( linalg.norm(uv) * linalg.norm(zv) ) )
        angle = arccos(cos) 
        angles_list.append(degrees(angle))
    
    return angles_list

if __name__ == "__main__":
    pass

