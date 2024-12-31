from mpi4py import MPI
import numpy as np
import cv2
import os
import time

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Low-pass filter function
def low_pass_filter(freq_data, cutoff):
    h, w = freq_data.shape
    center_x, center_y = h // 2, w // 2
    mask = np.zeros((h, w), dtype=np.float32)
    for i in range(h):
        for j in range(w):
            if np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2) <= cutoff:
                mask[i, j] = 1
    return freq_data * mask

overlap = 10  # Define overlap size

overlap = 10  # Define overlap size

# Read image on the root process
if rank == 0:
    image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    patches_per_proc = h // size

    # Create patches with overlap
    patches = []
    for i in range(size):
        start_row = max(0, i * patches_per_proc - overlap)
        end_row = min(h, (i + 1) * patches_per_proc + overlap)
        patches.append(image[start_row:end_row, :])
else:
    patches = None

# Scatter patches to all processes
patch = comm.scatter(patches, root=0)

# Measure time for FFT
start_time = time.time()
fft_patch = np.fft.fftshift(np.fft.fft2(patch))
fft_time = time.time() - start_time

# Save spectrogram of the patch
spectrogram = np.log(1 + np.abs(fft_patch))  # Log scaling for better visualization
cv2.imwrite(f"spectrogram_rank_{rank}.png", (spectrogram / spectrogram.max() * 255).astype(np.uint8))

# Measure time for filtering
start_time = time.time()
cutoff = 20  # Define cutoff frequency
filtered_patch = low_pass_filter(fft_patch, cutoff)
filter_time = time.time() - start_time

# Measure time for IFFT
start_time = time.time()
ift_patch = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_patch)))
ifft_time = time.time() - start_time

# Trim overlap from the processed patch
trimmed_patch = ift_patch[overlap:-overlap, :] if rank > 0 and rank < size - 1 else (
    ift_patch[overlap:, :] if rank == 0 else ift_patch[:-overlap, :]
)

# Print timing information for each process
print(f"Rank {rank}: FFT time = {fft_time:.4f}s, Filter time = {filter_time:.4f}s, IFFT time = {ifft_time:.4f}s")

# Gather the processed patches
processed_patches = comm.gather(trimmed_patch, root=0)

# Reconstruct and save the image on the root process
if rank == 0:
    reconstructed_image = np.vstack(processed_patches)
    cv2.imwrite("reconstructed_image.png", reconstructed_image.astype(np.uint8))
    print("Reconstructed image and spectrograms saved successfully.")
