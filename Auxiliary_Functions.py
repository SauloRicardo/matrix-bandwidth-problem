from scipy.sparse import csr_matrix
import copy
from scipy.sparse import csgraph


def objective_function_csr(matrix_fun=csr_matrix):
    bandwidth = 0
    for row_for in range(0, (int(matrix_fun.get_shape()[0] - 1))):
        indices_aux = list(matrix_fun[row_for].indices)
        bandwidth_aux = int(indices_aux[len(indices_aux)-1]) - row_for
        if bandwidth_aux > bandwidth:
            bandwidth = bandwidth_aux

    return bandwidth


def bandwidth_row(row, matrix_fun=csr_matrix):
    indices_aux = list(matrix_fun[row].indices)
    return int(indices_aux[len(indices_aux) - 1]) - row


def swap_indices(ind1, ind2, matrix_fun):
    for row_for in range((int(matrix_fun.get_shape()[0]))):
        if (row_for != ind1) and (row_for != ind2):
            if matrix_fun.__getitem__((ind1, row_for)) != matrix_fun.__getitem__((ind2, row_for)):
                ind1_value = matrix_fun.__getitem__((ind1, row_for))
                matrix_fun.__setitem__((ind1, row_for), matrix_fun.__getitem__((ind2, row_for)))
                matrix_fun.__setitem__((row_for, ind1), matrix_fun.__getitem__((ind2, row_for)))

                matrix_fun.__setitem__((ind2, row_for), ind1_value)
                matrix_fun.__setitem__((row_for, ind2), ind1_value)
                matrix_fun.eliminate_zeros()

    return matrix_fun


def upper_bound_rcm(matrix=csr_matrix):
    rcm = csgraph.reverse_cuthill_mckee(matrix, symmetric_mode=True)
    matrix_aux = copy.deepcopy(matrix)
    cont = 0
    list_aux = list(range(0, len(rcm)))
    rcm = list(rcm)
    rcm.pop()
    for x in rcm:
        swap_indices(list_aux.index(x), list_aux.index(cont), matrix_aux)
        list_aux[list_aux.index(x)], list_aux[list_aux.index(cont)] = \
            list_aux[list_aux.index(cont)], list_aux[list_aux.index(x)]
        cont += 1

    return matrix_aux


def simple_lower_bound(matrix=csr_matrix):
    non_zero = int((matrix.getnnz() - matrix.get_shape()[0])/2)
    cont = 0
    # print(non_zero)
    for x in range(matrix.get_shape()[0]-1, 0, -1):
        cont += 1
        non_zero -= x
        if non_zero <= 0:
            return cont
    # return cont

# def objective_function(matrix_fun=csr_matrix):
#     bandwidth = 0
#     for row_for in range((int(matrix_fun.get_shape()[0]-1)), 0, -1):
#         for col_for in range(row_for):
#             if row_for-col_for > bandwidth:
#                 if(col_for == 0) or (col_for == 1):
#                     if matrix_fun[row_for, col_for] != 0:
#                         bandwidth = row_for-col_for
#                         return bandwidth
#                 else:
#                     bandwidth = row_for-col_for
#     return bandwidth
