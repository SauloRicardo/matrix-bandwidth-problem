import numpy as np
from scipy.sparse import csr_matrix
import Auxiliary_Functions as Af
import copy

upo_global = []


def bandwidth_bnb(matrix=csr_matrix):
    bandwidth = Af.objective_function(matrix)
    k = np.amax(matrix.getnnz(0)-1)
    b = int(np.ceil(k/2))
    while b <= k:
        print("While : ")
        unselected = list(range(0, matrix.get_shape()[0]))
        adj_list = []
        upo = []
        add_node(matrix, unselected, adj_list, upo, 0, b)
        b += 1

    # print(upo_global)


def add_node(matrix, unselected, adj_list, upo, i, b):
    global upo_global
    matrix_aux = copy.deepcopy(matrix)
    upo_aux = copy.deepcopy(upo)
    if i == matrix.get_shape()[0]:
        print("Entrei no IF")
        upo_global = upo_aux
        return upo_aux

    for node in unselected:
        unselected_aux = copy.deepcopy(unselected)
        unselected_aux.remove(node)
        adj_list_aux = copy.deepcopy(adj_list)
        for x in matrix_aux[node].indices:
            adj_list_aux.append(x)

        adj_remove = []
        for x in adj_list_aux:
            if x not in unselected_aux:
                adj_remove.append(x)

        for x in adj_remove:
            adj_list_aux.remove(x)

        if len(adj_list_aux) <= b:
            print(upo_aux)
            upo_aux.append(node)
            upo_general = add_node(matrix_aux, unselected_aux, adj_list_aux, upo_aux, i+1, b)
            if len(upo_general) > 0:
                print(upo_general)
                continue
