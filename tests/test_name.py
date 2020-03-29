from nayose import split_name


def test_separate_name():
    last, first = split_name("田中一郎")
    assert last == "田中"
    assert first == "一郎"

    last, first = split_name("林田輝")
    assert last == "林田"
    assert first == "輝"

    last, first = split_name("一林")
    assert last == "林"
    assert first == "一"

    last, first = split_name("林")
    assert last == "林"
    assert first == ""
