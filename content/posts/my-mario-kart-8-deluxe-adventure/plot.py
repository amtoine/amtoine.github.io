import matplotlib.pyplot as plt
import sys
import os
import json

data = list(map(int, sys.argv[1].split("\n")))
days = json.loads(sys.argv[2])

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

    dates = [day["date"] for day in days]
    indices = [day["index"] for day in days]
    scores = [day["score"] for day in days]
    last_index = max(indices)
    ax.scatter(indices, scores)
    for (t, x, y) in zip(dates, indices, scores):
        if x < last_index * 0.9:
            offset = (x + 10, y - 100)
        else:
            offset = (x - 50, y - 100)
        ax.annotate(
            t,
            (x, y),
            xytext=offset,
            arrowprops=dict(arrowstyle="fancy")
        )

    ax.plot(data)

plt.grid(True)

plt.xlim([0, None])
plt.ylim([1_000, None])

plt.savefig(
    os.path.join(os.path.dirname(__file__), "scores.png"),
    dpi=500,
)
