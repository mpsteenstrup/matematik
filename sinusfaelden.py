import numpy as np
import matplotlib.pyplot as plt

# Givne værdier fra Opgave 6
A_deg = 30
c = 10
a = 7

# Omregn vinkel A til radianer for beregning
A_rad = np.radians(A_deg)

# Beregn sinus til vinkel C vha. sinusrelationen: sin(C) = (c * sin(A)) / a
sin_C = (c * np.sin(A_rad)) / a

# Find de to mulige vinkler for C (spids og stump)
C1_rad = np.arcsin(sin_C)
C2_rad = np.pi - C1_rad

# Beregn de tilsvarende vinkler for B
B1_rad = np.pi - A_rad - C1_rad
B2_rad = np.pi - A_rad - C2_rad

# Beregn længden af side b for de to tilfælde
b1 = (a * np.sin(B1_rad)) / np.sin(A_rad)
b2 = (a * np.sin(B2_rad)) / np.sin(A_rad)

# Definer koordinater for de faste punkter
A_coords = (0, 0)
B_coords = (c, 0)

# Beregn koordinater for de to mulige punkter C
C1_coords = (b1 * np.cos(A_rad), b1 * np.sin(A_rad))
C2_coords = (b2 * np.cos(A_rad), b2 * np.sin(A_rad))

# Plotting
plt.figure(figsize=(12, 8))

# 1. Tegn grundlinjen (side c)
plt.plot([A_coords[0], B_coords[0]], [A_coords[1], B_coords[1]], 'k-', lw=2, label=f'Side c = {c}')

# 2. Tegn linjen fra A med vinkel 30° (retning for side b)
plt.plot([A_coords[0], C1_coords[0] * 1.2], [A_coords[1], C1_coords[1] * 1.2], 'k--', alpha=0.5)

# 3. Tegn de to trekanter
# Trekant 1 (blå)
plt.plot([A_coords[0], B_coords[0], C1_coords[0], A_coords[0]], 
         [A_coords[1], B_coords[1], C1_coords[1], A_coords[1]], 
         'b-o', mfc='w', label=f'Trekant 1 (a={a}, b≈{b1:.1f}, ∠C₁≈{np.degrees(C1_rad):.1f}°)')

# Trekant 2 (rød)
plt.plot([A_coords[0], B_coords[0], C2_coords[0], A_coords[0]], 
         [B_coords[1], B_coords[1], C2_coords[1], A_coords[1]], 
         'r-o', mfc='w', label=f'Trekant 2 (a={a}, b≈{b2:.1f}, ∠C₂≈{np.degrees(C2_rad):.1f}°)')

# 4. Tegn halvcirklen, der viser den konstante afstand for a
# Vi danner en række vinkler fra A_rad op til pi-A_rad (for en halvcirkel "over" grundlinjen)
theta = np.linspace(A_rad, np.pi - A_rad, 100)
x_arc = B_coords[0] - a * np.cos(theta - A_rad) # Justering for at starte fra den rigtige vinkel
y_arc = a * np.sin(theta - A_rad)

# Bemærk: Den simple bue herover er svær at få til at passe perfekt. 
# En nemmere måde er at tegne en fuld cirkel og så begrænse visningen:
fuld_theta = np.linspace(0, 2*np.pi, 200)
x_cirkel = B_coords[0] + a * np.cos(fuld_theta)
y_cirkel = B_coords[1] + a * np.sin(fuld_theta)
plt.plot(x_cirkel, y_cirkel, 'g--', alpha=0.3, label='Mulige positioner for C (radius = a)')


# Indstillinger for grafen
plt.title(f'Visualisering af Sinusfælden: To mulige trekanter\n(Vinkel A={A_deg}°, side c={c}, side a={a})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.axis('equal') # Vigtigt for at cirklen ser cirkelrund ud og vinklerne er korrekte

# Tilføj labels til punkterne
plt.text(A_coords[0]-0.2, A_coords[1]-0.3, 'A', fontsize=12, fontweight='bold')
plt.text(B_coords[0]+0.1, B_coords[1]-0.3, 'B', fontsize=12, fontweight='bold')
plt.text(C1_coords[0], C1_coords[1]+0.2, 'C₁', fontsize=12, color='blue', fontweight='bold')
plt.text(C2_coords[0], C2_coords[1]+0.2, 'C₂', fontsize=12, color='red', fontweight='bold')

# Marker vinkel A
plt.text(1, 0.3, f'{A_deg}°', fontsize=10)

plt.show()