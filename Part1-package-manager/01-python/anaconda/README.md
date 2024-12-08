### **README.md**

# Example: Using Conda with Python

This document provides a practical guide to using **Conda** with Python. We'll cover the basics of installing Python and Conda on Ubuntu, using Conda to manage environments, and setting up Python projects with different versions.

---

## **1. Introduction**

**Conda** is an open-source package and environment management system that simplifies the installation of software and libraries while managing dependencies. It is especially useful for Python projects where different versions of Python or specific libraries are required.

This guide includes:
- Installing Python on Ubuntu.
- Installing Conda.
- Basic usage of Conda.
- Examples of creating and activating Conda environments with different Python versions.

---

## **2. Install Python on Ubuntu**

### Step 1: Update the system
Update the package list to ensure you have the latest information about available packages:
```bash
sudo apt update
```

### Step 2: Install Python
Install Python using the `apt` package manager:
```bash
sudo apt install python3 python3-pip -y
```

### Step 3: Verify installation
Check the installed Python version:
```bash
python3 --version
```

---

## **3. Install Conda**

### Option 1: Install Miniconda (Lightweight version of Conda)
1. Download the Miniconda installer script:
   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   ```

2. Run the installer:
   ```bash
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

3. Follow the installation prompts and restart your shell to activate Conda.

### Option 2: Install Anaconda (Includes Conda + Pre-installed Libraries)
1. Download the Anaconda installer:
   ```bash
   wget https://repo.anaconda.com/archive/Anaconda3-2023.11-Linux-x86_64.sh
   ```

2. Run the installer:
   ```bash
   bash Anaconda3-2023.11-Linux-x86_64.sh
   ```

3. Follow the prompts and restart your shell.

### Verify Conda Installation
After installation, verify that Conda is installed:
```bash
conda --version
```

---

## **4. Basic Usage of Conda**

### Check Installed Packages
```bash
conda list
```

### Update Conda
```bash
conda update conda
```

### Create a New Environment
Create an environment with Python 3.9:
```bash
conda create --name myenv python=3.9
```

### Activate an Environment
Activate the new environment:
```bash
conda activate myenv
```

### Deactivate the Current Environment
```bash
conda deactivate
```

### Remove an Environment
```bash
conda remove --name myenv --all
```

---

## **5. Simple Example: Activating Conda**

1. Create a new Conda environment:
   ```bash
   conda create --name simpleenv python=3.8
   ```

2. Activate the environment:
   ```bash
   conda activate simpleenv
   ```

3. Verify the Python version:
   ```bash
   python --version
   ```

4. Deactivate the environment:
   ```bash
   conda deactivate
   ```

---

## **6. Complex Example: Using Conda with Another Python Version**

### Step 1: Create an environment with Python 3.7
```bash
conda create --name complexenv python=3.7
```

### Step 2: Activate the environment
```bash
conda activate complexenv
```

### Step 3: Install Additional Packages
Install some libraries like NumPy and Pandas:
```bash
conda install numpy pandas
```

### Step 4: Run a Python script
Create a script `example.py`:
```python
# example.py
import numpy as np
import pandas as pd

print("NumPy Version:", np.__version__)
print("Pandas Version:", pd.__version__)
```

Run the script:
```bash
python example.py
```

### Step 5: Deactivate the environment
```bash
conda deactivate
```

---

## License

This project is licensed under the MIT License.

---
## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---

### **How to Use**
1. Copy and save this content as `README.md` in the root directory of your project.
2. Share it with your project repository or include it with your codebase.

Let me know if you'd like additional sections or details!