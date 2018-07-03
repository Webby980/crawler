from app.storage.storage_adapter import StorageAdapter


class FileAdapter(StorageAdapter):

    def get(self, path):
        with open(path, 'r') as file:
            return file.read()
