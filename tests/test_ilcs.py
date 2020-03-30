import numpy


def test_parse_1(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21', '126 55/21'),
        numpy.array([1, 0, 1, 2.1666667, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    )
