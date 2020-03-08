from nayose import __version__
from nayose import split_address
import csv
import os


def test_version():
    assert __version__ == '0.1.0'


def test_separete_address():
    file_path = os.path.dirname(__file__)
    with open(os.path.join(file_path, 'data/test.csv')) as f:
        reader = csv.reader(f)
        for row in reader:
            s, c, st = split_address(row[0])
            assert s == row[1]
            assert c == row[2]
            assert st == row[3]
