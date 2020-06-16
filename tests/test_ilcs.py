import numpy


def test_all_distances(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-a (att)', '126 55/21-b (att)'),
        numpy.array([
            1,  # citation: Not Missing
            0,  # ambiguous: Dummy
            1,  # same name type?: Dummy
            ilcs.compareString('126', '125'),  # chapter: Derived
            ilcs.compareString('55', '55'),  # act prefix: Derived
            ilcs.compareString('21', '21'),  # section: Derived
            ilcs.compareString('a', 'b'),  # subsection: Derived
            1,  # chapter: Not Missing
            1,  # act prefix: Not Missing
            1,  # section: Not Missing
            1,  # subsection: Not Missing
            0,  # full string: String
            1,  # attempted match: Dummy
            0   # exact match: Exact
        ])
    )


def test_exact_match(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21 (att)', '125 55/21 (att)'),
        numpy.array([1, 0, 1, 0.5, 0.5, 0.5, 0, 1, 1, 1, 0, 0, 1, 1])
    )


def test_mismatched_elements(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-a (att)', '125 56/21'),
        numpy.array([
            1, 0, 1,
            ilcs.compareString('125', '125'),
            ilcs.compareString('55', '56'),
            ilcs.compareString('21', '21'),
            0, 1, 1, 1, 0, 0, 0, 0
        ])
    )


def test_attempted_match(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('725 5/21-a (att)', '720-5/8-4 725 6/21'),
        numpy.array([
            1, 0, 1,
            ilcs.compareString('125', '125'),
            ilcs.compareString('5', '6'),
            ilcs.compareString('21', '21'),
            0, 1, 1, 1, 0, 0, 1, 0
        ])
    )
