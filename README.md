# ACTSVG DB Views

This is the main project space for the 2024 Summer Student Project `actsvg-dbgv`

Summer Student: Matthijs Ridder
CERN Supervisors: Andreas Salzburger, Shaun Roe

# How to run
## Python
To create svg-files from the data/odd-sensitives.json file use:

    python /path/to/load_sensitives.py

To generate the CSS files from data/trackstates-fitter.root use:

    python /path/to/preview.py

This wil also generate a HTML file and a JavaScript file.
These files are collected in an output directory. 

The result should then be visible when you setup a server from the output directory. For example by using:

    python -m http.server --directory /path/to/output_directory
