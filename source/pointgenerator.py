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
        # [innerDiameter, outerDiameter, thickness, nuberOfTeeth,teethheight, printTemperature [C],  locationLat, locationLong]
        self.cirkInner = list[0]
        self.cirkOuter = list[1]
        self.thickness = list[2]
        self.numberOfTeeth = list[3]
        self.teethHeiht = list[4]
        self.printTemp = list[5]
        self.Lat = list[6]  #Input from User interface, Need some restrictions
        self.Long = list[7] #Input from User interface, Need some restrictions

        self.cirkMain = self.cirkOuter - 2*self.teethHeiht
        self.theta = np.linspace(0, 2*np.pi, self.numberOfTeeth)
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
        self.zInner = 0
    def generatingMainCircle(self):
         # make a simple unit circle
        self.xMain, self.yMain = self.cirkMain/2 * np.cos(self.theta), self.cirkMain/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle
        self.zMain = 0
    def generatingOuterCircle(self):
        # make a simple unit circle shiftet one halv tooth
        self.xOuter, self.yOuter = self.cirkOuter/2 * np.cos(self.thetaShifted), self.cirkOuter/2 * np.sin(self.thetaShifted) #x,y are coordinates for the inner cirkle
        self.zOuter = 0

    def offsetPoints(self):
        #makes the offset plane to give the gear a thickness
        self.xInnerOffset = self.xInner
        self.yInnerOffset = self.yInner
        self.zInnerOffset = self.zInner + self.thickness

        self.xMainOffset = self.xMain
        self.yMainOffset  = self.yMain
        self.zMainOffset  = self.zMain + self.thickness

        self.xOuterOffset = self.xOuter
        self.yOuterOffset = self.yOuter
        self.zOuterOffset = self.zOuter + self.thickness

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
        return self.meanTemp
