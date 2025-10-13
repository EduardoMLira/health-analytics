# src/viz.py
import matplotlib.pyplot as plt
import numpy as np

def scatter_xy(df, x, y, title=None, alpha=0.6, out_path=None):
    plt.figure()
    plt.scatter(df[x], df[y], alpha=alpha)
    plt.xlabel(x)
    plt.ylabel(y)
    if title:
        plt.title(title)
    plt.tight_layout()
    if out_path:
        plt.savefig(out_path, dpi=140)
        plt.close()
    else:
        plt.show()

def corr_heatmap(df, cols=None, title='Matriz de Correlação', out_path=None):
    if cols is None:
        cols = df.select_dtypes('number').columns
    corr = df[cols].corr()
    plt.figure()
    im = plt.imshow(corr, vmin=-1, vmax=1)
    plt.colorbar(im, fraction=0.046, pad=0.04)
    plt.xticks(range(len(cols)), cols, rotation=90)
    plt.yticks(range(len(cols)), cols)
    plt.title(title)
    plt.tight_layout()
    if out_path:
        plt.savefig(out_path, dpi=140)
        plt.close()
    else:
        plt.show()
