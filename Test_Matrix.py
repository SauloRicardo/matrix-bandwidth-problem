import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import csgraph
from scipy.io import mmread
import Auxiliary_Functions as Af
import Branch_and_Bound as bnb
import copy
import random

# row_full = np.array([0, 1, 2, 3, 4, 0, 0, 0, 0, 1, 2, 3, 4, 1, 1, 1, 2, 3, 4, 2, 2, 3, 4, 3, 4])
# col_full = np.array([0, 1, 2, 3, 4, 1, 2, 3, 4, 0, 0, 0, 0, 2, 3, 4, 1, 1, 1, 3, 4, 2, 2, 4, 3])
# data_full = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# dense_matrix = csr_matrix((data_full, (row_full, col_full)), shape=(5, 5))

# row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, 5, 6, 7, 0, 3, 2])
# col = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 0, 3, 2, 5, 6, 7])
# data = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# matrix_aux = csr_matrix((data, (row, col)), shape=(10, 10))



# # matrix_aux = Auxiliary_Functions.upper_bound_rcm(matrix)
# matrix_aux = bnb.bandwidth_bnb(matrix)
# print(matrix_aux.toarray())

# matrix_test = mmread('matrizes/Trefethen_20b.mtx').tocsr()
# tam = 10
# matrix_aux = csr_matrix((tam, tam), dtype=int)
# for x in range(0, tam):
#     for y in range(0, tam):
#         matrix_aux.__setitem__((x, y), matrix_test.__getitem__((x, y)))
#
# matrix_aux.setdiag(1)
# matrix_aux.eliminate_zeros()

tam = 25
matrix_aux = csr_matrix((tam, tam), dtype=int)
matrix_aux.setdiag(1)
for x in range(0, tam):
    for y in range(0, tam):
        ran = random.randrange(0, 100)
        if ran >= 96:
            matrix_aux.__setitem__((x, y), 1)
            matrix_aux.__setitem__((y, x), 1)

print("opa")
matrix_test = bnb.bandwidth_bnb(matrix_aux)
# matrix_test = Af.swap_indices(0, 1, matrix_aux)
print(matrix_test.toarray())
print(Af.objective_function_csr(matrix_test))

matrix_test = Af.upper_bound_rcm(matrix_aux)
print(Af.objective_function_csr(matrix_test))
# print(matrix_test.toarray())

# matrix_aux = Af.upper_bound_rcm(matrix_test)
# print(Af.objective_function_csr(matrix_aux))
# matrix_aux = bnb.bandwidth_bnb(matrix_test)
# print(Af.objective_function_csr(matrix_aux))
