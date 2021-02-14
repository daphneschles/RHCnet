# HemoNet

## What is it?
HemoNet takes in the 12-lead, 10 second ECG, sampled at 500 Hz. It generates the following inferences of hemodynamic values:
- p(PCWP > 15 mmHg)
- p(mPAP > 20 mmHg)
- p(PVR > 3 Wood's Units)
- p(CO > 4 L/min)


## Dependencies
- numpy
- pandas
- matplotlib
- tensorflow 2.0 or greater
- tensorflow-addons

See the [package file](pkg_list.txt) for an exhaustive list.
