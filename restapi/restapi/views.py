# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from serializers import ServerSerializer
from models import Server
from GeoDistance.GeoDistance import GeoDistance


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'server': reverse('server-list', request=request, format=format),
        })


class ServerList(generics.ListCreateAPIView):
    '''
    List all servers
    '''
    serializer_class = ServerSerializer
    queryset = Server.objects.all()

    def get_queryset(self):
        if 'my_lat' in self.request.QUERY_PARAMS  and 'my_long' in self.request.QUERY_PARAMS:
            my_lat = self.request.QUERY_PARAMS['my_lat']
            my_long = self.request.QUERY_PARAMS['my_long']
            servers = Server.objects.all()
            distance_map = []
            for server in servers:
                distance = GeoDistance().computeDistance((my_lat, my_long), (server.latitute, server.longitude))
                print distance
                distance_map.append((server, distance))
            distance_map = sorted(distance_map, key=lambda dmap: dmap[1])
            return [d_map[0] for d_map in distance_map]
        else:
            return Server.objects.all()


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    give detailed view of a particular server
    '''
    serializer_class = ServerSerializer
    queryset = Server.objects.all()
