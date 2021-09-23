import os

import numpy as np
import pandas as pd

from nayose import complement_address, split_address


def test_separate_address() -> None:
    file_path = os.path.join(os.path.dirname(__file__), "data/test.ft")
    test = pd.read_feather(file_path)
    test["Result"] = test["Address"].apply(split_address)
    assert np.all(test["State"] == test["Result"].apply(lambda x: x[0]))
    assert np.all(test["City"] == test["Result"].apply(lambda x: x[1]))
    assert np.all(test["Street"] == test["Result"].apply(lambda x: x[2]))


def test_complement_address_1() -> None:
    correct = "北海道札幌市中央区盤渓"
    test = "海札幌中区盤渓"
    assert correct == complement_address(test)


def test_complement_address_2() -> None:
    correct = "長野県長野市南県町111"
    test = "長野市南県町111"
    assert correct == complement_address(test)


def test_complement_address_3() -> None:
    correct = "福岡県福岡市中央区天神1-1-1 ABCビル"
    test = "福岡市中央区天神1-1-1 ABCビル"
    assert correct == complement_address(test)


def test_complement_address_4() -> None:
    correct = "福岡県福岡市東区馬出1-1-11"
    test = "福岡市東区馬出1-1-11"
    assert correct == complement_address(test)


def test_complement_address_5() -> None:
    correct = "大阪府大阪市"
    test = "大阪市"
    assert correct == complement_address(test)


def test_complement_address_6() -> None:
    correct = "大阪府"
    test = "大阪府"
    assert correct == complement_address(test)


def test_complement_address_7() -> None:
    correct = "奈良県"
    test = "奈良県"
    assert correct == complement_address(test)


def test_complement_address_8() -> None:
    correct = "東京都港区港南11−11−11品川あいうビル1F"
    test = "港区港南11−11−11品川あいうビル1F"
    assert correct == complement_address(test)


def test_complement_address_9() -> None:
    correct = "東京都千代田区大手町1−1−1大手町あいうえビル"
    test = "千代田区大手町1−1−1大手町あいうえビル"
    assert correct == complement_address(test)


def test_complement_address_10() -> None:
    correct = "東京都大田区蒲田１−１−１１１"
    test = "蒲田１−１−１１１"
    assert correct == complement_address(test)


def test_complement_address_11() -> None:
    correct = "大阪府大阪市中央区備後町1−1−1"
    test = "大阪市中央区備後1−1−1"
    assert correct == complement_address(test)


def test_complement_address_12() -> None:
    correct = "東京都千代田区霞が関1−1−1"
    test = "霞ヶ関1−1−1"
    assert correct == complement_address(test)


def test_complement_address_13() -> None:
    test = ""
    assert split_address(test)[0] is None


def test_complement_address_14() -> None:
    test = "東京都"
    assert split_address(test)[0] == "東京都"


def test_complement_address_15() -> None:
    correct = "東京都千代田区大手町"
    test = "東京都大手町"
    assert correct == complement_address(test)


def test_complement_address_16() -> None:
    correct = "東京都大島町"
    test = "東京都大島町"
    assert correct == complement_address(test)


def test_complement_address_17() -> None:
    correct = "A"
    test = "海外A"
    assert correct == complement_address(test)


def test_complement_address_18() -> None:
    correct = ""
    test = "海外"
    assert correct == complement_address(test)


def test_complement_address_19() -> None:
    correct = "神奈川県三浦市海外町"
    test = "海外町"
    assert correct == complement_address(test)
