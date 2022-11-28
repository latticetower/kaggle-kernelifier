Work in progress, tested manually with python 3.7.

This installs script named "convert2ipynb.py", which converts scripts from local folder both with the code from local dependencies to single .ipynb notebook.

It is supposed to produce valid .ipynb files from the source code, which can be runnable via Kaggle Notebooks, Google Colab, etc.

The script is based on the one I've developed for [the ARC Challenge](https://github.com/latticetower/kaggle-arc).


# Usage

Let's suppose that inside of some folder <folder> we have the following:

```
folder_a/
folder_b/
...
script.py
```

In our script.py we have imports like
```
from folder_a.script1 import foo
import folder_b
...
```
Also we have regular imports
```
import numpy as np
import pandas as pd
from pathlib import Path
import torch
```

To collect all this to one jupyter notebook, we might want to do the following:
- keep the imports related to the installed packages, remove duplicate imports, place them before they are first needed;
- remove duplicated imports for the local imports, instead of "place them before first use", add the code of the corresponding module;
- also, we might take into account that local functions in folder might have the dependencies theirselves, so we have a dependency tree!

Basically, the script does all this and collects the output to single jupyter notebook file. 


# Installation

```
git clone https://github.com/latticetower/kaggle-kernelifier.git
cd kaggle-kernelifier
pip install -e .
```

# Limitations


