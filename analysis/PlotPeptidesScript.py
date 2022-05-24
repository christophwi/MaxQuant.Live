#  .\venv\Scripts\pyinstaller.exe --onefile .\PlotPeptidesScript.py

import pandas as pd
import sys
from scipy import *
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import os
import re


# %%

def density(x, y, res=100, s=3):
    xedges, yedges = np.linspace(x.min(), x.max(), res), np.linspace(y.min(), y.max(), res)
    hist, xedges, yedges = np.histogram2d(x, y, (xedges, yedges))
    xidx = np.clip(np.digitize(x, xedges), 0, hist.shape[0] - 1)
    yidx = np.clip(np.digitize(y, yedges), 0, hist.shape[1] - 1)
    hist = ndimage.gaussian_filter(hist, 3)
    c = hist[xidx, yidx]
    return c


# %%

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def parseLogFile(fName):
    fl = open(fName)
    data = [i.split()[3:] for i in fl.readlines() if i.find("PEPTIDE_FOUND_MS1") != -1]
    data = [["rt:", i[0]] + i[2:] for i in data]
    fl.close()

    keys, idz, values = [], [], []
    for c, s in enumerate(data[0]):
        if (s[-1] == ":"): keys.append(s.replace(":", ""))

    for s in data:
        v = []
        for c, i in enumerate(s):
            if (i[-1] == ":"): v.append(s[c + 1])
        if (len(v) == len(keys)):      values.append(v)

    values = [[float(v) if isfloat(v) else v for v in val] for val in values]

    peptides = pd.DataFrame(values, columns=keys)
    print(peptides.loc[0, :])
    peptideLengths = peptides.groupby('id')['rt'].max() - peptides.groupby('id')['rt'].min()

    peptides = peptides.loc[peptides.groupby('id')['intensity'].idxmax()]
    peptides['length'] = peptideLengths.values

    return peptides.sort_values('rt')


# %%

