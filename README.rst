pybatdata
=========

To run the GUI: ``python analyseGUI.py``
To run from a script: ``python analyse.py``

Modify these scripts to suit your analysis. Example data has been added to test the code.


Note than a folder **pycache** will be created when you run the app.
However, this folder would not be tracked with the version control
system.


Requirements
------------

The code runs in Python 3 and it requires the following libraries that
can be install using ``pip``: numpy, pathlib, preparenovonix.

Contributing
------------

If you have new analysis code add it as a function within the pybatdata/plot_cycling.py or pybatdata/plot_eis.py, depending if the type of analysis is for Cycling or EIS.

If you want to enhance the code to be able to deal with a new equipment or modify the default column names, update the file pybatdata/constants.py.


Acknowledgements
----------------

The first version of this code was created by Matheus Aparecido do Carmo
Alves, Alana Aragon Zulke and Caio Ferreira Bernardo, at Lancaster
University. For further contributions, see the history in the
corresponing GitHub.

