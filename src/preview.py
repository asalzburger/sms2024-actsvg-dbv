import ROOT
import numpy as np

import surfacedictionaries
import actHTMLCSS
import coloriser
import pulldistribution

from surfacedictionaries.createSD import createSurfaceDict
from actHTMLCSS.actHTMLCSS import createCSS, createHTML, createDirs
from coloriser.counting import hitsToRGB, holesToRGB, outliersToRGB
from coloriser.rms import rmsShiftToRGB, rmsWidthToRGB
from pulldistribution.createPD import createPullDistributions

ROOT.gErrorIgnoreLevel = ROOT.kFatal

# 
# Run in html_output directory with: python ../src/preview.py

# Path to .root file
PATH_to_ROOT = "../data/trackstates_fitter.root"

# Load root file as dataframe
df = ROOT.RDataFrame("trackstates", PATH_to_ROOT)

# Load columns as python dict {key = column name : value}
data = df.AsNumpy(["volume_id", "layer_id", "module_id", "pull_eLOC0_smt", "stateType"])

# For easy access
VID = data["volume_id"]
LID = data["layer_id"]
MID = data["module_id"]
#chi = data["chi2"]   
sType = data["stateType"]
pullLoc = data["pull_eLOC0_smt"]

dirs = ["hits", "holes", "outliers", "img", "rms_shift", "rms_width"]

createDirs(dirs)

# Count hits
print(">> flling hits data")

hits = createSurfaceDict(VID, LID, MID)
for i in range(VID.size):
    for j in range(VID[i].size()):
        hits[(VID[i][j], LID[i][j])][MID[i][j]] += 1

# Count holes
print(">> filling holes data")

holes = createSurfaceDict(VID, LID, MID)
for i in range(VID.size):
    for j in range(VID[i].size()):
        if (sType[i][j] == 2):
            holes[(VID[i][j], LID[i][j])][MID[i][j]] += 1

# Count outliers
print(">> filling outliers data")

outliers = createSurfaceDict(VID, LID, MID)
for i in range(VID.size):
    for j in range(VID[i].size()):
        if (sType[i][j] == 1):
            outliers[(VID[i][j], LID[i][j])][MID[i][j]] += 1

# Create arrays to plot pull distribution per surface
print(">> filling rms data")
rms = createSurfaceDict(VID, LID, MID, True)
for i in range(VID.size):
    c = 0
    for j in range(VID[i].size()):
        if (sType[i][j] == 0 and c < pullLoc[i].size()):
            tempVL = (VID[i][j], LID[i][j])
            rms[tempVL][MID[i][j]] = np.append(rms[tempVL][MID[i][j]], pullLoc[i][c])
            c += 1
        if (c == pullLoc[i].size()):
            break


# Create css-files to display hits per surface
print(">> creating css-hits")
for vl in hits:
    colors = hitsToRGB(hits[vl])
    css_filename = "css/hits/vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules"
    createCSS(css_filename, colors, vl[0], vl[1])



# Create css-files to display number of holes per surface
print(">> creating css-holes")
# Color will be relative to w.r.t. the highest number of holes on any surface 
mh = -1
for i in holes:
    for j in holes[i]:  
        if (holes[i][j] > mh):
            mh = holes[i][j]

for vl in holes:
    colors = holesToRGB(holes[vl], mh)
    css_filename = "css/holes/vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules"
    createCSS(css_filename, colors, vl[0], vl[1])


# Create css-files to display the number of outliers per surface
print(">> creating css-outliers")

# Color will be relative to w.r.t. the highest number of outliers on any surface
mo = -1
for i in outliers:
    for j in outliers[i]:
        if (outliers[i][j] > mo):
            mo = outliers[i][j]

for vl in outliers:
    colors = outliersToRGB(outliers[vl], mo)
    css_filename = "css/outliers/vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules"
    createCSS(css_filename, colors, vl[0], vl[1])


# Create css-files displaying the shift from zero in the mean of the pull distribution
print(">> creating css-rmsShift")
for vl in rms:
    colors = rmsShiftToRGB(rms[vl])
    css_filename = "css/rms_shift/vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules"
    createCSS(css_filename, colors, vl[0], vl[1])

# Create css-files displaying the change in standard deviation of the pull distribution
print(">> creating css-rmsWidth")
for vl in rms:
    colors = rmsWidthToRGB(rms[vl])
    css_filename = "css/rms_width/vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules"
    createCSS(css_filename, colors, vl[0], vl[1])

# Create Pull Distributions pngs for each layer and every module separately
print(">> Creating  Pull Distributions")
createPullDistributions(rms)

# Create the HTML-file
print(">> Creating html")
createHTML(VID, LID)


       