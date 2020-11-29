import numpy as np
import os
import pandas as pd

from nayose import split_address, complement_address


def test_separate_address():
    file_path = os.path.join(os.path.dirname(__file__), 'data/test.ft')
    test = pd.read_feather(file_path)
    test['Result'] = test['Address'].apply(split_address)
    assert np.all(test['State'] == test['Result'].apply(lambda x: x[0]))
    assert np.all(test['City'] == test['Result'].apply(lambda x: x[1]))
    assert np.all(test['Street'] == test['Result'].apply(lambda x: x[2]))


def test_complete_address_1():
    correct = '北海道札幌市中央区盤渓'
    test = '海札幌中区盤渓'
    assert correct == complement_address(test)


def test_complete_address_2():
    correct = '長野県長野市南県町111'
    test = '長野市南県町111'
    assert correct == complement_address(test)


def test_complete_address_3():
    correct = '福岡県福岡市中央区天神1-1-1 ABCビル'
    test = '福岡市中央区天神1-1-1 ABCビル'
    assert correct == complement_address(test)


def test_complete_address_4():
    correct = '福岡県福岡市東区馬出1-1-11'
    test = '福岡市東区馬出1-1-11'
    assert correct == complement_address(test)


def test_complete_address_5():
    correct = '大阪府大阪市'
    test = '大阪市'
    assert correct == complement_address(test)


def test_complete_address_6():
    correct = '大阪府'
    test = '大阪府'
    assert correct == complement_address(test)


def test_complete_address_7():
    correct = '奈良県'
    test = '奈良県'
    assert correct == complement_address(test)


def test_complete_address_8():
    correct = '東京都港区港南11−11−11品川あいうビル1F'
    test = '港区港南11−11−11品川あいうビル1F'
    assert correct == complement_address(test)


def test_complete_address_9():
    correct = '東京都千代田区大手町1−1−1大手町あいうえビル'
    test = '千代田区大手町1−1−1大手町あいうえビル'
    assert correct == complement_address(test)


def test_complete_address_10():
    correct = '東京都大田区蒲田１−１−１１１'
    test = '蒲田１−１−１１１'
    assert correct == complement_address(test)


def test_complete_address_11():
    correct = '大阪府大阪市中央区備後町1−1−1'
    test = '大阪市中央区備後1−1−1'
    assert correct == complement_address(test)


def test_complete_address_12():
    correct = '東京都千代田区霞が関1−1−1'
    test = '霞ヶ関1−1−1'
    assert correct == complement_address(test)
