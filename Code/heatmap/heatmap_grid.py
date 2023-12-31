import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# initializing 6x10 grid with travel time values from dataset
o = open("HeatMapModified.csv", "r")
data = o.read().split('\n')
data = data[1:-1]
grid = [[0.0 for _ in range(10)] for _ in range(6)]
for row in data:
    name, time, pos, x, y = row.split(",")
    grid[(int)(x)][(int)(y)] = float(time)

# placing above grid into a df and outputting heatmap based off the df
df = pd.DataFrame(np.array(grid), columns=["0","1","2","3","4","5","6","7","8","9"])
sns.heatmap(df)
plt.xlabel('Grid Column')
plt.ylabel('Grid Row')
plt.title('Durham Travel Time Heatmap')
plt.show()
