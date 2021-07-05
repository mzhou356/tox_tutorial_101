"""test for prod.py."""


from tox_tutorial.prod import calc


def test_cal():
    assert calc(1, 1) == 1
