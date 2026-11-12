import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

EFFECT = "Fibonacci calculator\ngives wrong / confusing\nresults"
TOP = [
    ("Code / algorithm", ["32-bit signed integers -> overflow from n = 47",
                          "Wrong base case: F(0) returns 1",
                          "parseInt() used without checks"]),
    ("Input validation", ["Negative n accepted, returns 0",
                          "2.5 silently truncated to 2",
                          "'12abc' accepted as 12"]),
    ("User interface", ["No error messages",
                        "Shows 'F(NaN) = 0' as a result",
                        "No hint about the valid range of n"]),
]
BOTTOM = [
    ("Requirements", ["F(0) convention not specified",
                      "Valid domain / max n not defined",
                      "Invalid-input behaviour not defined"]),
    ("Testing", ["No tests for edge cases (0, <0, large n)",
                 "Results not compared with reference values",
                 "No code review"]),
    ("People", ["Developer unaware of JS number limits",
                "User expects exact big results",
                "User expects a clear error, not 0"]),
]

fig, ax = plt.subplots(figsize=(18, 9))
ax.set_xlim(0, 18); ax.set_ylim(0, 9); ax.axis("off")
spine_y = 4.5
ax.annotate("", xy=(14.6, spine_y), xytext=(0.4, spine_y),
            arrowprops=dict(arrowstyle="-|>", lw=3, color="#16353d"))
ax.text(16.2, spine_y, EFFECT, ha="center", va="center", fontsize=13, weight="bold",
        bbox=dict(boxstyle="round,pad=0.6", fc="#f2a541", ec="#16353d"))

def bone(x_join, cat, causes, up):
    sign = 1 if up else -1
    x_top, y_top = x_join - 1.9, spine_y + sign * 3.6
    ax.plot([x_top, x_join], [y_top, spine_y], color="#55707a", lw=2)
    ax.text(x_top, y_top + sign * 0.35, cat, ha="center", va="center", fontsize=13, weight="bold",
            color="#16353d")
    for i, c in enumerate(causes):
        t = (i + 1) / (len(causes) + 1)
        x = x_top + (x_join - x_top) * t
        y = y_top + (spine_y - y_top) * t
        ax.plot([x, x + 0.35], [y, y], color="#55707a", lw=1)
        ax.text(x + 0.4, y, c, va="center", fontsize=9.5)

for x, (cat, causes) in zip([4.2, 8.6, 13.0], TOP):
    bone(x, cat, causes, True)
for x, (cat, causes) in zip([4.2, 8.6, 13.0], BOTTOM):
    bone(x, cat, causes, False)

ax.set_title("Ishikawa (fishbone) diagram - Fibonacci calculator", fontsize=16, weight="bold")
plt.tight_layout()
plt.savefig("fishbone.png", dpi=150)
