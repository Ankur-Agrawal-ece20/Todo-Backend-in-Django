"""APIProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views

#  for viewsets(routers)
from .views  import ArticleViewSet
from rest_framework.routers import DefaultRouter

#  for authentication
from .views import UserViewSet

'''Router automatically maps the incoming request to proper viewset action based on the request method type(i.e GET, POST, etc).'''
router =DefaultRouter()
router.register(r'articles',ArticleViewSet,basename='articles')
# router.register(r'users',UserViewSet,basename='articles')

urlpatterns = [
    # path('',views.Index,name='index'),

    #  for serialization, deserialization
    path('new',views.new,name='apirequest1'),
    path('new1',views.new1,name='apireqsuest2'),

    #  for function based  views
    # path('articles/',views.article_list,name='articles'),
    # path('articles/<int:id>/',views.article_details,name='article_details'),

    #  for class based views
    # path('articles/',views.ArticleList.as_view(),name='articles'),
    # path('articles/<int:id>/',views.ArticleDetails.as_view(),name='article_details'),

    #  for routers
    path('api/',include(router.urls)),
]
