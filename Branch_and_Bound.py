import numpy as np
from scipy.sparse import csr_matrix
import Auxiliary_Functions as Af
import copy


def bandwidth_bnb(matrix=csr_matrix):
    # matrix_aux = copy.deepcopy(Af.upper_bound_rcm(matrix))
    matrix_aux = copy.deepcopy(matrix)
    upper_bound = Af.objective_function_csr(matrix)
    lower_bound = Af.simple_lower_bound(matrix)
    while True:
        if Af.objective_function_csr(matrix_aux) == lower_bound:
            return matrix_aux

# def bandwidth_bnb(matrix=csr_matrix):
#     # bandwidth = Af.objective_function_csr(matrix)
#     k = np.amax(matrix.getnnz(0)-1)
#     b = int(np.ceil(k/2))
#     while True:
#         unselected = list(range(0, matrix.get_shape()[0]))
#         adj_list = []
#         row_column_upo = np.array(list(range(0, matrix.get_shape()[0])))
#         data_upo = np.array([1]*matrix.get_shape()[0])
#         upo = csr_matrix((data_upo, (row_column_upo, row_column_upo)), shape=(matrix.get_shape()))
#         min_mat = add_node(matrix, unselected, adj_list, upo, 0, b)
#         if min_mat is not None:
#             if min_mat.getnnz() > 0:
#                 return min_mat
#
#         b += 1
#
#     # print(upo_global)
#
#
# def add_node(matrix, unselected, adj_list, upo, i, b):
#     matrix_aux = copy.deepcopy(matrix)
#     upo_aux = copy.deepcopy(upo)
#
#     if i == matrix.get_shape()[0]-1:
#         return upo_aux
#
#     for node in unselected:
#         upo_aux = copy.deepcopy(upo)
#
#         indices_aux = list(matrix_aux[node].indices)
#         indices_aux.remove(node)
#         # print(indices_aux)
#         for x in indices_aux:
#             upo_aux.__setitem__((i, x), 1)
#             upo_aux.__setitem__((x, i), 1)
#
#         unselected_aux = copy.deepcopy(unselected)
#         unselected_aux.remove(node)
#         adj_list_aux = copy.deepcopy(adj_list)
#         for x in matrix_aux[node].indices:
#             adj_list_aux.append(x)
#         adj_remove = []
#         for x in adj_list_aux:
#             if x not in unselected_aux:
#                 adj_remove.append(x)
#
#         for x in adj_remove:
#             adj_list_aux.remove(x)
#
#         print("Node : " + str(node))
#         print("Coluna, i : " + str(i))
#         print("UPO AUX")
#         print(upo_aux.toarray())
#         print('Adj : ' + str(len(adj_list_aux)))
#         print('band : ' + str(Af.objective_function_csr(upo_aux)))
#         print('b - band + 1 : ' + str(b-Af.objective_function_csr(upo_aux)+1))
#         if len(adj_list_aux) <= b-Af.objective_function_csr(upo_aux)+1:
#             print("UPO AUX REC")
#             print(upo_aux.toarray())
#             upo_general = add_node(matrix_aux, unselected_aux, adj_list_aux, upo_aux, i+1, b)
#             if upo_general is not None:
#                 if upo_general.getnnz() > 0:
#                     return upo_general
