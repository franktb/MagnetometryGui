import scipy.ndimage as ndi

def running_mean_uniform_filter1d(x, N):
    return ndi.uniform_filter1d(x, N, mode='reflect')