'''
Gear Generator MAS417 Project
Flexible Production
UserApi
Martin Økter
25.10.2022
'''

import apilibrary as api
import colors as cl


class UserApi:
    def __init__(self):
        # [innerDiameter, nuberOfTeeth, printTemperature, teethheight, locationLong, locationLat, locationTemp]
        self.specificationList = [0, 0, 0, 0, 0, 0, 0]
        self._locationTemp = 20

        self.myApi = api.ApiLibrary()

    def userInput(self):
        self.myApi.message_display("Gear Generator v0.1", 70, 300, 40, cl.black)

        self.myApi.message_display("Inner diameter [d]:", 30, 80, 200, cl.black)
        self.myApi.message_display("Outer diameter [D]:", 30, 80, 275, cl.black)
        self.myApi.message_display("Teeth height [T]:", 30, 80, 350, cl.black)
        self.myApi.message_display("Number of teeth [n]:", 30, 80, 425, cl.black)
        self.myApi.message_display("Print temperature [t]:", 30, 80, 500, cl.black)
        self.myApi.message_display("Use location latitude [n]:", 30, 80, 575, cl.black)
        self.myApi.message_display("Use loaction longitude [t]:", 30, 80, 650, cl.black)

        self.myApi.text_box(460, 200, 100, 30, cl.dark_blue, cl.black, 30, 0)
        self.myApi.text_box(460, 275, 100, 30, cl.dark_blue, cl.black, 30, 1)
        self.myApi.text_box(460, 350, 100, 30, cl.dark_blue, cl.black, 30, 2)
        self.myApi.text_box(460, 425, 100, 30, cl.dark_blue, cl.black, 30, 3)
        self.myApi.text_box(460, 500, 100, 30, cl.dark_blue, cl.black, 30, 4)
        self.myApi.text_box(460, 575, 100, 30, cl.dark_blue, cl.black, 30, 5)
        self.myApi.text_box(460, 650, 100, 30, cl.dark_blue, cl.black, 30, 6)

        self.myApi.img_show(600, 400, 0)

        action = self.myApi.button('Generate Gear', 800, 600, 160, 80, cl.grey, cl.dark_blue, True)

        self.myApi.update_screen()

        if action:
            self.updateValues()
            return True

        return False


    def updateValues(self):
        self.specificationList = self.myApi.returnLists()
        return 0

    def fetchingTemperature(self):
        self.myApi.message_display("Fetching temperature data", 40, 350, 200, cl.black)
        self.myApi.message_display("and generating point cloud", 40, 350, 300, cl.black)

        self.myApi.update_screen()

        # Point generating here
        # Return True when finished!

        return True

    def generatingPMS(self):
        self.myApi.message_display("Generating mesh", 50, 350, 300, cl.black)
        self.myApi.message_display("Mean temperature last year at your location", 30, 350, 400, cl.grey)
        self.myApi.message_display("was {} degrees celsius".format(self._locationTemp), 30, 350, 450, cl.grey)

        self.myApi.update_screen()

        return False

    def outputPage(self):


    def getList(self):
        return self.specificationList
