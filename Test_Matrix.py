import numpy as np
from scipy.sparse import csr_matrix
from scipy.io import mmread
import Auxiliary_Functions
import Branch_and_Bound as bnb
import copy


# row_full = np.array([0, 1, 2, 3, 4, 0, 0, 0, 0, 1, 2, 3, 4, 1, 1, 1, 2, 3, 4, 2, 2, 3, 4, 3, 4])
# col_full = np.array([0, 1, 2, 3, 4, 1, 2, 3, 4, 0, 0, 0, 0, 2, 3, 4, 1, 1, 1, 3, 4, 2, 2, 4, 3])
# data_full = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# dense_matrix = csr_matrix((data_full, (row_full, col_full)), shape=(5, 5))

row = np.array([0, 1, 2, 3, 4, 4, 0])
col = np.array([0, 1, 2, 3, 4, 0, 4])
data = np.array([1, 1, 1, 1, 1, 1, 1])
matrix = csr_matrix((data, (row, col)), shape=(5, 5))
# print(matrix.toarray())

matrix = Auxiliary_Functions.upper_bound_rcm(matrix)
# print(Auxiliary_Functions.simple_lower_bound(matrix))

# print(bnb.bandwidth_bnb(matrix).toarray())

# print(Auxiliary_Functions.objective_function_csr(matrix))
# print(bnb.bandwidth_bnb(matrix).toarray())
# print(tentativa.bandwidth_bnb(matrix).toarray())

# print(matrix_result.toarray())

# matrix = Auxiliary_Functions.swap_indices(0, 1, matrix)
# print(matrix.toarray())
# matrix = Auxiliary_Functions.swap_indices(1, 2, matrix)
# matrix = Auxiliary_Functions.swap_indices(2, 3, matrix)
# matrix = Auxiliary_Functions.swap_indices(0, 1, matrix)
# print(matrix.toarray())
# a = mmread('rel3.mtx')
# print(a)
# print(a.toarray())
# b = a.tocsr()
# print(b)

