import numpy as np


# get indices of disqualified ECGs
def filter_ecgs(ecgs_array) :
    exclude_list = list(set(np.where(np.abs(ecgs_array)>5000)[0]))
    
    return exclude_list

# normalize a single ecg
def normalize_ecg(ecg_array) :
    ecg_array -= np.mean(ecg_array)
    ecg_array /= np.std(ecg_array)
    
    return ecg_array