# HemoNet

## What is it?
HemoNet takes in the 12-lead, 10 second ECG, sampled at 500 Hz. It generates the following inferences of hemodynamic values:
- p(PCWP > 15 mmHg)
- p(mPAP > 20 mmHg)
- p(PVR > 3 Wood's Units)
- p(CO > 4 L/min)

We pre-train on a much larger cohort of ECGs, then fine-tune the model for the downstream task of interest: identifying abnormal hemodynamic values.

## How do I use it?
We include an example ECG from PhysioNet<sup>[1](#ptb),[2](#physionet)</sup> in the [example notebook](Examples/model_loading_demo.ipynb). The input leads should be in the following order: I, II, III, aVR, aVL, aVF, V1-V6. Each ECG is normalized by its mean and variance across all samples. An input array should be of shape Nx5000x12 for N ECGs.

The output will be of shape Nx4, where the columns ordered mPAP, PCWP, PVR, CO.


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
