import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 6))

# Wymiary działki (przykładowe): szerokość = 24 m, głębokość = 80 m
plot_width = 24
plot_depth = 80

# Rysujemy obrys działki
plot_rect = patches.Rectangle((0, 0), plot_width, plot_depth, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(plot_rect)

# Oznaczenie drogi (górna krawędź działki)
ax.text(plot_width/2, plot_depth + 2, "Droga", ha='center', va='bottom', fontsize=12)

# Pozycja garażu przy wjeździe: przyjmujemy margines 3 m od lewej i od drogi
garage_width = 6.0  # m (równolegle do drogi)
garage_depth = 5.8  # m (wgłąb działki)
garage_left = 3     # m od lewej granicy
garage_top = plot_depth - 3  # 3 m od górnej granicy (drogi)
garage_bottom = garage_top - garage_depth

# Rysujemy garaż
garage_rect = patches.Rectangle((garage_left, garage_bottom), garage_width, garage_depth, 
                                 linewidth=2, edgecolor='blue', facecolor='lightblue', label="Garaż")
ax.add_patch(garage_rect)
ax.text(garage_left + garage_width/2, garage_bottom + garage_depth/2, "Garaż 6x5,8 m", 
        ha='center', va='center', fontsize=10, color='blue')

# Ustawienia osi
ax.set_xlim(-5, plot_width+5)
ax.set_ylim(-5, plot_depth+10)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Plan zagospodarowania działki (przykład poglądowy)")
plt.tight_layout()
plt.savefig("/mnt/data/plan_zagospodarowania_dzialki_przykladowy.png")
plt.show()
