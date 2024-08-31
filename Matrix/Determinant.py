#determinant of matrices
import numpy as np
def Determinant_matrices(matA, matB):
    np_matA = np.array(matA, dtype=float)
    np_matB = np.array(matB, dtype=float)

    det_matA = np.linalg.det(np_matA) # Calculate determinant of matA
    det_matB = np.linalg.det(np_matB) # Calculate determinant of matB
    return det_matA, det_matB
