#from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status           #2.0
from rest_framework import viewsets         #4.0
from rest_framework.authentication import TokenAuthentication #6.0
from rest_framework import filters          #7.0

from profiles_api import my_serializers     #2.0
from profiles_api import my_permissions     #6.0
from profiles_api import models             #5.0
from django.http import HttpResponse        #X.0


# HelloApiView
# ---------------------------------------------
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

# HelloViewSet
# ---------------------------------------------
class HelloViewSet(viewsets.ViewSet):   #4.1
    """ Test API ViewSet """
    serializer_class = my_serializers.HelloSerializer  #4.1

    def list(self,resuest):
        """ Resturn a Hello Message """
        a_viewset = [
            'Uses actions (list, create, retrievv, update, partial_update)',
            'Atomatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello','a_viewset':a_viewset})

    def create(self, request):
        """ Create a new hello message """
        Lserializer = self.serializer_class(data=request.data)
        if Lserializer.is_valid():
            name = Lserializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                Lserializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def retrieve(self,reuest,pk=None):      #4.2
        """ Handle getting an object by its ID """
        return Response({'http_method' : 'GET'})

    def update(self,reuest,pk=None):
        """ Handle Updating part of  an object """
        """ อัพเดตทั้งหมด เงื่อนไขเหมือนตอนเพิ่มข้อมูล """
        return Response({'http_method' : 'PUT'})

    def partial_update(self,reuest,pk=None):
        """ Handle Updating part of  an object """
        """ อัพเดตบางฟิลด์ หรือ ทั้งหมดก็ได้ """
        return Response({'http_method' : 'PATCH'})

    def destroy(self,reuest,pk=None):
        """ Handle Removing an object """
        return Response({'http_method' : 'DELETE'})


# UserProfileViewSet
# ---------------------------------------------
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = my_serializers.UserProfileSerializer     #5
    queryset = models.UserProfile.objects.all()                 #5
    authentication_classes = (TokenAuthentication,)             #6
    permission_classes = (my_permissions.UpdateOwnProfile,)     #6
    filter_backends = (filters.SearchFilter,)                   #7
    search_fields = ('name','email',)                           #7

# ---------------------------------------------
# Home
# ---------------------------------------------
class Home(APIView):            #X.1
    """ สร้าง Home page for my site """

    def index(request):
        return HttpResponse("<h1>สวัสดี Django Web Server ทำงานได้แล้ว</h1>")
