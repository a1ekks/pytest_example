import pytest

from file_helper import Api, FileHelper


@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / "filename.txt"
    f.write_text("content")
    return f


@pytest.fixture
def api():
    api = Api('tt_key')
    yield api
    api.close()


@pytest.fixture
def fh(api):
    fh = FileHelper(api)
    return fh
