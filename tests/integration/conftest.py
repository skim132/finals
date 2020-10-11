import os
import pytest
from movie import create_app
from movie.adapters import memory_repository
from movie.adapters.memory_repository import MemoryRepository
MOVIE_DATA_PATH = os.path.join('C:','users','seank','OneDrive','Desktop','finals','movie','adapters','datafiles','Data1000Movies.csv')
USER_DATA_PATH= os.path.join('movie','adapters','datafiles','users.csv')
REVIEW_DATA_PATH= os.path.join('movie','adapters','datafiles','reviews.csv')

@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(MOVIE_DATA_PATH,repo)
    return repo
@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': MOVIE_DATA_PATH,               # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()
class AuthenticationManager:
    def __init__(self, client):
        self._client = client

    def login(self, username='sean', password='150000$g65YfNpF$35f076f8bc3806a73c143a7d256412963be8378f6c4cd966bd2022ef3e7fbdec'):
        return self._client.post(
            'auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthenticationManager(client)
