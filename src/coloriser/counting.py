# Converts number of hits to an rgb-value relative up to 100 hits  
def hitsToRGB(mDict):
    returnDict = {}
    for m in mDict:
        col = mDict[m] / 100
        if col > 1:
            col = 1
        tRGB = (int(255*col), int(255*(1-col)), 0)
        returnDict[m] = tRGB
    return returnDict

# Converts number of holes to an rgb-value relative up to maxHoles
def holesToRGB(mDict, maxHoles):
    returnDict = {}
    for m in mDict:
        if maxHoles:
            col = mDict[m] / maxHoles
        else:
            col = 0
        tRGB = (int(255*col), int(255*(1-col)), 0)
        returnDict[m] = tRGB
    return returnDict

# Converts number of holes to an rgb-value relative up to maxOutliers
def outliersToRGB(mDict, maxOutliers):
    returnDict = {}
    for m in mDict:
        if (maxOutliers != 0):
            col = mDict[m] / maxOutliers
        if (maxOutliers <= 0):
            col = 0
        
        tRGB = (int(255*col), int(255*(1-col)), 0)
        returnDict[m] = tRGB
    return returnDict