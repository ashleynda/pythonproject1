# def valid(channel):
#     pass
#
#
# class Tv:
#     def __init__(self):
#         self.channel = 0
#         self.volume_level = 0
#         self.on = False
#
#     def turn_on(self):
#         self.on = True
#
#     def get_channel(self):
#         return self.channel
#
#     def channel_down(self):
#         if self.channel > 0:
#             self.channel = self.channel - 1
#
#     def channel_up(self):
#         if self.channel < 150:
#             self.channel = self.channel + 1
#
#     def set_channel(self, channel):
#         if valid(channel):
#             self.channel = channel
#
#     def get_volume_level(self):
#         return self.volume_level
#
#     def volume_up(self):
#         if 100 > self.volume_level > 0:
#             self.volume_level += 1
#
#     def volume_down(self):
#         if self.on:
#             if 0 < self.volume_level < 100:
#                 self.volume_level -= 1
#
#     def set_volume_level(self, volume_level):
#         if self.volume_level < 100:
#             self.volume_level = volume_level
