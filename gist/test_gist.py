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


class Company:
    def __init__(self, name, stock_symbol):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f'{self.name} : {self.stock_symbol}'


@pytest.fixture
def company() -> Company:
    return Company(name="amazone", stock_symbol="AMZ")


def test_company(company: Company) -> None:
    print(f"This is a Company{company}")
    assert company.name == 'amazone'


@pytest.mark.parametrize(
    'company_name',
    ['Instagram','Tiktok','Facebook'],
    ids=['Instagram TEST', 'Tiktok TEST', 'Facebook TEST']
)


def test_multiple_company_names(company_name: str) -> None:
    print(f"\nTest With {company_name}")

def raise_covid19():
    raise ValueError("CoronaVirus Exception")


def test_covid19_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19()
    assert str(e.value) == "CoronaVirus Exception"