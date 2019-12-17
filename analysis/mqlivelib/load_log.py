import pandas as pd
import sys
from scipy import *
from scipy import ndimage
from numpy import *
from pylab import *

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
    peptideLengths = peptides.groupby('id')['rt'].max() - peptides.groupby('id')['rt'].min()

    peptides = peptides.loc[peptides.groupby('id')['intensity'].idxmax()]
    peptides['length'] = peptideLengths.values

    return peptides.sort_values('rt')