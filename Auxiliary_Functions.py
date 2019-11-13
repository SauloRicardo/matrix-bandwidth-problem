from scipy.sparse import csr_matrix


def objective_function(matrix_fun):
    bandwidth = 0
    for row_for in range((int(matrix_fun.get_shape()[0])), 0, -1):
        for col_for in range(row_for-1):
            if row_for-1-col_for > bandwidth:
                if(col_for == 0) or (col_for == 1):
                    if matrix_fun[row_for-1, col_for] != 0:
                        bandwidth = row_for-1-col_for
                        return bandwidth
                else:
                    bandwidth = row_for-1-col_for
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
