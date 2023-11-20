import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# scanning csv data into df and outputting heatmap based off grid
o = open("HeatMapModified.csv", "r")
data = o.read().split('\n')
data = data[1:-1]
grid = [[0.0 for _ in range(10)] for _ in range(6)]
for row in data:
    name, time, pos, x, y = row.split(",")
    grid[(int)(x)][(int)(y)] = float(time)

df = pd.DataFrame(np.array(grid), columns=["0","1","2","3","4","5","6","7","8","9"])
sns.heatmap(df)
plt.xlabel('Grid Column')
plt.ylabel('Grid Row')
plt.title('Durham Travel Time Heatmap')
plt.show()
