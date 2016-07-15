import numpy as np

def morgan(matrix):
    dim = len(matrix)
    A = np.zeros((dim, dim))
    #A[:, 0] = matrix[:, 0] * np.sqrt(matrix.diagonal())
    A[0, 0] = np.sqrt(matrix[0, 0])

    #print matrix
    for i, row in enumerate(matrix[1:]):
        A[i+1, i+1] = np.sqrt(matrix[i+1, i+1] - np.sum(A[i+1, :i] * A[i+1, :i]))
        for j, s in enumerate(row[:i]):
            A[i, j] = matrix[i, j] - np.sum(A[i,:j-1] * A[j,:j-1])
            A[i, j] /= A[i+1, i+1]
        #A[i, i+1] = np.sqrt()
    print A
    #print matrix[:, 0] * np.sqrt(matrix.diagonal())
    return dim
