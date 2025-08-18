import pytest

from .get_identities import GetIdentitiesMocker
from .userinfo import UserinfoMocker


@pytest.fixture(scope="session")
def get_identities_mocker():
    return GetIdentitiesMocker()


@pytest.fixture(scope="session")
def userinfo_mocker():
    return UserinfoMocker()
