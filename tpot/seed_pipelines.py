# -*- coding: utf-8 -*-

'''
Copyright 2016 Randal S. Olson

This file is part of the TPOT library.

The TPOT library is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

The TPOT library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
the TPOT library. If not, see http://www.gnu.org/licenses/.
'''

import random

seeds = ['_random_forest(ARG0, mul(100, 5), 0)',
         '_random_forest(ARG0, mul(50, 5), 0)',
         '_random_forest(ARG0, mul(25, 5), 0)',]

def random_seed_individual():
    return seeds[random.randint(0, len(seeds) - 1)]
