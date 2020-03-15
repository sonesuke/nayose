import numpy as np
import os
import pandas as pd

from nayose import __version__
from nayose import split_address


def test_version():
    assert __version__ == '0.1.0'


def test_separete_address():
    file_path = os.path.join(os.path.dirname(__file__), 'data/test.ft')
    test = pd.read_feather(file_path)
    test['Result'] = test['Address'].apply(split_address)
    assert np.all(test['State'] == test['Result'].apply(lambda x: x[0]))
    assert np.all(test['City'] == test['Result'].apply(lambda x: x[1]))
    assert np.all(test['Street'] == test['Result'].apply(lambda x: x[2]))
