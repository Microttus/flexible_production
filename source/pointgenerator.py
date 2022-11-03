'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
27.10.2022
'''

import numpy as np
import requests

class PointGenerator:
    def __init__(self, list):
        #self.specificationList = list
        # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
        self.cirkInner = list[0]
        self.cirkOuter = list[1]
        self.teethHeiht = list[2]
        self.gearHeight = list[3]
        self.numberOfTeeth = list[4]
        self.printTemp = list[5]
        self.Lat = list[6]  #Input from User interface, Need some restrictions
        self.Long = list[7] #Input from User interface, Need some restrictions

        self.cirkMain = self.cirkOuter - 2*self.teethHeiht
        self.theta = np.linspace(0, 2*np.pi, int(self.numberOfTeeth))
        self.thetaShifted = self.theta + self.theta[1]/2

        # Activates all the functions
        self.temperatureSizing()
        self.generatingInnerCircle()
        self.generatingMainCircle()
        self.generatingOuterCircle()
        self.offsetPoints()



    def generatingInnerCircle(self):

        # make a simple unit circle with teeth number of points
        self.xInner, self.yInner = self.cirkInner/2 * np.cos(self.theta), self.cirkInner/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle
        self.zInner = np.zeros(int(self.numberOfTeeth))
        self.pointsInner = [self.xInner, self.yInner, self.zInner]
        return self.pointsInner
    def generatingMainCircle(self):
         # make a simple unit circle
        self.xMain, self.yMain = self.cirkMain/2 * np.cos(self.theta), self.cirkMain/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle
        self.zMain = np.zeros(int(self.numberOfTeeth))
        self.pointsMain = [self.xMain, self.yMain, self.zMain]
        return self.pointsMain
    def generatingOuterCircle(self):
        # make a simple unit circle shiftet one halv tooth
        self.xOuter, self.yOuter = self.cirkOuter/2 * np.cos(self.thetaShifted), self.cirkOuter/2 * np.sin(self.thetaShifted) #x,y are coordinates for the inner cirkle
        self.zOuter = np.zeros(int(self.numberOfTeeth))
        self.pointsOuter = [self.xOuter, self.yOuter, self.zOuter]
        return self.pointsOuter
    def offsetPoints(self):
        #makes the offset plane to give the gear a thickness
        self.xInnerOffset = self.xInner
        self.yInnerOffset = self.yInner
        self.zInnerOffset = self.zInner + self.gearHeight
        self.pointsInnerOffset = [self.xInnerOffset, self.yInnerOffset, self.zInnerOffset]

        self.xMainOffset = self.xMain
        self.yMainOffset  = self.yMain
        self.zMainOffset  = self.zMain + self.gearHeight
        self.pointsMainOffset = [self.xMainOffset, self.yMainOffset, self.zMainOffset]

        self.xOuterOffset = self.xOuter
        self.yOuterOffset = self.yOuter
        self.zOuterOffset = self.zOuter + self.gearHeight
        self.pointsOuterOffset = [self.xOuterOffset, self.yOuterOffset, self.zOuterOffset]

    def temperatureSizing(self):

        # Insert your own client ID here
        self.client_id = 'd5398c91-5891-4c26-b199-990eebd37174'
        self.endpoint = 'https://frost.met.no/observations/v0.jsonld'
        self.geoendpoint = 'https://frost.met.no/sources/v0.jsonld'
        self.geoparameters = {'geometry': f'nearest(POINT({self.Lat} {self.Long}))'}
        # Issue an HTTP GET request
        self.s = requests.get(self.geoendpoint, self.geoparameters, auth=(self.client_id,''))
        # Extract JSON data
        self.geo_json = self.s.json()

        self.geo_json = self.s.json()
        self.loc_data = self.geo_json['data']
        self.loc_data = self.geo_json['data']
        self.loc_id = self.loc_data[0]['id']
        self.id_str = str(self.loc_id)
        self.parameters = {'sources': self.id_str,'elements': 'mean(air_temperature P1D)','referencetime': '2021-06-01/2022-08-01',}
        self.r = requests.get(self.endpoint, self.parameters, auth=(self.client_id,''))
        self.temp_json = self.r.json()
        self.temp_data = self.temp_json['data']
        self.meanTemp = self.temp_data[0]['observations'][0]['value']
        #print(self.meanTemp)

        self.degDiff = self.printTemp - self.meanTemp
        #self.sizeConstant = self.degDiff
        # https://llplastic.co.uk/llplastic-information plastic expantion coefficient 0.11 mm/m/C




    def returnTemp(self):
        """
        :return: The mean temperature of the last year.
        """
        return self.meanTemp

    def getPointsInner(self):
        """
        Description
        :return:
        Returns the list of the inner circle
        """
        return self.pointsInner

    def getPointsMain(self):
        """
        Description
        :return:
        Returns the list of the Main circle
        """
        return self.pointsMain

    def getPointsOuter(self):
        """
        Description
        :return:
        Returns the list of the Outer circle. x = getPointsOuterOffset[0], y = getPointsOuterOffset[1], z = getPointsOuterOffset[2]
        """
        return self.pointsMain
    def getPointsInnerOffset(self):
        """
        Description
        :return:
        Returns the list of the inner circle with ofset.
        """
        return self.pointsInnerOffset

    def getPointsMainOffset(self):
        """
        Description
        :return:
        Returns the list of the Main circle with ofset.
        """
        return self.pointsMainOffset

    def getPointsOuterOffset(self):
        """
        Description
        :return:
        Returns the list of the Outer circle with ofset. x = getPointsOuterOffset[0], y = getPointsOuterOffset[1], z = getPointsOuterOffset[2]
        """
        return self.pointsMainOffset



