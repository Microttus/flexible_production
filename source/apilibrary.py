'''
Gear Generator MAS417 Project
Flexible Production
ApiLibary
Martin Økter
25.10.2022
'''

#import key_board_input
import pygame

class ApiLibrary:
    def __init__(self):
        self.mode = 0
        pygame.init()
        print("initialized")

        display_width = 1200
        display_height = 800

        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('OverRun')
        self.clock = pygame.time.Clock()
        # Icon = pygame.image.load('Welle.png')
        # pygame.display.set_icon(Icon)
        self.clicked = pygame.mouse.get_pressed(3)
        self.click = 0
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.fps = 15

    def update_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        click_prev = self.clicked[0]
        self.clicked = pygame.mouse.get_pressed(3)
        self.click = self.clicked[0] - click_prev

        print(self.click)

        pygame.display.update()
        self.clock.tick(self.fps)
        self.gameDisplay.fill(self.white)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, size, x, y, color=(0, 0, 0)):
        largeText = pygame.font.SysFont('comicsansms', size)
        l_Text = largeText.render(str(text), 1, color)
        # TextSurf, TextRect = text_objects(text, l_Text)
        TextRect = (x, y)
        self.gameDisplay.blit(l_Text, TextRect)

    def button(self, msg, x, y, width, height, inactive, active, action=None):
        mouse = pygame.mouse.get_pos()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, active, (x, y, width, height))
            if self.click == 1 and action != None:
                global next
                next = action
        else:
            pygame.draw.rect(self.gameDisplay, inactive, (x, y, width, height))
        smallText = pygame.font.SysFont('comicsansms', 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = (x + (width / 2), y + (height / 2))
        self.gameDisplay.blit(textSurf, textRect)

    def text_box(self,x_place, y_place, width, height, active, inactive, size=30):
        global text_for_print
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        action = False
        print_key = True
        x_place = x_place - width / 2

        pygame.draw.rect(gameDisplay, white, (x_place, y_place, width, height))

        if x_place + width > pos[0] > x_place and y_place + height > pos[1] > y_place:
            if pressed[0] == 1 or action == True:
                action = True
                while print_key:
                    text_two = key_board_input.key_board()
                    if text_two != None and text_two != '-1':
                        text_for_print.append(text_two)
                    if text_two == '-1' and len(text_for_print) > 0:
                        del (text_for_print[-1])
                    print_key = key_board_input.key_key()
                    fin_tex = ''.join(text_for_print)
                    message_display_2(fin_tex, size, x_place + 10, y_place, black)
                    pygame.draw.rect(gameDisplay, active, (x_place, y_place, width, height), 5)
                    pygame.display.update(pygame.rect.Rect(x_place, y_place, width, height))
                    gameDisplay.fill(white)
            else:
                pygame.draw.rect(gameDisplay, active, (x_place, y_place, width, height), 3)
                action = False
        else:
            action = False
            pygame.draw.rect(gameDisplay, inactive, (x_place, y_place, width, height), 3)

        fin_tex = ''.join(text_for_print)
        message_display_2(fin_tex, size, x_place + 10, y_place, black)
        action = True
        key_board_input.key_key(True)

