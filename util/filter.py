import scipy.ndimage as ndi
import numpy as np

def running_mean_uniform_filter1d(x, N):
    return ndi.uniform_filter1d(x, N, mode='reflect')


class DownwardContinuation():
    def upward_continue(self, T0, dz, ):
        nx, ny = T0.shape
        kx = np.fft.fftfreq(nx, ) * 2 * np.pi
        ky = np.fft.fftfreq(ny, ) * 2 * np.pi
        KX, KY = np.meshgrid(kx, ky, indexing='ij')
        K = np.sqrt(KX ** 2 + KY ** 2)

        T0_hat = np.fft.fft2(T0)
        Tz_hat = T0_hat * np.exp(-K * dz)
        Tz = np.real(np.fft.ifft2(Tz_hat))
        return Tz


    def horizontal_laplacian_fft_pad(self, T, k_c=2 * np.pi / 150, pad_fraction=0.1):
        nx, ny = T.shape
        pad_x = int(nx * pad_fraction)
        pad_y = int(ny * pad_fraction)
        T_pad = np.pad(T, ((pad_x, pad_x), (pad_y, pad_y)), mode='reflect')  # 'reflect' works better than 'constant'

        # Step 2: Set up FFT frequency grid
        nx_pad, ny_pad = T_pad.shape
        kx = np.fft.fftfreq(nx_pad, ) * 2 * np.pi
        ky = np.fft.fftfreq(ny_pad, ) * 2 * np.pi
        KX, KY = np.meshgrid(kx, ky, indexing='ij')
        K2 = KX ** 2 + KY ** 2

        gaussian_filter = np.exp(-K2 / (2 * k_c ** 2))

        # Step 4: Compute Laplacian in frequency space
        T_hat = np.fft.fft2(T_pad)
        lap_hat = -K2 * T_hat * gaussian_filter
        lap = np.fft.ifft2(lap_hat).real

        # Step 5: Crop back to original shape
        lap_crop = lap[pad_x:pad_x + nx, pad_y:pad_y + ny]

        return -lap_crop


    def iterative_downward_finite(self, T_obs, dz, n_iter=3):
        print(T_obs)
        Tn_h = (2 * T_obs
                - self.upward_continue(T_obs, dz, )
                + self.horizontal_laplacian_fft_pad(T_obs,) * np.square(dz))

        for i in range(n_iter):
            Tn_0 = self.upward_continue(Tn_h, dz, )

            delTn_0 = T_obs - Tn_0
            rmse = np.sqrt(np.mean((delTn_0) ** 2))
            print("RMSE:", rmse)

            delTn_h = (
                    2 * delTn_0
                    - self.upward_continue(delTn_0, dz, )
                    + self.horizontal_laplacian_fft_pad(delTn_0, ) * np.square(dz)
            )

            Tn_h = Tn_h + delTn_h

        return Tn_h