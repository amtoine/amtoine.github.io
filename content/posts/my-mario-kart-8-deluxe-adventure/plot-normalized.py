import matplotlib.pyplot as plt
import sys
import os

values = list(map(float, sys.argv[1:]))

colors = {
    "axes.edgecolor": "orange",
    "xtick.color": "red",
    "ytick.color": "green",
    "figure.facecolor": "white",
}

with plt.rc_context(colors):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig.canvas.manager.full_screen_toggle()
    fig.patch.set_facecolor((31 / 255, 34 / 255, 42 / 255))
    ax.xaxis.label.set_color(colors["xtick.color"])
    ax.yaxis.label.set_color(colors["ytick.color"])
    ax.plot(values)

plt.grid(True)

plt.savefig(
    os.path.join(os.path.dirname(__file__), "normalized-scores.png"),
    dpi=500,
)
