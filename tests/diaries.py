from tests.diary import Diary


class Diaries:
    def __init__(self):
        self.__diaries_of_entry = []

    def add_diary(self, username, password):
        diary_adding = Diary(username, password)
        self.__diaries_of_entry.append(diary_adding)

    def find_by_username(self, username):
        for diary in self.__diaries_of_entry:
            if diary.get_diary_by_username() == username:
                return diary

    def can_delete(self, username, password):
        if self.find_by_username(username) is not None:
            self.__diaries_of_entry.remove(self.find_by_username(username))
