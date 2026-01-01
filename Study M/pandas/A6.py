import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
print(df.head())

x = df['X_column'].values  
y = df['Y_column'].values  
mean_x = np.mean(x)
mean_y = np.mean(y)


plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Data Points')
plt.axvline(mean_x, color='red', linestyle='--', label='Mean of X_column')
plt.axhline(mean_y, color='green', linestyle='--', label='Mean of Y_column')
plt.xlabel('X_column')
plt.ylabel('Y_column')
plt.title('Scatter Plot with Means')
plt.legend()
plt.grid(True)
plt.show()
