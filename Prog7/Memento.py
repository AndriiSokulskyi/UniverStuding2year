from ForeignID import *

class Memento:
    def __init__(self, collection):
        self._collection = collection.copy_collection()

    def get_collection(self):
        return self._collection


class Caretaker:
    def __init__(self, collection=None, max_size = 6): #для зберігання останніх 5 дій
        self._mementos = []
        self._collection = collection
        self._max_size = max_size
        self.last_pos = -1

    def backup(self):
        if len(self._mementos) == self._max_size:
            self._mementos.pop(0)
        self._mementos.append(self._collection.save())

    def undo(self):
        if (self.last_pos == -len(self._mementos)) or (len(self._mementos) == 0):
            print('Nothing to undo.')
            return
        self.last_pos -= 1
        memo = self._mementos[self.last_pos]
        self._collection.restore(memo)

    def redo(self):
        if (self.last_pos == -1) or (len(self._mementos) == 0):
            print('Nothing to redo.')
            return
        self.last_pos += 1
        memo = self._mementos[self.last_pos]
        self._collection.restore(memo)