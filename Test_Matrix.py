import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import csgraph
from scipy.io import mmread
import Auxiliary_Functions
import Branch_and_Bound as bnb
import tentativa
import copy


row = np.array([0, 1, 2, 3, 4, 1, 0, 4, 0])
col = np.array([0, 1, 2, 3, 4, 0, 1, 0, 4])
data = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
matrix = csr_matrix((data, (row, col)), shape=(5, 5))
# print(matrix.toarray())
rcm = csgraph.reverse_cuthill_mckee(matrix, symmetric_mode=True)

Auxiliary_Functions.swap_all_indices(rcm, matrix)

# aux_swap = list(range(0, matrix.get_shape()[0]))
# cont = 0

# print(rcm)
# for x in rcm:
#     print(x, cont)
#     print(aux_swap[x], aux_swap[cont])
#     matrix = Auxiliary_Functions.swap_indices(aux_swap[x], aux_swap[cont], matrix)
#     aux_swap[aux_swap.index(x)] = aux_swap[cont]
#     aux_swap[cont] = x
#     # aux_swap[x] = cont
#     print(aux_swap)
#
#     cont += 1

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

