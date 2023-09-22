from tests.diaryexceptions import InvalidIdException
from tests.entry import Entry


class Diary:

    def __init__(self, username, password):
        self.entry = None
        self.__list_of_entries = []
        self.__is_locked = False
        self.username = username
        self.__password = password

    def is_locked(self):
        return self.is_locked

    def lock_diary(self):
        pass

    def unlock_diary(self, password):
        return self.__password

    def create_entry(self, id, title, body):
        entry = Entry(id, title, body)
        self.__list_of_entries.append(entry)

    def __generateId(self):
        return len(self.__list_of_entries) + 1

    def find_entry_by_id(self, id):
        for entry in self.__list_of_entries:
            if entry.getId() == id:
                return entry
        raise InvalidIdException("Entry could not be found")

    def delete_entry(self, id):
        # for entry in self.__list_of_entries:
        #     if entry.getId() == id:
        #         return self.__list_of_entries.remove(id)
        entry = self.find_entry_by_id(id)
        self.__list_of_entries.remove(entry)

    def update_entry(self, id, title, body):
        entry = self.find_entry_by_id(id)
        entry.set_id(id)
        entry.set_title(title)
        entry.set_body(body)

    def get_diary_by_username(self):
        return self.username


