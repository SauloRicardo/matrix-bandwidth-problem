import numpy as np
from scipy.sparse import csr_matrix
from scipy.io import mmread


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


row = np.array([0, 1, 2, 3, 3, 2])
col = np.array([0, 1, 2, 3, 2, 0])
data = np.array([1, 1, 1, 1, 1, 1])
matrix = csr_matrix((data, (row, col)), shape=(4, 4))
test = matrix.toarray()
print(objective_function(matrix))
#print(matrix.get_shape()[0])
print(test)

#a = mmread('rel3.mtx')
#print(a)
#print(a.toarray())
#b = a.tocsr()
