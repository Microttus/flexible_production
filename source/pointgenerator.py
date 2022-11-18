'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
27.10.2022

source: https://gis.stackexchange.com/questions/411113/generate-a-circle-of-coordinates-around-a-point-but-im-getting-an-oval
is used to get inspiration on how to make the circle patterned points.
'''

import numpy as np
import requests


class PointGenerator:
    def __init__(self):

        self.cirkInner = 0
        self.cirkOuter = 0
        self.teethHeiht = 0
        self.gearHeight = 0
        self.numberOfTeeth = 0
        self.printTemp = 0
        self.meanTemp = 0
        self.Lat = 0
        self.Long = 0

        self.pointsInner = []
        self.pointsOuter = []
        self.pointsMain = []
        self.pointsInnerOffset = []
        self.pointsOuterOffset = []
        self.pointsMainOffset = []

    def inputList(self, list):
        '''
        :param list: List with all the inputs from the user interface
        :return: list of all points in the circle
        '''
        #self.specificationList = list
        # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
        self.cirkInner = list[0]
        self.cirkOuter = list[1]
        self.teethHeiht = list[2]
        self.gearHeight = list[3]
        self.numberOfTeeth = list[4]
        self.printTemp = list[5]
        self.meanTemp = []
        self.Lat = list[6]  #Input from User interface, Need some restrictions
        self.Long = list[7] #Input from User interface, Need some restrictions

        self.cirkMain = self.cirkOuter - 2*self.teethHeiht
        self.theta = np.linspace(0, 2*np.pi, int(self.numberOfTeeth))
        self.thetaShifted = self.theta + self.theta[1]/2



    def generatingInnerCircle(self):
        '''
        :return: Generates the points of the inner lower circle
        '''
        # make a simple unit circle with teeth number of points
        self.xInner, self.yInner = self.cirkInner/2 * np.cos(self.theta), self.cirkInner/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle
        self.zInner = np.zeros(int(self.numberOfTeeth))
        self.pointsInner = [self.xInner, self.yInner, self.zInner]
        self.pointsInner = [value*self.multiplyingFactor for value in self.pointsInner] #Multiplies list by the sizing factor
        self.pointsInner = np.array(self.pointsInner).T
    def generatingMainCircle(self):
        '''
        :return:   Generates the points of the main lower circle
        '''
         # make a simple unit circle
        self.xMain, self.yMain = self.cirkMain/2 * np.cos(self.theta), self.cirkMain/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle
        self.zMain = np.zeros(int(self.numberOfTeeth))
        self.pointsMain = [self.xMain, self.yMain, self.zMain]
        self.pointsMain = [value*self.multiplyingFactor for value in self.pointsMain] #Multiplies list by the sizing factor
        self.pointsMain = np.array(self.pointsMain).T

    def generatingOuterCircle(self):
        '''###### GearGenerator 1.0 ######

Authors:
Torbjørn Halvorsen
Per Henrik Hardeberg
Martin Økter

Instructions:
For running the program, download all files and run in a python 3.4
environment or newer. A list of nessesary packages can be found here:

Nessesary Packages:
matplotlib==3.6.2
numpy==1.23.4
pygame==2.1.2
requests==2.28.1
scipy==1.9.3
stl==0.0.3
numpy.stl== 2.17.1

        :return: Generates the points of the outer lower circle
        '''
        # make a simple unit circle shiftet one halv tooth
        self.xOuter, self.yOuter = self.cirkOuter/2 * np.cos(self.thetaShifted), self.cirkOuter/2 * np.sin(self.thetaShifted) #x,y are coordinates for the inner cirkle
        self.zOuter = np.zeros(int(self.numberOfTeeth))
        self.pointsOuter = [self.xOuter, self.yOuter, self.zOuter]
        self.pointsOuter = [value*self.multiplyingFactor for value in self.pointsOuter] #Multiplies list by the sizing factor
        self.pointsOuter = np.array(self.pointsOuter).T

    def offsetPoints(self):
        '''
        :return: Reproduce the points from above but shifts them in the z-direction
        '''
        #makes the offset plane to give the gear a thickness
        self.xInnerOffset = self.xInner
        self.yInnerOffset = self.yInner
        self.zInnerOffset = self.zInner + self.gearHeight
        self.pointsInnerOffset = [self.xInnerOffset, self.yInnerOffset, self.zInnerOffset]
        self.pointsInnerOffset = [value*self.multiplyingFactor for value in self.pointsInnerOffset] #Multiplies list by the sizing factor
        self.pointsInnerOffset = np.array(self.pointsInnerOffset).T

        self.xMainOffset = self.xMain
        self.yMainOffset  = self.yMain
        self.zMainOffset  = self.zMain + self.gearHeight
        self.pointsMainOffset = [self.xMainOffset, self.yMainOffset, self.zMainOffset]
        self.pointsMainOffset = [value*self.multiplyingFactor for value in self.pointsMainOffset]
        self.pointsMainOffset = np.array(self.pointsMainOffset).T

        self.xOuterOffset = self.xOuter
        self.yOuterOffset = self.yOuter
        self.zOuterOffset = self.zOuter + self.gearHeight
        self.pointsOuterOffset = [self.xOuterOffset, self.yOuterOffset, self.zOuterOffset]
        self.pointsOuterOffset = [value*self.multiplyingFactor for value in self.pointsOuterOffset] #Multiplies list by the sizing factor
        self.pointsOuterOffset = np.array(self.pointsOuterOffset).T

    def temperatureSizing(self):
        '''
        :return: Calculates the mean temperature from the last year and use this to size the gear. In other
        words: If the gear is printed in high temperature and needs to be used in cold environment, the STL of the gear needs to be bigger
        than the given size to shrink and fit for the environment. From the given long and lat the location is found and used to calculate the factor.
        '''

        '''Referanse:
                This code was originaly inspired by Frosts wather API example code, which is used to gather weather data and used in the sizing of the gears.
                https://frost.met.no/python_example.html
                '''
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
        self.loc_id = self.loc_data[0]['id']
        self.name = self.loc_data[0]['name']
        self.id_str = str(self.loc_id)
        self.parameters = {'sources': self.id_str,'elements': 'mean(air_temperature P1D)','referencetime': '2021-06-01/2022-08-01',}
        self.r = requests.get(self.endpoint, self.parameters, auth=(self.client_id,''))
        self.temp_json = self.r.json()
        self.temp_data = self.temp_json['data']
        lenght = len(self.temp_data)
        allTemp = []

        for i in range(0, lenght):
            Temp = (self.temp_data[i]['observations'][0]['value'])
            allTemp.append(Temp)
        self.meanTemp = np.mean(allTemp)
        print('mean temp at :', self.name, 'is :', self.meanTemp, 'celcius')

        #Change the size of the gear:
        degDiff = self.printTemp - self.meanTemp
        sizeCoef = 0.11 # https://llplastic.co.uk/llplastic-information plastic expantion coefficient 0.11 mm/m/C
        self.prosChange = sizeCoef/1000* degDiff*100 #Prosent change after temperetur added
        self.multiplyingFactor = 1 + self.prosChange/100

        print('DegDiff')
        print(degDiff)
        print('prosChange')
        print(self.prosChange)
        print('Multiplying factor')
        print(self.multiplyingFactor)


    def returnSizeChangeProsent(self):
        """
        :return: Change in prosent with 1 desimal, due to temperature.
        """
        return (round(self.prosChange,1))



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
        return self.pointsOuter
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
        return self.pointsOuterOffset



