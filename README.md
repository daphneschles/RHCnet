# HemoNet

## What is it?
HemoNet takes in the 12-lead, 10 second ECG, sampled at 500 Hz. It generates the following inferences of hemodynamic values:

<img src="http://www.sciweavers.org/tex2img.php?eq=p%28PCWP%20%3E15%20%5Cmbox%7B%20mmHg%7D%29%20%5C%5C%0Ap%28mPAP%20%3E%2020%20%20%5Cmbox%7B%20mmHg%7D%29%20%5C%5C%0Ap%28PVR%20%3E%203%20%20%5Cmbox%7B%20Wood%27s%20Units%7D%29%20%5C%5C%0Ap%28CO%20%3E%204%20%20%5Cmbox%7B%20L%2Fmin%7D%29%20%5C%5C&bc=Transparent&fc=Black&im=jpg&fs=18&ff=arev&edit=0" align="center" border="0" alt="p(PCWP >15 \mbox{ mmHg}) \\p(mPAP > 20  \mbox{ mmHg}) \\p(PVR > 3  \mbox{ Wood's Units}) \\p(CO > 4  \mbox{ L/min}) \\" width="317" height="137" />


## Dependencies
- numpy
- pandas
- matplotlib
- tensorflow 2.0 or greater
- tensorflow-addons

See the [package file](pkg_list.txt) for an exhaustive list.
