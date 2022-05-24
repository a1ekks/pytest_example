import os


class Session:

    def close(self):
        print("Closed session")


class Api:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = Session()

    def request(self, method, date):
        print("Executed", method)

    def close(self):
        print("Closing session")
        self.session.close()

class FileHelper:

    def __init__(self, api):
        self.api = api

    def remove_file(self, filepath):
        if os.path.isfile(filepath):
            print("removing file %s", filepath)
            os.unlink(filepath)

    def prepare_file(self, filepath):
        print("preparing file %s for upload", filepath)
        return bytes()

    def upload_file(self, filepath):
        data = self.prepare_file(filepath)
        self.api.request("POST", data)
