import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter

import sys
import os

colors = {
    "axes.edgecolor": "orange",
    "xtick.color": "red",
    "ytick.color": "green",
    "figure.facecolor": "white",
}


if __name__ == "__main__":
    filename = sys.argv[1]

    data = list(map(int, sys.argv[2:]))

    with plt.rc_context(colors):
        fig, ax = plt.subplots()

        ax.set_xlabel("score delta")
        ax.set_ylabel("density")

        fig.canvas.manager.full_screen_toggle()
        fig.patch.set_facecolor((31 / 255, 34 / 255, 42 / 255))
        ax.xaxis.label.set_color(colors["xtick.color"])
        ax.yaxis.label.set_color(colors["ytick.color"])

        def update(frame: int):
            print(f"{frame} / {len(data)}\r", end="")
            c = Counter(data[:frame])
            return ax.bar(list(c.keys()), list(c.values()), color="blue")

        ani = animation.FuncAnimation(fig=fig, func=update, frames=len(data), interval=30)

    ani.save(
        os.path.join(os.path.dirname(__file__), filename),
    )
