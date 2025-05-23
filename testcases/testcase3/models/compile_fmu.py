# -*- coding: utf-8 -*-
"""
This module compiles the defined test case model into an FMU using the
overwrite block parser.

The following libraries must be on the MODELICAPATH:

- Modelica IBPSA

"""

import os
import sys

# Add the path to the parser module
root_repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, root_repo_path)

from parsing import parser


def compile_fmu():
    '''Compile the fmu.

    Returns
    -------
    fmupath : str
        Path to compiled fmu.

    '''

    # DEFINE MODEL
    # ------------
    mopath = 'TwoZones.mo';
    modelpath = 'TwoZones'
    # ------------

    # COMPILE FMU
    # -----------
    fmupath = parser.export_fmu(modelpath, [mopath])
    # -----------

    return fmupath

if __name__ == "__main__":
    fmupath = compile_fmu()
