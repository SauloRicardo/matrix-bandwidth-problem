import numpy as np
from scipy.sparse import csr_matrix
from scipy.io import mmread
import Auxiliary_Functions


row = np.array([0, 1, 2, 3, 0, 3])
col = np.array([0, 1, 2, 3, 3, 0])
data = np.array([1, 1, 1, 1, 1, 1])
matrix = csr_matrix((data, (row, col)), shape=(4, 4))
print(matrix.toarray())
matrix_aux = Auxiliary_Functions.swap_indices(0, 1, matrix)
matrix_aux = Auxiliary_Functions.swap_indices(1, 2, matrix)
matrix_aux = Auxiliary_Functions.swap_indices(1, 2, matrix)
matrix_aux = Auxiliary_Functions.swap_indices(0, 1, matrix)
print(matrix_aux.toarray())
# a = mmread('rel3.mtx')
# print(a)
# print(a.toarray())
# b = a.tocsr()
# print(b)

