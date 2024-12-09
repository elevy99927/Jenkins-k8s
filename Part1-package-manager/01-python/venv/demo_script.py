# demo_script.py

import matplotlib.pyplot as plt
import pandas as pd

# Create a simple plot
data = {"A": [1, 2, 3], "B": [4, 5, 6]}
df = pd.DataFrame(data)

df.plot(kind='bar', x='A', y='B', title="Demo Plot")
plt.show()
