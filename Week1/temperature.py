import numpy as np
#Temperature data (in °C): [18.5, 19, 20, 25.0, 2, 30, 13.9]

def _averageGenerator_(tempList):
    average = np.average(tempList)
    return average

def _getMax_(tempList):
    max = np.max(tempList)
    return max

def _getMin_(tempList):
    min = np.min(tempList)
    return min

def _temperatureCast_(tempList):
    convertedArray = []
    for temp in tempList:
        convertedArray.append( temp * 9/5 + 32)
    print("Converted array",convertedArray)
    

if __name__ =="__main__":
    tempArray = [18.5, 19, 20, 25.0, 2, 30, 13.9]
    average =_averageGenerator_(tempArray)
    print(f"average of the temperature {average: .2f}")
    maxArray =_getMax_(tempArray)
    print(f"max of the temperature {maxArray: .2f}")
    minArray =_getMin_(tempArray)
    print(f"min of the temperature {minArray: .2f}")
    _temperatureCast_(tempArray)

    #arrange array
    arr = np.array(tempArray)

    # Find values greater than 10
    result = np.where(arr > 20)
    print("temperates above 20",result[0])
                      