import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 3, 5, 7, 11]}
df = pd.DataFrame(data)

# Plotting
df.plot(x='x', y='y', kind='scatter')
plt.show()
