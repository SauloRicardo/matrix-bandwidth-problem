from scipy.sparse import csr_matrix
import copy

def objective_function_csr(matrix_fun=csr_matrix):
    bandwidth = 0
    for row_for in range(0, (int(matrix_fun.get_shape()[0] - 1))):
        indices_aux = list(matrix_fun[row_for].indices)
        bandwidth_aux = int(indices_aux[len(indices_aux)-1]) - row_for
        if bandwidth_aux > bandwidth:
            bandwidth = bandwidth_aux

    return bandwidth


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


def swap_all_indices(list_aux, matrix=csr_matrix):
    matrix_aux = copy.deepcopy(matrix)
    print(list_aux)
    cont = 0
    swap_indices(4, 0, matrix_aux)
    swap_indices(4, 1, matrix_aux)
    swap_indices(4, 2, matrix_aux)
    swap_indices(3, 3, matrix_aux)
    swap_indices(4, 4, matrix_aux)

    print(matrix_aux.toarray())
    # return matrix_aux

'''
def objective_function(matrix_fun=csr_matrix):
    bandwidth = 0
    for row_for in range((int(matrix_fun.get_shape()[0]-1)), 0, -1):
        for col_for in range(row_for):
            if row_for-col_for > bandwidth:
                if(col_for == 0) or (col_for == 1):
                    if matrix_fun[row_for, col_for] != 0:
                        bandwidth = row_for-col_for
                        return bandwidth
                else:
                    bandwidth = row_for-col_for
    return bandwidth
'''
