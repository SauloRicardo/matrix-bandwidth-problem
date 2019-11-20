import numpy as np
from scipy.sparse import csr_matrix
from scipy.io import mmread
import Auxiliary_Functions
import Branch_and_Bound as bnb


row = np.array([0, 1, 2, 3, 0, 3])
col = np.array([0, 1, 2, 3, 3, 0])
data = np.array([1, 1, 1, 1, 1, 1])
matrix = csr_matrix((data, (row, col)), shape=(4, 4))
print(matrix.toarray())
print(bnb.bandwidth_bnb(matrix))

#matrix = Auxiliary_Functions.swap_indices(2, 3, matrix)
#matrix = Auxiliary_Functions.swap_indices(2, 1, matrix)
#print(matrix.toarray())

# matrix = Auxiliary_Functions.swap_indices(0, 1, matrix)
# matrix = Auxiliary_Functions.swap_indices(1, 2, matrix)
# matrix = Auxiliary_Functions.swap_indices(1, 2, matrix)
# matrix = Auxiliary_Functions.swap_indices(0, 1, matrix)
# print(matrix.toarray())
# a = mmread('rel3.mtx')
# print(a)
# print(a.toarray())
# b = a.tocsr()
# print(b)

