# HemoNet

## What is it?
HemoNet takes in the 12-lead, 10 second ECG, sampled at 500 Hz. It generates the following inferences of hemodynamic values:
- p(PCWP > 15 mmHg)
- p(mPAP > 20 mmHg)
- p(PVR > 3 Wood's Units)
- p(CO > 4 L/min)

## How do I use it?
We include an example ECG from PhysioNet<sup>[1](#ptb),[2](#physionet)</sup> in the [example notebook](Examples/model_loading_demo.ipynb).


## Dependencies
- numpy
- pandas
- matplotlib
- tensorflow 2.0 or greater
- tensorflow-addons

See the [package file](pkg_list.txt) for an exhaustive list.

## References
<a name="ptb">[1]</a> Bousseljot R, Kreiseler D, Schnabel, A. Nutzung der EKG-Signaldatenbank CARDIODAT der PTB über das Internet. Biomedizinische Technik, Band 40, Ergänzungsband 1 (1995) S 317

<a name="physionet">[2]</a> Goldberger AL, Amaral LAN, Glass L, Hausdorff JM, Ivanov PCh, Mark RG, Mietus JE, Moody GB, Peng C-K, Stanley HE. PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals. Circulation 101(23):e215-e220 [Circulation Electronic Pages; http://circ.ahajournals.org/content/101/23/e215.full]; 2000 (June 13).
