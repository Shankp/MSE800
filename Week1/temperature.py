import numpy as np

def _ConvertTemperature_(tempList):
    convertedArray = []
    for temp in tempList:
        convertedArray.append( temp * 9/5 + 32)
    return convertedArray
    

if __name__ =="__main__":
    tempArray = [18.5, 19, 20, 25.0, 2, 30, 13.9]    
    print(f"average of the temperature,{np.average(tempArray): .2f}")
    print(f"max of the temperature,{np.max(tempArray): .2f}")   
    print(f"min of the temperature {np.min(tempArray): .2f}")
    print(f"converted temperature: {_ConvertTemperature_(tempArray)}")

    arr = np.array(tempArray)
    result = np.where(np.array(tempArray) > 20)
    print("Indices of temperature values above 20: ",result[0])
    print(f"values of temperature values above 20: {arr[result]}")
                      