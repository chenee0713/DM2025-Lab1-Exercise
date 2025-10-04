import matplotlib.pyplot as plt
import pandas as pd
def bar_counts(counts: pd.Series, title: str, ylim_margin: int = 0, savepath: str | None = None):
    plt.figure()
    counts.plot(kind="bar")
    ymax = counts.max() + int(ylim_margin or counts.max() * 0.05)
    plt.ylim(0, ymax)
    plt.title(title); plt.ylabel("Count"); plt.tight_layout()
    if savepath: plt.savefig(savepath, dpi=150)
    plt.show()
