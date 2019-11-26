import numpy as np
from scipy.sparse import csr_matrix
import Auxiliary_Functions as Af
import copy


def bandwidth_bnb(matrix=csr_matrix):
    # bandwidth = Af.objective_function_csr(matrix)
    k = np.amax(matrix.getnnz(0)-1)
    b = int(np.ceil(k/2))
    while True:
        unselected = list(range(0, matrix.get_shape()[0]))
        adj_list = []
        row_column_upo = np.array(list(range(0, matrix.get_shape()[0])))
        data_upo = np.array([1]*matrix.get_shape()[0])
        upo = csr_matrix((data_upo, (row_column_upo, row_column_upo)), shape=(matrix.get_shape()))
        min_mat = add_node(matrix, unselected, adj_list, 0, b)
        if min_mat is not None:
            if min_mat.getnnz() > 0:
                return min_mat

        b += 1

    # print(upo_global)


def add_node(matrix, unselected, adj_list, i, b):
    matrix_aux = copy.deepcopy(matrix)

    if i == matrix.get_shape()[0]-1:
        return matrix_aux

    for node in unselected:
        matrix_aux = copy.deepcopy(matrix_aux)

        indices_aux = list(matrix_aux[node].indices)
        indices_aux.remove(node)
        # print(indices_aux)
        matrix_aux = Af.swap_indices(node, i, matrix_aux)

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

        print("MATRIX AUX")
        print(matrix_aux.toarray())
        print("Node : " + str(node))
        print("Coluna, i : " + str(i))
        print('Adj : ' + str(len(adj_list_aux)))
        print('band : ' + str(Af.objective_function_csr(matrix_aux)))
        print('b - band + 1 : ' + str(b-Af.objective_function_csr(matrix_aux)+1))
        if len(adj_list_aux) <= b-Af.objective_function_csr(matrix_aux):
            print("MATRIX AUX REC")
            print(matrix_aux.toarray())
            matrix_aux = add_node(matrix_aux, unselected_aux, adj_list_aux, i+1, b)
            if matrix_aux is not None:
                if matrix_aux.getnnz() > 0:
                    return matrix_aux
            print("SAI DA RECURÇAO")
