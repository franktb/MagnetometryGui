# fastmask.pyx

from libc.math cimport fabs
from cython.parallel import prange
import numpy as np
cimport numpy as np
cimport cython
from cython.parallel cimport parallel
from libc.stdio cimport printf

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def compute_mask(double[:] coord_array,
                 double[:] targets,
                 double tol):
    cdef Py_ssize_t coord_len = coord_array.shape[0]
    cdef Py_ssize_t target_len = targets.shape[0]
    cdef np.ndarray[np.uint8_t, ndim=1] mask = np.zeros(coord_len, dtype=np.uint8)

    cdef np.ndarray[np.uint8_t, ndim=1] jarray = np.zeros(coord_len, dtype=np.uint8)

    cdef Py_ssize_t i#, j
    cdef double current

    #targets.sort()

    #printf("Hello")

    for i in prange(coord_len, nogil=True, schedule='dynamic'):
        current = coord_array[i]

        # Move forward to find the first targets[j] >= current  - tol
        while jarray[i] < target_len and targets[jarray[i]] < current  - tol:
            jarray[i] += 1

        # Check if we're still within bounds and inside ±tol
        if jarray[i] < target_len and fabs(current  - targets[jarray[i]]) <= tol:
            #printf("Hello")
            mask[i] = 1
    return mask.astype(np.bool_)
