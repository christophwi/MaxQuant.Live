# Script to plot the log files of MaxQuant.Live Targeting 
## Set up the virtual environment
First create the virtual environment
```
python3 -m venv ./env
```
and install the needed packages by running 
```
pip install -r requirements.txt 
```
# Analyze log files 
The script PlotPeptides.py analyzes all files, which are given as argument in the command
```
./env/bin/python3 PlotPeptides.py 1001_20211214-0207.txt 1002_20211214-0818.txt ...
```
Only files whose name follows the pattern ID_DATE_TIME.txt are processed by the script. 
For every log file it generates three new files
- ID_DATE_TIME_peptides.png
- ID_DATE_TIME_peptides.pdf
- ID_DATE_TIME_peptides.TXT
that contain the information about the elution times and the dynamic correction.