import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = {"M1": (40, 20), "M2": (15, 30), "M3": (25, 5), "M4": (10, 10), "M5": (8, 20),
        "M6": (4, 20), "M7": (10, 30), "M8": (5, 5), "M9": (7, 10), "M10": (14, 20)}

rows = sorted(((m, d, loc, d / loc) for m, (d, loc) in data.items()), key=lambda r: r[3], reverse=True)

with open("defect_density.csv", "w") as f:
    f.write("Module,Defects,LOC,Defect density\n")
    for m, d, loc, dd in rows:
        f.write(f"{m},{d},{loc},{dd:.2f}\n")

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar([r[0] for r in rows], [r[3] for r in rows], color="#1f4e5f")
bars[0].set_color("#e8a33d")
for b, r in zip(bars, rows):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.05, f"{r[3]:.2f}", ha="center")
ax.set_title("Defect density per module (sorted, highest to lowest)")
ax.set_xlabel("Module")
ax.set_ylabel("Defects / LOC")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("defect_density_chart.png", dpi=150)
for r in rows: print(r)
