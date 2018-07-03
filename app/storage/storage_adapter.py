from abc import ABC, abstractmethod


class StorageAdapter(ABC):

    @abstractmethod
    def get(self, path):
        pass
