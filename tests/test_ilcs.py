import numpy


def test_all_distances(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-a (att)', '126 55/21-b (atttt)'),
        numpy.array([
            1, 0, 1,
            ilcs.compareString('126', '125'),
            ilcs.compareString('55', '55'),
            ilcs.compareString('21', '21'),
            ilcs.compareString('a', 'b'),
            ilcs.compareString('att', 'atttt'),
            1, 1, 1, 1, 1, 0, 0
        ])
    )


def test_exact_match(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21 (att)', '125 55/21 (att)'),
        numpy.array([1, 0, 1, 0.5, 0.5, 0.5, 0, 0.5, 1, 1, 1, 0, 1, 0, 1])
    )


def test_mismatched_elements(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-a (att)', '125 56/21'),
        numpy.array([
            1, 0, 1,
            ilcs.compareString('125', '125'),
            ilcs.compareString('56', '55'),
            ilcs.compareString('21', '21'),
            0, 0, 1, 1, 1, 0, 0, 0, 0
        ])
    )
