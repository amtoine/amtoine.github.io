import matplotlib.pyplot as plt
import sys
import os

data = list(map(int, sys.argv[1:]))

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
    ax.plot(data)

plt.grid(True)

plt.xlim([0, None])
plt.ylim([1_000, None])

plt.savefig(
    os.path.join(os.path.dirname(__file__), "scores.png"),
    dpi=500,
)
