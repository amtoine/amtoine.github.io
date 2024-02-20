import matplotlib.pyplot as plt
import sys
import os

data = list(map(int, sys.argv[1:]))

plt.plot(data)
plt.savefig(os.path.join(os.path.dirname(__file__), "scores.png"))
