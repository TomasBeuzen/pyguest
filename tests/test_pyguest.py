import pyguest
import numpy as np


def test_simulate():
    np.random.seed(2020)
    x = list(np.random.randint(0, 11, 100) / 10)
    y = pyguest.simulate(x)
    assert y.mean() == 49.47
    assert y.shape[0] == 100
