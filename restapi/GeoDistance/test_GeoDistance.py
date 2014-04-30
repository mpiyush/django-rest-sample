'''
Created on Apr 28, 2014

@author: Piyush Mittal
'''
from GeoDistance import GeoDistance
import unittest


class test_GeoDistance(unittest.TestCase):
    '''
    tests the implemenation of GeoDistance class
    '''

    def test_distanceValue1(self):
        '''
        Validate a value with refernce to http://www.movable-type.co.uk/scripts/latlong.html
        '''
        cord1 = (0, 0)
        cord2 = (20, 20)
        output = GeoDistance().computeDistance(cord1, cord2)
        expected_output = 3116.0
        msg = 'Input = %s, Expected Output = %s, Output = %s' % ((cord1, cord2), expected_output, output)
        self.assertEqual(output, expected_output, msg)

    def test_distanceValue2(self):
        '''
        Same coordinates should return 0
        '''
        cord1 = cord2 = (20, 20)
        output = GeoDistance().computeDistance(cord1, cord2)
        expected_output = 0.0
        msg = 'Input = %s, Expected Output = %s, Output = %s' % ((cord1, cord2), expected_output, output)
        self.assertEqual(output, expected_output, msg)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_Name']
    unittest.main()
