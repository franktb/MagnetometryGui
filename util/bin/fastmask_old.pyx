# fastmask.pyx

from libc.math cimport fabs
import numpy as np
cimport numpy as np

def compute_mask(np.ndarray[float, ndim=1] coord_array,
                     np.ndarray[float, ndim=1] targets,
                     float tol):
    cdef int coord_len = coord_array.shape[0]
    cdef int target_len = targets.shape[0]
    cdef np.ndarray[np.uint8_t, ndim=1] mask = np.zeros(coord_len, dtype=np.uint8)

    cdef int i, j
    cdef float current

    for i in range(coord_len):
        current = coord_array[i]
        for j in range(target_len):
            if fabs(current - targets[j]) <= tol:
                mask[i] = 1  # True
                break
    return mask.astype(np.bool_)
