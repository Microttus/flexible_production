'''
Gear Generator MAS417 Project
Flexible Production
ApiLibary
Martin Økter
25.10.2022

Referanse:
This code was originaly inspired by a open source "Dodge Coin Game"
'''

#import key_board_input
import pygame
import key_board_input
import colors as cl

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab

class ApiLibrary:
    '''
    A compleate libary for buliding windows with
    GUI and self containg run management
    '''

    def __init__(self):
        self.mode = 0
        pygame.init()
        print("initialized")

        display_width = 1200
        display_height = 800

        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Gear Generator')
        self.clock = pygame.time.Clock()
        Icon = pygame.image.load('Images/gear.png')
        pygame.display.set_icon(Icon)
        self.clicked = pygame.mouse.get_pressed(3)
        self.click = 0
        self.fps = 15
        self.text_for_print = [[]]
        self.specification = []
        self._file_name = [[]]
        self._filename = ''

        self.gearDisc = pygame.image.load('Images/gearIlu.jpg')
        self.gearDisc = pygame.transform.scale(self.gearDisc,(400,400))
        self.gearSmall = pygame.transform.scale(self.gearDisc, (160, 160))


    def update_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        click_prev = self.clicked[0]
        self.clicked = pygame.mouse.get_pressed(3)
        self.click = self.clicked[0] - click_prev

        pygame.display.update()
        self.clock.tick(self.fps)
        self.gameDisplay.fill(cl.white)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, cl.black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, size, x, y, color=(0, 0, 0)):
        largeText = pygame.font.SysFont('calibri', size)
        l_Text = largeText.render(str(text), 1, color)
        # TextSurf, TextRect = text_objects(text, l_Text)
        TextRect = (x, y)
        self.gameDisplay.blit(l_Text, TextRect)

    def message_display_center(self, text, size, x, y, color=(0, 0, 0)):
        largeText = pygame.font.SysFont('calibri', size)
        l_Text = largeText.render(str(text), 1, color)
        TextRect = l_Text.get_rect()
        TextRect.center = (x, y)
        self.gameDisplay.blit(l_Text, TextRect)

    def img_show(self, x, y, img_ind):
        if img_ind == 1:
            self.gameDisplay.blit(self.gearDisc, (x, y))
        elif img_ind == 2:
            self.gameDisplay.blit(self.gearSmall, (x, y))
        return 0

    def button(self, msg, x, y, width, height, inactive, active, action=None, non_action=None):
        mouse = pygame.mouse.get_pos()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, active, (x, y, width, height))
            if self.click == 1 and action != None:
                return action
        else:
            pygame.draw.rect(self.gameDisplay, inactive, (x, y, width, height))
        smallText = pygame.font.SysFont('calibri', 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = (x + (width / 2), y + (height / 2))
        self.gameDisplay.blit(textSurf, textRect)

        return non_action

    def text_box_float(self, x_place, y_place, width, height, active, inactive, size=30, text_index=0):
        if len(self.text_for_print) < text_index+2:
            self.text_for_print.append([])
            self.specification.append(0)

        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        action = False
        print_key = True
        x_place = x_place - width / 2

        pygame.draw.rect(self.gameDisplay, cl.white, (x_place, y_place, width, height))

        if x_place + width > pos[0] > x_place and y_place + height > pos[1] > y_place:
            if pressed[0] == 1 or action == True:
                action = True
                while print_key:
                    text_two = key_board_input.key_board()
                    if text_two != None and text_two != '-1':
                        self.text_for_print[text_index].append(text_two)
                    if text_two == '-1' and len(self.text_for_print[text_index]) > 0:
                        del (self.text_for_print[text_index][-1])
                    print_key = key_board_input.key_key()
                    fin_tex = ''.join(self.text_for_print[text_index])
                    self.message_display(fin_tex, size, x_place + 10, y_place, cl.black)
                    pygame.draw.rect(self.gameDisplay, active, (x_place, y_place, width, height), 5)
                    pygame.display.update(pygame.rect.Rect(x_place, y_place, width, height))
                    self.gameDisplay.fill(cl.white)
            else:
                pygame.draw.rect(self.gameDisplay, active, (x_place, y_place, width, height), 3)
                action = False
        else:
            action = False
            pygame.draw.rect(self.gameDisplay, inactive, (x_place, y_place, width, height), 3)

        fin_tex = ''.join(self.text_for_print[text_index])

        try:
            number_spec = float(fin_tex)
            self.specification[text_index] = number_spec
        except ValueError:
            self.text_for_print[text_index] = []

        self.message_display(fin_tex, size, x_place + 10, y_place, cl.black)
        action = True
        key_board_input.key_key(True)

    def text_box(self, x_place, y_place, width, height, active, inactive, size=30, text_index=0):

        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        action = False
        print_key = True
        x_place = x_place - width / 2

        pygame.draw.rect(self.gameDisplay, cl.white, (x_place, y_place, width, height))

        if x_place + width > pos[0] > x_place and y_place + height > pos[1] > y_place:
            if pressed[0] == 1 or action == True:
                action = True
                while print_key:
                    text_two = key_board_input.key_board()
                    if text_two != None and text_two != '-1':
                        self._file_name[text_index].append(text_two)
                    if text_two == '-1' and len(self._file_name[text_index]) > 0:
                        del (self._file_name[text_index][-1])
                    print_key = key_board_input.key_key()
                    fin_tex = ''.join(self._file_name[text_index])
                    self.message_display(fin_tex, size, x_place + 10, y_place, cl.black)
                    pygame.draw.rect(self.gameDisplay, active, (x_place, y_place, width, height), 5)
                    pygame.display.update(pygame.rect.Rect(x_place, y_place, width, height))
                    self.gameDisplay.fill(cl.white)
            else:
                pygame.draw.rect(self.gameDisplay, active, (x_place, y_place, width, height), 3)
                action = False
        else:
            action = False
            pygame.draw.rect(self.gameDisplay, inactive, (x_place, y_place, width, height), 3)

        self._filename = ''.join(self._file_name[text_index])

        self.message_display(self._filename, size, x_place + 10, y_place, cl.black)
        action = True
        key_board_input.key_key(True)

    def show_plot(self):
        fig = pylab.figure(figsize=[4, 4],  # Inches
                           dpi=100,  # 100 dots per inch, so the resulting buffer is 400x400 pixels
                           )
        ax = fig.gca()
        ax.plot([1, 2, 4])

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        self.gameDisplay.blit(surf, (0, 0))

    def returnLists(self):
        return self.specification

    def returnName(self):
        if self._filename == '':
            self._filename = 'gear.stl'
        else:
            self._filename += '.stl'

        return self._filename