# plot
def plotPeptides(fp):
    m = fp['mz']
    me = fp['mz_correction']
    err = fp['mz_tol']
    off = fp['mz_deviation']

    t = fp['rt']
    t_diff = fp['rt_deviation']
    t_diff_apex = fp['ApexRtDiff']
    t_me = fp['rt_correction']
    t_err = fp['rt_tol']

    int_ratio = np.array(fp['int_ratio'])
    int_corr = fp['int_correction']
    lengths = fp['length']

    f = 1.0e6

    plt.suptitle("%i peptides found [%s]; median length [%5.2f]" % (len(t), fName, np.median(lengths)))

    plt.subplot(331)

    plt.fill_between(t, (me) / m * f - err, (me) / m * f + err, color="gray", alpha=0.5)

    x, y = t, off / m * f
    plt.title("Mass deviation, median=%5.2f" % (np.median(abs(y))))
    plt.scatter(x, y, c=density(x, y), marker=".", linewidth=0)
    # plot( t, off/m*f,"o",ms=3.0,color="black")
    plt.plot(t, me / m * f, "-", lw=1.5, color="black")
    # plot(t,t*0.0,".",lw=0.5,color="black")
    plt.xlim([min(t) - 1, max(t) + 1])
    plt.ylabel("ppm")
    plt.xlabel("min")

    plt.subplot(334)

    plt.fill_between(t, -err, err, color="gray", alpha=0.5)
    x, y = t, (off - me) / m * f
    plt.title("Corrected mass deviation, median=%5.2f" % (np.median(abs(y))))
    plt.scatter(x, y, c=density(x, y), marker=".", linewidth=0)
    # plot(t, (off-me)/m*f,"o",ms=3.0,color="black")
    plt.plot(t, (me - me) / m * f, "-", lw=1.5, color="black")
    plt.plot(t, t * 0.0, "-", lw=0.5, color="black")
    plt.xlim([min(t) - 1, max(t) + 1])
    plt.ylabel("ppm")
    plt.xlabel("min")

    plt.subplot(337)
    plt.hist(np.array((off - me) / m * f), 25, range=(-5, 5), color="gray")
    plt.xlabel("ppm")
    plt.xlim(-5, 5)

    plt.subplot(332)
    plt.title("Retention time deviation, median=%5.2f" % (np.median(abs(t_diff))))
    plt.fill_between(t, t_me - t_err, t_me + t_err, color="gray", alpha=0.5)
    plt.plot(t, t * 0.0, "-", lw=0.5, color="black")
    # plot(t, t_diff,"o",ms=3.0,color="black")

    plt.scatter(t, t_diff, c=density(t, t_diff), marker=".", linewidth=0)
    # scatter(t, t_diff_apex, marker="o",linewidth=0)
    plt.plot(t, t_me, "-", lw=1.5, color="black")

    plt.ylabel("min")
    plt.xlabel("min")
    # xlim([min(t)-1,max(t)+1])

    plt.subplot(335)
    plt.title("corrected retention time deviation, median=%5.2f" % (np.median(abs(t_diff - t_me))))
    plt.fill_between(t, -t_err, t_err, color="gray", alpha=0.5)
    plt.plot(t, t * 0.0, "-", lw=0.5, color="black")

    plt.scatter(t, t_diff - t_me, c=density(t, t_diff - t_me), marker=".", linewidth=0)

    # plot(t, t_diff-t_me,"o",ms=3.0,color="black")

    plt.plot(t, t_me - t_me, "-", lw=1.50, color="black")

    plt.ylabel("min")
    plt.xlabel("min")

    plt.subplot(338)
    plt.hist(np.array(t_diff), 50, color="lightgray", alpha=0.5)
    plt.hist(np.array(t_diff - t_me), 50, color="gray", alpha=0.5)
    plt.xlim(min(t_diff), max(t_diff))
    plt.xlabel("min")

    plt.subplot(333)
    int_ratio[int_ratio == 0] = 1.
    int_ratio = np.nan_to_num(int_ratio)
    x, y = t, int_ratio  # log(int_ratio)

    plt.title("intensity ratios, median=%5.2f" % (np.median(abs(y))))

    plt.scatter(x, y, c=density(x, y, res=50), marker=".", linewidth=0)
    plt.plot(t, 1.0 / int_corr, "-", lw=1.5, color="black")
    plt.ylabel("")
    plt.xlabel("min")
    plt.ylim(0, np.median(y) * 3)

    plt.subplot(336)

    x, y = t, int_ratio * int_corr  # log(int_ratio*int_corr)
    plt.title("corrected intensity ratios, median=%5.2f" % (np.median(abs(y))))
    plt.scatter(x, y, c=density(x, y), marker=".", linewidth=0)
    plt.plot(t, t * 0.0, "-", ms=3.0, color="gray")
    plt.ylabel("")
    plt.xlabel("min")
    plt.ylim(0, np.median(y) * 3)

    plt.subplot(339)
    plt.hist(np.array(int_ratio * int_corr), 25, range=(0, 5), color="gray")
    plt.xlim(0, 5)
    plt.xlabel("")


# %%

def plotLogFile(fName, overwrite=False, expectFilenamePattern=True):
    if not re.match(r'.+\.txt$', fName): return

    if expectFilenamePattern and not re.match(r'^\d{4}_\d{8}-\d{4}\.txt$', fName):
        return

    baseName = ".".join(fName.split(".")[:-1])

    if not overwrite and os.path.exists(baseName + "_peptides.pdf"):
        print("skipping " + baseName)
        return

    print("plotting " + baseName)

    # read log file
    fp = parseLogFile(baseName + ".txt")

    # plot peptides
    plt.clf()
    plt.figure(figsize=(20, 20))
    plotPeptides(fp)


    # save figures and peptide list
    # savefig(baseName + "_peptides.pdf")
    plt.savefig(baseName + "_peptides.png")
    fp.to_csv(baseName + "_peptides.TXT")


if len(sys.argv) == 1:
    print("No command line argument. Please give file path!")
else:
    for fName in sys.argv[1:]:
        plotLogFile(fName, overwrite=True, expectFilenamePattern=False)

input("Press Enter to continue...")
