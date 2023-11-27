from rest_framework import viewsets
from APP.mimir.serializers import  GroupSerializer
from APP.mimir.models import pttdata
from rest_framework import generics
import django_filters.rest_framework
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page"
class PostViewSet(viewsets.ModelViewSet):
    pagination_class = StandardPagination
class GroupViewSet(viewsets.ModelViewSet):
    lookup_url_kwarg = "title"
    serializer_class = GroupSerializer
    def get_queryset(self):
        queryset = pttdata.objects.all()
        username = self.request.query_params.get('title', None)
        if username is not None:
            queryset = queryset.filter(title__contains=str(username))
            return queryset
    
# class GroupViewSet(viewsets.ModelViewSet):
#     serializer_class = GroupSerializer
#     def get_queryset(self):
#         queryset = pttdata.objects.all()
#         return queryset

# class GroupViewSet(viewsets.ModelViewSet):
#     lookup_url_kwarg = "title"
#     serializer_class = GroupSerializer
#     def get_queryset(self):
#             queryset = pttdata.objects.all()
#             username = self.request.query_params.get('title', None)
#             date= self.request.query_params.get('date', None)
#             if username is not None:
#                         queryset = queryset.filter(title__contains=str(username)) 
#                         queryset = queryset.filter(date__contains=str(date))
#             return queryset