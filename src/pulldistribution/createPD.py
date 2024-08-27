import os
import ROOT
import numpy as np

# Create a pull distribution for a single module (single sensitive)
def createModuleDistribution(vl, mDict, path):

    for m in mDict:
        if not os.path.isdir(os.path.join(path, "vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules")):
            os.makedirs(os.path.join(path, "vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules"))

        c1 = ROOT.TCanvas( "sen" + str(m), 'Pull Distribution vol' + str(vl[0]) + " lay" + str(vl[1]) + " sen" + str(m), 200, 10, 700, 500 )

        h1 = ROOT.TH1D("Overview", 'Pull Distribution vol' + str(vl[0]) + " lay" + str(vl[1]) + " sen" + str(m), 10, np.min(m), np.max(m))
        for xeach in mDict[m]:
            h1.Fill(xeach)
        h1.Fit('gausn', 'Q')
        h1.Draw()

        c1.SetFillColor( 18 )
        c1.SetGrid()
        c1.SaveAs(os.path.join(path, "vol_" + str(vl[0]) + "_layer_" + str(vl[1])  + "_modules/_sen"  + str(m) + ".png"))

# Create pull distribution for a whole layer
def createLayerDistribution(vl, mDict, path):
    
    total = np.array([])
    for m in mDict:
        total = np.append(total, mDict[m])
    
    total = total[~np.isnan(total)]

    if total.size != 0:
        c2 = ROOT.TCanvas( "c" + str(vl[0]) + str(vl[1]), 'hist', 200, 10, 700, 500 )

        h2 = ROOT.TH1D("Overview", 'Total Pull Distribution vol' + str(vl[0]) + '_layer' + str(vl[1]), 10, np.min(total), np.max(total))
        for xeach in total:
            h2.Fill(xeach)
        h2.Fit('gausn', 'Q')
        h2.Draw()

        c2.SetFillColor( 18 )
        c2.SetGrid()
        c2.SaveAs(os.path.join(path, "vol_" + str(vl[0]) + "_layer_" + str(vl[1]) + "_modules", "pull.png"))

# Create pull distributions
def createPullDistributions(rms, path):
    img_path = os.path.join(path, "css", "img")
    for vl in rms:
        createModuleDistribution(vl, rms[vl], img_path)
        createLayerDistribution(vl, rms[vl], img_path)