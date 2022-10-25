'''
Gear Generator MAS417 Project
Flexible Production
ApiLibary
Martin Økter
25.10.2022
'''

import apilibrary as api
import pygame

myAPI = api.ApiLibrary()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (150, 0, 0)
dark_white = (200, 200, 200)
dark_blue = (0, 0, 150)
block_color = (0, 162, 232)
green = (31, 181, 4)
gold = (159, 138, 66)

def next():
    myAPI.message_display("Hey MF",15, 100, 200, black)

while True:
    next()
    myAPI.update_screen()


