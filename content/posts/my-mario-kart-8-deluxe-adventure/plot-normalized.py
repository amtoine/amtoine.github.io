import matplotlib.pyplot as plt
import sys
import os

values = list(map(float, sys.argv[1:]))

plt.plot(values)
plt.savefig(
    os.path.join(os.path.dirname(__file__), "normalized-scores.png"),
)
