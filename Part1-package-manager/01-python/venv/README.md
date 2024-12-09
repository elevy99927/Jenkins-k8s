# Python Virtual Environment (venv) Example

This guide demonstrates how to use Python's `venv` module to create and manage a virtual environment. We'll walk through the following steps:
1. Run a Python script without dependencies (failure expected).
2. Install and set up a virtual environment using `venv`.
3. Activate the virtual environment.
4. Install dependencies using `requirements.txt`.
5. Successfully run the Python script.
6. Deactivate the virtual environment and observe dependency isolation.

---

## **Steps**

### Step 1: Prepare a Python Script
Create a Python script named `demo_script.py`:
```python
# demo_script.py

import matplotlib.pyplot as plt
import pandas as pd

# Create a simple plot
data = {"A": [1, 2, 3], "B": [4, 5, 6]}
df = pd.DataFrame(data)

df.plot(kind='bar', x='A', y='B', title="Demo Plot")
plt.show()
```

Try running the script:
```bash
python3 demo_script.py
```

Expected output:
```plaintext
ModuleNotFoundError: No module named 'matplotlib'
```

---

### Step 2: Install `python3-venv` (if not already installed)
Install the `venv` module, which is required to create virtual environments:
```bash
sudo apt update
sudo apt install python3-venv -y
```

---

### Step 3: Create and Activate a Virtual Environment
1. Create a virtual environment named `venv`:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Verify the Python version in the virtual environment:
   ```bash
   python -V
   ```

---

### Step 4: Install Dependencies
Once the virtual environment is active, install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### Step 5: Run the Script in the Virtual Environment
Run the Python script again:
```bash
python demo_script.py
```

Expected output:
- A bar chart is displayed using matplotlib.

---

### Step 6: Deactivate the Virtual Environment
Deactivate the virtual environment:
```bash
deactivate
```

---

### Step 7: Verify Isolation
Run the script again **outside** the virtual environment:
```bash
python3 demo_script.py
```

Expected output:
```plaintext
ModuleNotFoundError: No module named 'matplotlib'
```

---

## **Requirements**

The `requirements.txt` file includes the following dependencies:
```plaintext
contourpy==1.0.6
cycler==0.11.0
fonttools==4.38.0
kiwisolver==1.4.4
matplotlib==3.6.2
numpy==1.23.5
pandas==1.5.1
pillow==9.3.0
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2022.6
scipy==1.9.3
seaborn==0.10.1
six==1.16.0
```

---

## **Summary**
- Virtual environments allow you to manage dependencies in an isolated manner.
- Installing dependencies inside a virtual environment prevents conflicts with system-wide packages.
- Deactivating the environment ensures that global dependencies are not affected.

For further reading, check Python's official [venv documentation](https://docs.python.org/3/library/venv.html).

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