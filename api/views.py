from .models import MyUser
from .serializers import MyUserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.schemas.openapi import SchemaGenerator

class MyPaginationView(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'limit'

class MyUserCreateView(generics.ListCreateAPIView):
    queryset = MyUser.objects.all().order_by('age')
    serializer_class = MyUserSerializer
    pagination_class = MyPaginationView
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['first_name','last_name']
    ordering_fields= ['age']

class MyCustomUserView(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        myuser = self.get_object(pk)
        serializer = MyUserSerializer(myuser)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        myuser = self.get_object(pk)
        serializer = MyUserSerializer(myuser, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        myuser = self.get_object(pk)
        myuser.delete()
        myuser = {}
        return Response(data=myuser,status=status.HTTP_200_OK)

