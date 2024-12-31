# MPI Image Processing Project

This repository contains an MPI-based image processing project that demonstrates the application of Fourier Transform (FFT), low-pass filtering, and Inverse Fourier Transform (IFFT) to an image using distributed computing.

The code is implemented using Python with the `mpi4py`, `numpy`, and `opencv-python` libraries. The project is designed to run on an HPC cluster using SLURM for job scheduling.

---

## **Contents**

### **Scripts**

1. **`script.py`**:
   - Implements MPI-based parallel processing for image filtering.
   - Steps:
     - Reads an input image (`lena.jpg`) on the root process.
     - Divides the image into overlapping patches and scatters them to worker processes.
     - Applies FFT, low-pass filtering, and IFFT to each patch.
     - Trims overlaps and reconstructs the image on the root process.
     - Saves the reconstructed image and spectrograms for each patch.

2. **`final.sh`**:
   - SLURM script to run the `script.py` on an HPC cluster.
   - Configures the environment, loads necessary modules, and submits the job.

### **Images**

- **Input Image**:
  - `lena.jpg`: Original grayscale image.
- **Output Images**:
  - `reconstructed_image.png`: Final reconstructed image after processing.
  - `spectrogram_rank_0.png`, `spectrogram_rank_1.png`, `spectrogram_rank_2.png`, `spectrogram_rank_3.png`: Spectrograms of image patches processed by different ranks.
### **Input vs Output Example**

#### **Input Image:**
![Input Image](lena.png)

#### **Output Image:**
![Reconstructed Image](reconstructed_image.png)
---

## **Requirements**

### **Dependencies**

- **Python Libraries**:
  - `mpi4py`
  - `numpy`
  - `opencv-python`
- **MPI Library**:
  - OpenMPI or compatible implementation

### **HPC Environment**

- SLURM workload manager
- Compatible with HPC clusters supporting MPI
- Conda for Python environment management

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/JoseLMedinaC/MPI4HPC
cd MPI4HPC
```

### **2. Prepare the Conda Environment**

```bash
module load any/python/3.8.3-conda
conda create -n myenv python=3.8 mpi4py opencv -c conda-forge
conda activate myenv
```

### **3. Submit the Job**

Edit `final.sh` to set the correct working directory and paths, then submit the job:

```bash
sbatch final.sh
```

---

## **Code Workflow**

1. **Image Reading**:
   - The root process reads the input image (`lena.jpg`) and divides it into overlapping patches.

2. **Patch Distribution**:
   - Patches are scattered to worker processes using MPI.

3. **FFT, Filtering, and IFFT**:
   - Each process computes the FFT of its patch, applies a low-pass filter, and then performs IFFT.

4. **Spectrogram Generation**:
   - Each rank saves a spectrogram of its FFT-transformed patch.

5. **Image Reconstruction**:
   - Trimmed patches are gathered on the root process, reconstructed, and saved as `reconstructed_image.png`.

---

## **Output Description**

- **Reconstructed Image (`reconstructed_image.png`)**:
  - The final image after applying FFT, filtering, and IFFT.

- **Spectrograms (`spectrogram_rank_X.png`)**:
  - Log-scaled visualizations of the frequency domain for each processed patch.

---

## **Example Execution**

### **1. Submit Job**

```bash
sbatch final.sh
```

### **2. View Output**

After the job completes, the following outputs will be saved:

- Reconstructed image: `reconstructed_image.png`
- Spectrograms: `spectrogram_rank_0.png`, `spectrogram_rank_1.png`, etc.

---

## **Contributing**

Contributions are welcome! Please submit pull requests or open issues for improvements.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**

Special thanks to the HPC course team and the contributors of `mpi4py` and `opencv-python` for enabling this project.

