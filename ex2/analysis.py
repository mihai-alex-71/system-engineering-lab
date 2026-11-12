"""Fill Lab4_defect_data.xlsx with formulas and draw the defect-age histogram."""
import openpyxl
from openpyxl.chart import BarChart, Reference
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SRC, OUT = "Lab4_defect_data.xlsx", "Lab4_defect_data_completed.xlsx"
wb = openpyxl.load_workbook(SRC)

# Sheet 1: defect age + histogram bins
ws = wb["Defect age"]
ages = []
for r in range(2, 29):
    ws[f"D{r}"] = f"=C{r}-B{r}"
    ages.append((ws[f"C{r}"].value - ws[f"B{r}"].value).days)

bins = [(1, 10), (11, 20), (21, 30), (31, 40)]
ws["F1"], ws["G1"], ws["H1"] = "Bin (days)", "Upper limit", "Count"
for i, (lo, hi) in enumerate(bins, start=2):
    ws[f"F{i}"], ws[f"G{i}"] = f"{lo}-{hi}", hi
    ws[f"H{i}"] = f'=COUNTIFS($D$2:$D$28,">={lo}",$D$2:$D$28,"<={hi}")'
ws["F7"], ws["H7"] = "Total", "=SUM(H2:H5)"
ws["F9"], ws["G9"] = "Mean", "=AVERAGE(D2:D28)"
ws["F10"], ws["G10"] = "Median", "=MEDIAN(D2:D28)"
ws["F11"], ws["G11"] = "Min", "=MIN(D2:D28)"
ws["F12"], ws["G12"] = "Max", "=MAX(D2:D28)"
for c in "FGH":
    ws.column_dimensions[c].width = 14

chart = BarChart()
chart.title, chart.y_axis.title, chart.x_axis.title = "Defect age histogram", "Number of defects", "Age (days)"
chart.add_data(Reference(ws, min_col=8, min_row=1, max_row=5), titles_from_data=True)
chart.set_categories(Reference(ws, min_col=6, min_row=2, max_row=5))
chart.gapWidth, chart.legend = 5, None
ws.add_chart(chart, "J2")

# Sheet 2: defect density (exercise 3)
ws2 = wb["Defect density"]
for r in range(2, 12):
    ws2[f"D{r}"] = f"=B{r}/C{r}"
    ws2[f"D{r}"].number_format = "0.00"

# Sheet 3: Fibonacci results (exercise 1)
ws3 = wb["Fibonacci results"]
correct = {4: ("0", "No"), 5: ("1", "Yes"), 6: ("610", "Yes"), 7: ("28657", "Yes"),
           8: ("12586269025", "No"), 9: ("135301852344706746049", "No"),
           10: ("invalid (n < 0)", "No"), 11: ("invalid (not an integer)", "No"),
           12: ("invalid (not a number)", "No"), 13: ("invalid (not a number)", "No"),
           14: ("invalid (empty)", "No")}
for r, (val, ok) in correct.items():
    ws3[f"C{r}"], ws3[f"D{r}"] = val, ok
ws3.column_dimensions["C"].width = 26
wb.save(OUT)

# PNG histogram
counts = [sum(lo <= a <= hi for a in ages) for lo, hi in bins]
fig, ax = plt.subplots(figsize=(8, 5))
b = ax.bar([f"{lo}-{hi}" for lo, hi in bins], counts, width=0.95, color="#1f4e5f", edgecolor="white")
for bar, c in zip(b, counts):
    ax.text(bar.get_x() + bar.get_width() / 2, c + 0.2, str(c), ha="center")
ax.set_title(f"Defect age histogram (n = {len(ages)}, bin width 10 days)")
ax.set_xlabel("Age (days) = Resolved - Submitted")
ax.set_ylabel("Number of defects")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("defect_age_histogram.png", dpi=150)
print(ages, counts, sum(ages) / len(ages))
