# ------------------------- Show modules search path ------------------------- #
# import sys

# print(sys.path)

# ------------------------ Import module as namespace ------------------------ #
# import my_module as mm


# mm.greet("Ada")
# print(mm.PI)

# global = {
#     mm:...,
# }

# -------------------------- Import name from module ------------------------- #
# from my_module import greet

# greet("Ada")
# # print(PI)
# # x = 1

# print(x)
# # global = {
# #     greet,
# #     PI,
# #     x
# # }

# ---------------------------- Import from package --------------------------- #
# from lib.audio.player import play
# from lib.video.player import play
import lib.audio.player as audio_player
import lib.video.player as vidio_player

audio_player.play()
vidio_player.play()
