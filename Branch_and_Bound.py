import numpy as np
from scipy.sparse import csr_matrix


def bandwidth_bnb(matrix=csr_matrix):
    k = np.amax(matrix.getnnz(0))
    b = int(np.ceil(k/2))

    return k
