#!/bin/bash
#SBATCH -J finallab
#SBATCH --partition=testing
#SBATCH -A ealloc_2cd39_hpc_joseluis1
#SBATCH -t 10:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=%x-%j.out

# Set the working directory
#cd /path/to/your/directory
cd  /gpfs/space/projects/hpc-course/hpc_joseluis/labFinal
# Load required modules
# Load MPI and Conda
module purge
module load any/python/3.8.3-conda
module load openmpi/4.1.3
#module load opencv/3.4.12
# Activate Conda environment
source activate myenv

# Prioritize Conda's GCC runtime
export LD_LIBRARY_PATH=/gpfs/helios/home/etais/hpc_joseluis/.conda/envs/myenv/lib:$LD_LIBRARY_PATH

# Execute the script
#mpirun -np ${SLURM_NTASKS} python script.py
mpirun --mca btl ^openib --mca opal_warn_on_missing_libcuda 0 -np ${SLURM_NTASKS} /gpfs/helios/home/etais/hpc_joseluis/.conda/envs/myenv/bin/python script.py
