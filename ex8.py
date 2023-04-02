import geopandas as gpd
import matplotlib.pyplot as plt

filepath = "Data/TM_WORLD_BORDERS-0.3.shp"  # Завантаження даних
data = gpd.read_file(filepath)

fig, ax = plt.subplots(figsize=(12, 8))  # Створення карти
data.plot(ax=ax, color='white', edgecolor='black')
ax.set_title('World Map')
plt.show()
