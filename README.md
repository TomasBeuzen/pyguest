# pyguest 

[![PyPI version](https://badge.fury.io/py/pyguest.svg)](https://badge.fury.io/py/pyguest)
![build](https://github.com/TomasBeuzen/pyguest/workflows/build/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/TomasBeuzen/pyguest/branch/master/graph/badge.svg)](https://codecov.io/gh/TomasBeuzen/pyguest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p align="center">
  <img src="docs/pyguest-hex.png" width="300">
</p>

A simple python package for simulating event attendance from a guest list.

## Installation

```sh
pip install pyguest
```

## Usage

```python
import math
from pyguest import simulate

x = [0.5, 0.8, 1, 0.6, 0.2, 0.8, 1]  # guest attendance probabilities
y = simulate(x, simulations=1000)  # run simulations
math.ceil(y.mean())  # round up to get average number of guests across simulations
5
```

## Credits
This package was created with a Cookiecutter from [UBC-MDS/cookiecutter-ubc-mds](https://github.com/UBC-MDS/cookiecutter-ubc-mds) and was inspired by [@vcoia](https://github.com/vincenzocoia).
