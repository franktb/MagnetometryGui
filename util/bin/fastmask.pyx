# fastmask.pyx

from libc.math cimport fabs
from cython.parallel import prange
import numpy as np
cimport numpy as np
cimport cython
from cython.parallel cimport parallel
from libc.math cimport sqrt


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def compute_mask(double[:] coord_array,
                 double[:] targets,
                 double tol):
    cdef Py_ssize_t coord_len = coord_array.shape[0]
    cdef Py_ssize_t target_len = targets.shape[0]
    cdef np.ndarray[np.uint8_t, ndim=1] mask = np.zeros(coord_len, dtype=np.uint8)

    cdef Py_ssize_t i, j
    cdef double current

    with nogil:
        for i in prange(coord_len, schedule='static'):
            current = coord_array[i]
            for j in range(target_len):
                if fabs(current - targets[j]) <= tol:
                    mask[i] = 1  # True
                    break
    return mask.astype(np.bool_)

def compute_pairwise_mask(
                        np.ndarray[np.float64_t, ndim=2] coords,
                        np.ndarray[np.float64_t, ndim=2] selected,
                        double tol):
    cdef Py_ssize_t i, j
    cdef Py_ssize_t n_coords = coords.shape[0]
    cdef Py_ssize_t n_selected = selected.shape[0]
    cdef np.ndarray[np.uint8_t, ndim=1] mask = np.zeros(n_coords, dtype=np.bool_)

    cdef double dx, dy, dist

    for i in range(n_coords):
        for j in range(n_selected):
            dx = coords[i, 0] - selected[j, 0]
            dy = coords[i, 1] - selected[j, 1]
            dist = sqrt(dx * dx + dy * dy)
            if dist <= tol:
                mask[i] = True
                break

    return mask