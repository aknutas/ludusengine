python
=====

This folder includes example scripts written in Python 3 to demonstrate how to use the Ludus Engine CN2 Classifier. 

The scripts are for *Windows only* (for example, relative file paths) but should be modifiable to be used in other operating systems. Tested examples for Linux OS's are *currently under work.* 

Requirements for use
----
The Orange Canvas Data Mining suite is required for these examples to work. You can donwload the latest version of Orange at: <https://orange.biolab.si/download/> 

A version of the Python programming language comes with the Orange installer. (At present, Python version 3.4 is used.)

List of files and instruction for use
----
This folder includes the following example scripts:

* _readAndClassifyFromExcelFile.py_ 

   This script loads the example (training) data from the algorithm folder, loads the classifier from it's binary distributable and classifies the data. 

* _createAndClassifyCustomDataTables.py_

   This script is an example on how to form data tables correctly within the script (and not from an xlsx or csv file).

* _poc_demo.py_

   A proof of concept "text adventure" to classify a single player by inputting features by hand (similarly to the previous example). 
