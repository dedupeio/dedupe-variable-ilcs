import pytest
from dedupe.variables.ilcs import ILCSType


@pytest.fixture
def ilcs():
    return ILCSType({'field': 'foo'})
