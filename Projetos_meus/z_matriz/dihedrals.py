from itertools import combinations
from numpy import linalg, array, dot, cross, arctan2, degrees

def find_dihedrals(angles_index):
    """
    In: 1. Angles_index: lista com listas dos índices do átomos conectados.
    Out: 1. Lista com listas dos diedros da molécula.
    """
    suffled_angles = []
    temp_lists_added = []
    dihedrals_index = []

    # Fazendo todas as combinações das listas de index dos ângulos
    temp_suffled_angles = list(combinations(angles_index, 2)) 
        
    # Transformando as tupples das combinações em listas
    for tupple in temp_suffled_angles:
        suffled_angles.append(list(tupple))

    # Pegando os dihedros, ou seja, ângulos que possuem 2 átomos em comum
    for atom in range(len(suffled_angles)):
        id_angles1 = suffled_angles[atom][0]
        id_angles2 = suffled_angles[atom][1] 
        is_connected = (set(id_angles1).intersection(set(id_angles2)))
        is_connected_list = list(is_connected)
        if len(is_connected_list) == 2:
            # Criando uma lista, com elementos repetidos, dos átomos do dihedro
            temp_lists_added.append(id_angles1 + id_angles2)

    # Removendo os átomos repetidos
    for index in temp_lists_added:
        res = [*set(index)]
        dihedrals_index.append(res)

    return dihedrals_index 

def dihe_index_xyz(xyz_list, dihedrals_index):
    """
    In: 1. xyz_list: lista com os símbolos dos átomos.
        2. dihedrals_index: lista com os índices dos diedrais.
    out: 1. ordelyDihe_xyz: lista contendo listas das coordenadas xyz ordenadas de forma igual ao dihedrals_index. 
    """

    oneD_DiheIndex = []
    oneD_Dihexyz_ordened = []

    # Adicionando os indíces na lista oneD_DiheIndex.
    for angles_connected in dihedrals_index:
        #print(angles_connected)
        for index in angles_connected:
            oneD_DiheIndex.append(index)
    #print(oneD_DiheIndex)

    # Ordenando as coordenadas, de acordo com os índices dos diedrais.
    for index in oneD_DiheIndex:
        oneD_Dihexyz_ordened.append(xyz_list[index-1])
    #print(oneD_Dihexyz_ordened)

    ordelyDihe_xyz = []
    temp_ordely = []

    for atom in range(len(oneD_Dihexyz_ordened)):
        if atom == 0:
            temp_ordely.append(oneD_Dihexyz_ordened[atom])
        elif (atom%4 != 0):
            temp_ordely.append(oneD_Dihexyz_ordened[atom])
        elif (atom%4 == 0):
            ordelyDihe_xyz.append(temp_ordely)
            temp_ordely = []
            temp_ordely.append(oneD_Dihexyz_ordened[atom])
        else:
            print("Tem um erro no else da função dihe_index_xyz")
    
    return ordelyDihe_xyz

def calc_dihedral(list_xyz):
    """
    In: 1. ordelyDihe_xyz: uma lista contendo listas com as coordenadas dos átomos.
    Out: 1. dihedral: o cálculo dos ângulos diedros.

    """
    v0 = list_xyz[0]
    v1 = list_xyz[1]
    v2 = list_xyz[2]
    v3 = list_xyz[3]

    a0 = -1.0*(v1 - v0)
    a1 = v2 - v1
    a2 = v3 - v2

    a1 /= linalg.norm(a1)

    c = a0 - dot(a0, a1)*a1
    d = a2 - dot(a2, a1)*a1

    x = dot(c, d)
    y = dot(cross(a1, c), d)
    dihedral = degrees(arctan2(y, x))

    return dihedral 

def dihedral(ordelyDihe_xyz):
    """
    In: 1. ordelyDihe_xyz: lista contendo listas ordenadas de xyz.
    Out: 1. dihedral: lista contendo os diedros calculados.
    """
    dihedral = []
    for xyz_list in ordelyDihe_xyz:
        nump = array(xyz_list)
        dihedral_np = calc_dihedral(nump)
        dihedral.append(dihedral_np)

    return dihedral

if __name__ == "__main__":
    pass
