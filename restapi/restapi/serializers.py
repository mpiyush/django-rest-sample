'''
Created on Apr 28, 2014

@author: Piyush Mittal
'''

from rest_framework import serializers
from models import Server


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializes the data from Server class
    '''
    class Meta:
        model = Server
