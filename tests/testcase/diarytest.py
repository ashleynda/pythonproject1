import unittest
from tests.diary import Diary
from tests.diaryexceptions import InvalidIdException
from tests.entry import Entry


class TestDiaryFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.diary = Diary("Ashley", "1234")

    def test_that_diary_exist(self):
        self.assertTrue(self.diary)

    def test_that_diary_is_locked(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_is_unlocked(self):
        self.diary.lock_diary()
        self.diary.unlock_diary("1234")

    def test_that_entry_can_be_created(self):
        self.diary.create_entry(1, "Life lately", "These are the happenings")
        # self.assertRaises(InvalidIdException, self.diary.find_entry_by_id, 1)
        self.assertEqual("1 Life lately These are the happenings", self.diary.find_entry_by_id(1).get_entry())

    def test_that_entry_can_be_deleted(self):
        self.diary.create_entry(1,"Life lately", "These are the happenings")

        self.diary.delete_entry(1)
        self.assertRaises(InvalidIdException, self.diary.find_entry_by_id, 1)

    def test_that_update_entry(self):
        self.diary.create_entry(1, "Life lately", "These are the happenings")
        self.diary.update_entry(1, "Success and failures", "Journey so far")
        self.assertEqual(Entry(1, "Success and failures", "Journey so far").get_entry(),self.diary.find_entry_by_id(1)
                         .get_entry())




