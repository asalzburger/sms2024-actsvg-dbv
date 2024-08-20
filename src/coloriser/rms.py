import numpy as np

# Converts the change in standard deviation of the pull distribution to an rgb-value
def rmsWidthToRGB(mDict):
    returnDict = {}
    for m in mDict:
        if mDict[m].size != 0:
            col = np.sqrt(np.nanmean(mDict[m]**2))
        else:
            continue

        # If 1 < rms < 5 green to red, if rm < 1 blue to green
        if (col < 1):
            tRGB = (0, int(255*col), int(255*(1-col)))
        else:
            if (col > 5):
                tRGB = (255,0,0)
            else:
                col -= 1
                col = col / 4
                tRGB = (int(255*col), int(255*(1-col)), 0)
        returnDict[m] = tRGB
    return returnDict

# Converts the shift in mean of the pull distribution to an rgb-value
def rmsShiftToRGB(mDict):
    returnDict = {}
    for m in mDict:
        if mDict[m].size != 0:
            col = np.nanmean(mDict[m])
        else:
            continue

        if (col < 0):
            col = abs(col)
        if (col > 5):
            tRGB = (255,0,0)
        else:
            col = col / 5
            tRGB = (int(255*col), int(255*(1-col)), 0)
        returnDict[m] = tRGB
    return returnDict