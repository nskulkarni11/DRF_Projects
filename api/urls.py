from django.urls import path,re_path
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MyUser API Urls')

urlpatterns = [
    re_path(r'^$', schema_view),
    path('api/users/',views.MyUserCreateView.as_view(),name='post'),
    path('api/users/<int:pk>/',views.MyCustomUserView.as_view(), name='retrieve'),
 


]
