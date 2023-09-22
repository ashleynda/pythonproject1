class Entry:

    def __init__(self, id, title, body):
        self.__id = id
        self.__title = title
        self.__body = body

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def getId(self):
        return self.__id

    def get_entry(self):
        return f'{self.__id} {self.__title} {self.__body}'
