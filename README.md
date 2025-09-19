# Semi-Dense Feature Matching

Precise GIS layers are essential for smart-city services and autonomous navigation. However, pedestrian-level assets such as sidewalks and vegetation buffers remain poorly mapped in most urban databases. AI-generated imagery offers a way to complement these datasets, but only if its synthesised views can be accurately aligned. To address this challenge, we introduce a feature-to-feature knowledge distillation (KD) framework that produces an ultra-lightweight neural network (student) capable of extracting semi-dense features from images. These features yield semantically rich keypoint correspondences that support translation, rotation, and scale restoration. The framework distils geometric expertise from a high-capacity teacher into a compact student, built on a Mamba model. Our evaluation focuses on aligning GIS features, covering roads, sidewalks, buildings, and vegetation. The KD-Mamba matcher boosts alignment accuracy and reaches an 86% post-correction similarity rate. The proposed method outperforms classical feature-based baselines, SIFT and ORB, by a wide margin (around 12%). Compared with state-of-the-art deep homography estimators, it achieves similar precision while cutting computational cost by 40%. These gains stem from the model’s ability to capture long-range geometric dependencies with O(N ) complexity. By tightening the spatial registration of AI-generated imagery, our approach enables the reliable fusion of street-level, aerial, and satellite data into coherent pedestrian GIS layers. This paves the way for high-fidelity maps that support next-generation urban applications.
---

## **Contents**

### **Scripts**

1. **`script.py`**:
   - Implements MPI-based parallel processing for image filtering.
   - Steps:
     - Reads an input image (`lena.png`) on the root process.
     - Divides the image into overlapping patches and scatters them to worker processes.
     - Applies FFT, low-pass filtering, and IFFT to each patch.
     - Trims overlaps and reconstructs the image on the root process.
     - Saves the reconstructed image and spectrograms for each patch.

2. **`final.sh`**:
   - SLURM script to run the `script.py` on an HPC cluster.
   - Configures the environment, loads necessary modules, and submits the job.

### **Images**

- **Input Image**:
  - `lena.png`: Original RGB image.
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
   - The root process reads the input image (`lena.png`) and divides it into overlapping patches.

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

