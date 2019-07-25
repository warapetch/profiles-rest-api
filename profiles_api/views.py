#from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import my_serializers     #2.0
from rest_framework import status           #2.0
from django.http import HttpResponse        #X.0

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = my_serializers.HelloSerializer  #2.1

    def get(self, request, format=None):            #1
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):        #2.2
        """Create a hello message with our name"""
        Lserializer = self.serializer_class(data=request.data)

        if Lserializer.is_valid():
            name = Lserializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            content = {'Error':'ชื่อยาวเกินไป'}
            return Response(
                Lserializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):  #3.1
        """ Handle updating an object """

        return Response({'method':'PUT'})

    def patch(self,request,pk=None): #3.1
        """ Handle partial update of an object """

        return Response({'method':'PATCH'})

    def delete(self,request,pk=None): #3.1
        """ Delete an object """

        return Response({'method':'DELETE'})


class Home(APIView):            #X.1
    """ สร้าง Base view for my site """

    def index(request):
        return HttpResponse("<h1>สวัสดี การ์ตูน ♥ Web Server ทำงานได้แล้ว</h1>")
