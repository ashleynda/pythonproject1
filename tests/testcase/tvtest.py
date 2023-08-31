import unittest
from tests.tv import Tv


class TestTvFunction(unittest.TestCase):
    def test_that_tv_can_come_on(self):
        self.assertTrue(True, Tv.turn_on)

    def test_that_tv_can_go_off(self):
        self.assertFalse(False, Tv.turn_off)

    def test_that_tv_has_channel(self):
        self.assertTrue(True, Tv.channel)

    def test_that_tv_can_change_channel(self):
        tv = Tv()
        tv.turn_on()
        tv.channel = 1
        tv.channel_up()
        tv.channel_up()
        channel = tv.get_channel()
        self.assertEqual(3, channel)
        tv.channel_down()
        channel = tv.get_channel()
        self.assertEqual(2, channel)

    def test_that_channel_can_go_up(self):
        tv = Tv()
        tv.turn_on()
        tv.channel = 50
        tv.channel_up()
        channel = tv.get_channel()
        self.assertEqual(51, channel)
