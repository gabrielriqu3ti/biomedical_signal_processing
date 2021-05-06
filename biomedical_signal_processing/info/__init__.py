# -*- coding: utf-8 -*-
##
# @file __init__.py
# @brief Contain paths to information files
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 06/05/2021
#

import os
from pathlib import Path


PATH_NERNST_EQUATION_INFO = Path(os.path.abspath(__file__)).parent / 'nernst_equation.txt'
PATH_GOLDMAN_EQUATION_INFO = Path(os.path.abspath(__file__)).parent / 'goldman_equation.txt'

if not PATH_NERNST_EQUATION_INFO.exists():
    raise FileNotFoundError(PATH_NERNST_EQUATION_INFO.as_posix() + ' not found!')
if not PATH_GOLDMAN_EQUATION_INFO.exists():
    raise FileNotFoundError(PATH_GOLDMAN_EQUATION_INFO.as_posix() + ' not found!')
