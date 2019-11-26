import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import csgraph
from scipy.io import mmread
import Auxiliary_Functions
import Branch_and_Bound as bnb
import tentativa


row = np.array([0, 1, 2, 3, 4, 1, 0, 4, 0])
col = np.array([0, 1, 2, 3, 4, 0, 1, 0, 4])
data = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
matrix = csr_matrix((data, (row, col)), shape=(5, 5))
print(matrix.toarray())
print(csgraph.reverse_cuthill_mckee(matrix, symmetric_mode=True))
# print(Auxiliary_Functions.objective_function_csr(matrix))
# print(bnb.bandwidth_bnb(matrix).toarray())
# print(tentativa.bandwidth_bnb(matrix).toarray())

# matrix = Auxiliary_Functions.swap_indices(2, 3, matrix)
# matrix = Auxiliary_Functions.swap_indices(2, 1, matrix)
# print(matrix.toarray())

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

