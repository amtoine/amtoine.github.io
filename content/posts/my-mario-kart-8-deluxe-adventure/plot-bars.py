import matplotlib.pyplot as plt
import sys
import os


if __name__ == "__main__":
    filename = sys.argv[1]

    data = list(map(int, sys.argv[2:]))

    nb_uniq_deltas = len(set(data))
    mean = sum(data) / len(data)
    if len(data) % 2 == 0:
        median = sorted(data)[len(data) / 2]
    else:
        median = sorted(data)[len(data) // 2]

    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig.canvas.manager.full_screen_toggle()

    density, _, _ = ax.hist(data, bins=nb_uniq_deltas, density=True)
    ax.vlines(mean, 0, max(density), color="red", label=f"mean: {mean:.2f}")
    ax.vlines(median, 0, max(density), color="orange", label=f"median: {median}")

    ax.set_xlabel("score delta")
    ax.set_ylabel("density")

    plt.title("score deltas over {} races".format(len(data)))
    plt.legend()

    plt.savefig(
        os.path.join(os.path.dirname(__file__), filename),
        dpi=500,
    )
