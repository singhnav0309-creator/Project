"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from SatShriAkalWorld.views import SatShriAkalWorldView
from rest_framework import routers
from SatShriAkalWorld.views import PostView
from SatShriAkalWorld.serializers import PostSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Sat Shri Akal/' , SatShriAkalWorldView.as_view()),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]

router = routers.DefaultRouter()
router.register('posts', PostView, 'posts')

urlpatterns += router.urls

