'''
Created on Apr 28, 2014

@author: Piyush Mittal
'''
from math import sin, cos, sqrt, atan2, radians
Radius_Of_Earth = 6378.1


class GeoDistance(object):
    '''
    Hold various functions which help with geography of earth
     * Computes geographical distance between two coordinates
    '''

    def computeDistance(self, cord1, cord2):
        '''
        Computes geographical distance between two coordinates
        Using: Haversine formula
        http://www.movable-type.co.uk/scripts/latlong.html
        '''
        lat_1 = radians(float(cord1[0]))
        lon_1 = radians(float(cord1[1]))
        lat_2 = radians(float(cord2[0]))
        lon_2 = radians(float(cord2[1]))

        del_lon = lon_2 - lon_1
        del_lat = lat_2 - lat_1
        a = (sin(del_lat / 2)) ** 2 + cos(lat_1) * cos(lat_2) * (sin(del_lon / 2)) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = round(Radius_Of_Earth * c,)
        return distance


