import numpy as np
from sklearn.metrics import confusion_matrix
import pandas as pd

def PPV(sens, spec, prev) :
    numerator = sens * prev
    denomenator = sens * prev + (1-spec) * (1-prev)
    
    return numerator/denomenator

def NPV(sens, spec, prev) :
    numerator = spec * (1-prev)
    denomenator = spec * (1-prev) + (1-sens) * prev
    
    return numerator/denomenator

def make_sens_spec_table(y_test_bin, y_test_pred, sensitivity_targets, which, strap=[None]) :
    # we must choose the decision threshold such that we get the above sensitivity
    
    if strap[0] == None :
        strap = range(len(y_test_bin))

    thresholds = []
    thr_lspace = np.linspace(0,1,1001)

    for targ in sensitivity_targets :
        sens_list_temp = []
        for thr in thr_lspace :
            tn, fp, fn, tp = confusion_matrix(y_test_bin[strap,which],y_test_pred[strap,which]>thr).ravel()
            sens = tp/(tp+fn)
            sens_list_temp.append(sens)

        best_thresh_loc = np.argmin(np.abs([s-targ for s in sens_list_temp]))

        thresholds.append(thr_lspace[best_thresh_loc])

    # now we know the thresholds! Let's compute specificity
    #print(thresholds)

    specificities = []

    for thr in thresholds :
        tn, fp, fn, tp = confusion_matrix(y_test_bin[strap,which],y_test_pred[strap,which]>thr).ravel()
        specificities.append(tn/(tn+fp))

    prevalences = [.05, .1, .2, .3, .4, .5]

    ppv_values={}
    npv_values={}

    sensitivity_targets = np.array(sensitivity_targets)
    specificities = np.array(specificities)
    for prev in prevalences :
        ppv_values[str(int(prev*100))] = PPV((sensitivity_targets), (specificities), prev)
        npv_values[str(int(prev*100))] = NPV((sensitivity_targets), (specificities), prev)

    res_df = pd.DataFrame(columns=['Sensitivity','Specificity'], 
                          data=np.array([sensitivity_targets, specificities]).T)

    for k in ppv_values :
        name = "PPV at prevalence of %s percent" % k
        res_df.insert(len(res_df.columns), name, ppv_values[k])

    for k in npv_values :
        name = "NPV at prevalence of %s percent" % k
        res_df.insert(len(res_df.columns), name, npv_values[k])
        
    res_df.insert(len(res_df.columns), 'cutoffs', thresholds)
        
    return res_df