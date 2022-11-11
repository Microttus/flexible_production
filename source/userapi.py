'''
Gear Generator MAS417 Project
Flexible Production
UserApi
Martin Økter
25.10.2022

Sources:
https://stackoverflow.com/questions/48093361/using-matplotlib-in-pygame
'''

import apilibrary as api
import colors as cl
import os



class UserApi:
    def __init__(self):
        self.specificationList = [0, 0, 0, 0, 0, 0, 0, 0]
        self._locationTemp = 20
        self._filepath = 'C:/dustepc/dustemappe'
        self.myApi = api.ApiLibrary()
        self._filename = ''

    def userInput(self):
        '''
        User GUI for user input for size of the gear
        '''
        self.myApi.message_display_center("Gear Generator v0.2", 70, 600, 50, cl.black)
        self.myApi.message_display_center("Press 'Enter' to exit text block", 20, 600, 100, cl.black)
        self.myApi.message_display_center("OBS: If 'number of teeth is left to zero 'dummy gear are generated", 15, 600, 750, cl.dark_red)

        self.myApi.message_display("Inner diameter [d]:", 30, 80, 150, cl.black)
        self.myApi.message_display("Outer diameter [D]:", 30, 80, 225, cl.black)
        self.myApi.message_display("Teeth height [T]:", 30, 80, 300, cl.black)
        self.myApi.message_display("Gear height [H]:", 30, 80, 375, cl.black)
        self.myApi.message_display("Number of teeth [n]:", 30, 80, 450, cl.black)
        self.myApi.message_display("Print temperature [t]:", 30, 80, 525, cl.black)
        self.myApi.message_display("Use location latitude [n]:", 30, 80, 600, cl.black)
        self.myApi.message_display("Use loaction longitude [t]:", 30, 80, 675, cl.black)

        self.myApi.text_box_float(460, 150, 100, 30, cl.dark_blue, cl.black, 30, 0)
        self.myApi.text_box_float(460, 225, 100, 30, cl.dark_blue, cl.black, 30, 1)
        self.myApi.text_box_float(460, 300, 100, 30, cl.dark_blue, cl.black, 30, 2)
        self.myApi.text_box_float(460, 375, 100, 30, cl.dark_blue, cl.black, 30, 3)
        self.myApi.text_box_float(460, 450, 100, 30, cl.dark_blue, cl.black, 30, 4)
        self.myApi.text_box_float(460, 525, 100, 30, cl.dark_blue, cl.black, 30, 5)
        self.myApi.text_box_float(460, 600, 100, 30, cl.dark_blue, cl.black, 30, 6)
        self.myApi.text_box_float(460, 675, 100, 30, cl.dark_blue, cl.black, 30, 7)

        self.myApi.img_show(680, 170, 1)

        action = self.myApi.button('Generate Gear', 780, 630, 160, 80, cl.dark_white, cl.dark_blue, True)

        self.myApi.update_screen()

        if action:
            self.updateValues()
            return True

        return False


    def updateValues(self):
        '''
        Used for update spesification list from the internal list in the API class
        '''
        self.specificationList = self.myApi.returnLists()
        return 0

    def fetchingTemperature(self):
        '''
        Page for the point fas and the temperature fase
        '''

        self.myApi.message_display_center("Fetching temperature data and generating point cloud", 30, 600, 200, cl.black)
        self.myApi.message_display_center("Name of genrated file:", 20, 600, 260, cl.black)

        self.myApi.text_box(600, 300, 200, 30, cl.dark_blue, cl.black, 30, 0)

        self.myApi.img_show(500, 500, 2)

        action = self.myApi.button('Next', 520, 680, 160, 80, cl.dark_white, cl.dark_blue, True)

        self.myApi.message_display_center("Loading points, please wait until box is active", 15, 600, 350, cl.dark_red)

        self.myApi.update_screen()

        if action:
            self._filename = self.myApi.returnName()
            return True

        return False

    def generatingPMS(self, temp):
        self._locationTemp = temp

        self.myApi.message_display_center("Generating mesh", 40, 600, 200, cl.black)
        self.myApi.message_display_center("Mean temperature last year at your location", 20, 600, 300, cl.grey)
        self.myApi.message_display_center("was {} degrees celsius".format(self._locationTemp), 20, 600, 350, cl.grey)

        self.myApi.img_show(500, 500, 2)

        self.myApi.update_screen()

        return False

    def outputPage(self):
        self._filepath = os.getcwd()
        self.myApi.show_plot(400, 200)
        self.myApi.message_display_center("Your gear are ready!", 40, 600, 170, cl.black)
        self.myApi.message_display_center("It is saved in {}".format(self._filepath), 20, 600, 250, cl.black)

        action = self.myApi.button('New Gear', 520, 650, 160, 80, cl.dark_white, cl.dark_blue, True)

        self.myApi.update_screen()

        if action:
            self.myApi.resetSInd()
            return True

        return False

    def getList(self):
        return self.specificationList

    def getFilename(self):
        return self._filename
