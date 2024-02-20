import matplotlib.pyplot as plt
import sys
import os
import json

data = list(map(int, sys.argv[1].split("\n")))
days = json.loads(sys.argv[2])

MIN_SCORE = 1_000

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
    full_score_range = max(scores) - MIN_SCORE
    ax.scatter(indices, scores)
    for (t, x, y) in zip(dates, indices, scores):
        if x < last_index * 0.85:
            offset = (x + last_index * 0.1, y - full_score_range * 0.05)
        else:
            offset = (x - last_index * 0.4, y - full_score_range * 0.05)
        ax.annotate(
            t,
            (x, y),
            xytext=offset,
            arrowprops=dict(arrowstyle="fancy")
        )

    ax.plot(data)

plt.grid(True)

plt.xlim([0, None])
plt.ylim([MIN_SCORE, None])

plt.savefig(
    os.path.join(os.path.dirname(__file__), "scores.png"),
    dpi=500,
)
