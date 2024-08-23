import numpy as np

# Create a dictionary with the following structure:
#
# {(volume_id, layer_id) : {module_id : 0}} if emptyArray == False
# or
# {(volume_id, layer_id) : { module_id : np.array([])}} emptyArray == True
#
# Ensures every combination of volume, layer and module that has an entry in the data, 
# gets an entry in the dictionary represented by a tuple
def createSurfaceDict(v_id, l_id, m_id, emptyArray = False) :
    returnDict = {}
    for i in range(v_id.size):
        for j in range(v_id[i].size()):
            s = (v_id[i][j], l_id[i][j])
            if s not in returnDict: 
                returnDict[s] = {}
            
            if m_id[i][j] not in returnDict[s]:
                if emptyArray:
                    returnDict[s][m_id[i][j]] = np.array([])
                else:
                    returnDict[s][m_id[i][j]] = 0

    return returnDict