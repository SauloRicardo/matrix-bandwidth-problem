import numpy as np
from scipy.sparse import csr_matrix
import Auxiliary_Functions as Af
import copy


def bandwidth_bnb(matrix=csr_matrix):
    bandwidth = Af.objective_function(matrix)
    k = np.amax(matrix.getnnz(0)-1)
    b = int(np.ceil(k/2))
    while b <= k:
        unselected = list(range(0, matrix.get_shape()[0]))
        adj_list = []
        upo = []
        add_node(matrix, unselected, adj_list, upo, 0, b)
        b += 1
    return bandwidth


def add_node(matrix, unselected, adj_list, upo, i, b):
    matrix_aux = copy.deepcopy(matrix)
    if i == matrix.get_shape()[0]:
        return matrix_aux

    for node in unselected:
        unselected_aux = list(range(0, matrix.get_shape()[0]))
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
            add_node(matrix_aux, unselected_aux, adj_list_aux, i+1, b)
