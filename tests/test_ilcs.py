import numpy
import math


def test_chapter_small_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21', '126 55/21'),
        numpy.array([1, 0, 1, math.sqrt(126-125), 0, 0, 0, 0, 1, 1, 1, 0, 0, 0])
    )


def test_chapter_large_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21', '6 55/21'),
        numpy.array([1, 0, 1, math.sqrt(125-6), 0, 0, 0, 0, 1, 1, 1, 0, 0, 0])
    )


def test_act_prefix_small_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21', '125 56/21'),
        numpy.array([1, 0, 1, 0, math.sqrt(56-55), 0, 0, 0, 1, 1, 1, 0, 0, 0])
    )


def test_act_prefix_large_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 550/21', '125 5/21'),
        numpy.array([1, 0, 1, 0, math.sqrt(550-5), 0, 0, 0, 1, 1, 1, 0, 0, 0])
    )


def test_section_small_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21', '125 55/22'),
        numpy.array([1, 0, 1, 0, 0, math.sqrt(22-21), 0, 0, 1, 1, 1, 0, 0, 0])
    )


def test_section_large_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21', '125 55/210'),
        numpy.array([1, 0, 1, 0, 0, math.sqrt(210-21), 0, 0, 1, 1, 1, 0, 0, 0])
    )


def test_subsection_small_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-1', '125 55/21-2'),
        numpy.array([1, 0, 1, 0, 0, 0, math.sqrt(2-1), 0, 1, 1, 1, 1, 0, 0])
    )


def test_subsection_large_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-1', '125 55/21-100'),
        numpy.array([1, 0, 1, 0, 0, 0, math.sqrt(100-1), 0, 1, 1, 1, 1, 0, 0])
    )


def test_subsection_small_alphabetic_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-a', '125 55/21-b'),
        numpy.array([1, 0, 1, 0, 0, 0, math.sqrt(1-0), 0, 1, 1, 1, 1, 0, 0])
    )


def test_subsection_large_alphabetic_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21-a', '125 55/21-z'),
        numpy.array([1, 0, 1, 0, 0, 0, math.sqrt(25-0), 0, 1, 1, 1, 1, 0, 0])
    )


def test_attempted_delta(ilcs):
    numpy.testing.assert_almost_equal(
        ilcs.comparator('125 55/21 (att)', '125 55/21 (con)'),
        numpy.array([1, 0, 1, 0, 0, 0, 0, ilcs.compareString('att', 'con'), 1, 1, 1, 0, 1, 0])
    )
