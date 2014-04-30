'''
Created on Apr 29, 2014

@author: Piyush Mittal
'''
import unittest
import requests
import json
SERVER = 'http://127.0.0.1:8000/server/'


class test_RESTAPI(unittest.TestCase):
    '''
    Tests the rest api using http calls
    '''

    def test_ServerReachable(self):
        try:
            response = requests.get(SERVER)
            server_reachable = True
        except Exception:
            server_reachable = False
        self.assertTrue(server_reachable, "Couldn't reach server")

    def test_Create(self):
        payload = {'name': 'test1', 'latitute': '80', 'longitude': '80'}
        response = requests.post(SERVER, payload)
        self.assertEqual(response.status_code, 201, "Response code should have been 201")

    def test_Delete(self):
        url = SERVER + '1/'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, "Response code should have been 200")

        response = requests.delete(url)
        response = requests.get(url)
        self.assertEqual(response.status_code, 404, "Response code should have been 404")

    def test_findDistanceSorted(self):
        payload = {'my_lat': '100', 'my_long': '80'}
        response = requests.get(SERVER, params=payload)
        expected_output = [{u'url': u'http://127.0.0.1:8000/server/3/', u'latitute': u'100', u'name': u'TestServer3', u'longitude': u'80'},
                           {u'url': u'http://127.0.0.1:8000/server/2/', u'latitute': u'90.214', u'name': u'TestServer2', u'longitude': u'80.145'},
                           {u'url': u'http://127.0.0.1:8000/server/4/', u'latitute': u'80', u'name': u'test1', u'longitude': u'80'}]
        response.encoding = 'utf-8'
        output = json.loads(response.text)
        self.assertEquals(expected_output, output, "Given this database, the expected output doesnt match the expected input")


if __name__ == '__main__':
    unittest.main()
