"""Plot benchmark results from results.csv."""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rows = list(csv.DictReader(open("results.csv")))
fig, axes = plt.subplots(1, 3, figsize=(10, 3.4), sharey=True)
styles = {"Merge Sort": ("#1f4e79", "o"), "Quick Sort": ("#b03a2e", "s"),
          "Randomized Quick Sort": ("#7f7f7f", "^")}
titles = {"sorted": "Sorted input", "reverse": "Reverse sorted input", "random": "Random input"}
for ax, kind in zip(axes, ["sorted", "reverse", "random"]):
    for name, (color, marker) in styles.items():
        pts = [(int(r["n"]), float(r["time_ms"])) for r in rows
               if r["algorithm"] == name and r["dataset"] == kind]
        ax.plot([p[0] for p in pts], [p[1] for p in pts], marker=marker,
                color=color, label=name, linewidth=1.6, markersize=5)
    ax.set_title(titles[kind], fontsize=11)
    ax.set_xscale("log", base=2)
    ax.set_yscale("log")
    ax.set_xticks([500, 1000, 2000, 4000, 8000])
    ax.set_xticklabels(["500", "1k", "2k", "4k", "8k"])
    ax.set_xlabel("Input size (n)")
    ax.grid(True, which="major", alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel("Median time (ms, log scale)")
axes[0].legend(fontsize=8, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig("runtime_chart.png", dpi=200)
