import os
from unittest import mock

import pytest

from file_helper import FileHelper, Api


# fh is fixture check in conftest

class TestFileHelper:

    def test_init(self):
        api = object()
        fh = FileHelper(api)
        assert fh.api is api

    def test_remove_file(self, fh, temp_file):
        fh.remove_file(temp_file)
        assert os.path.exists(temp_file) is False

    @mock.patch.object(FileHelper, 'prepare_file')
    def test_upload_file(self, mocked_prepare_file):
        fake_api = mock.MagicMock()

        fh = FileHelper(fake_api)
        fh.upload_file('fake filepath')
        fake_api.request.assert_called_with("POST", mocked_prepare_file.return_value)

    @mock.patch('file_helper.os')
    def test_uses_unlink_for_remove(self, mocked_fh_os, fh):
        filepath = 'test'
        mocked_fh_os.path.isfile.return_value = True
        fh.remove_file(filepath)
        mocked_fh_os.unlink_assert_called_ones_with(filepath)
