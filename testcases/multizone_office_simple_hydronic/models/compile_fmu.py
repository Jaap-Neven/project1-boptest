# -*- coding: utf-8 -*-
"""
This module compiles the defined test case model into an FMU using the
BOPTEST parser.

The tool cli argument is the FMU compilation tool.  "OCT" or "dymola" or "openmodelica" supported.
i.e. python compile_fmu openmodelica

The following libraries with correct versions/commits must be on the MODELICAPATH:

- Buildings
- IDEAS

"""

from parsing import parser
import sys

def compile_fmu():
    '''Compile the fmu.

    Returns
    -------
    fmupath : str
        Path to compiled fmu.

    '''

    # DEFINE MODEL
    # ------------
    mopath = 'BuildingEmulators/package.mo'
    modelpath = 'BuildingEmulators.BuildingSystem'
    # ------------

    # COMPILE FMU
    # -----------
    fmupath = parser.export_fmu(modelpath, [mopath], tool=  sys.argv[1])
    # -----------

    return fmupath

if __name__ == "__main__":
    fmupath = compile_fmu()
