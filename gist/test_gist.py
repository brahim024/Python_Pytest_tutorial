# in this video we will take a look at
# Test functions
# markers
# Skip, Skip_if
# fixtures
# Parametrize

# if we want to run test type: pytest src/.../test_functions.py
# if we want to run test and show more info type: pytest src/.../test_functions.py -v
# if we want to run test and skip all warning type: pytest src/.../test_functions.py -v \
#     -p no:warnings
# if we want to run just slow tests type: pytest src/.../test_functions.py -v \
#     -p no:warnings -m slow
# if we want to run just not slow tests type: pytest gist/test_gist.py -v -p no:warnings -m "not slow"
import pytest


def test_our_first_input() -> None:
    assert 1 == 1


@pytest.mark.skip(reason="Just for Testing the test")
def test_should_be_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="Skipped because 4 not < 1")
def test_should_be_skiped_if() -> None:
    assert 1 < 2


@pytest.mark.xfail
def test_dont_care_if_fail() -> None:
    assert 1 < 2


@pytest.mark.slow()
def test_function_as_slow1() -> None:
    pass


@pytest.mark.slow
def test_function_as_slow() -> None:
    pass


