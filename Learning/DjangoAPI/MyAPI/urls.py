from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'MyAPI'
router = routers.DefaultRouter()
routers.register('MyAPI', views.ApprovalsView)

urlpatterns = [
    path('form/', views.myform, name = 'myform'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]
