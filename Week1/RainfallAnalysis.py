import numpy as np

def calculate_rainfall_statistics(array):    
    print(f"Rainfall values: {array}")
    print(f"Total rainfall : {np.sum(array): .2f}")
    print(f"Average rainfall : {np.mean(array): .2f}")
    zeroRainfall = np.where(array == 0.0)
    print(f"Number of days with zero rainfall : {len(zeroRainfall[0])}")
    rainfallFiltered = np.where(array > 5)
    print(f"Number of days with zero rainfall : {rainfallFiltered[0]}")
    percentile = np.percentile(array,75)
    print(f"75th percentile of rainfall : {percentile: .2f}")

if __name__ == "__main__":
    array = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    calculate_rainfall_statistics(array)
