"""finello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import project.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project.views.home, name='home'),
    path('local/', project.views.local, name='local'),
    path('international/', project.views.international, name='international'),
    path('resource/', project.views.resource, name='resource'),
    path('fund/', project.views.fund, name='fund'),
    path('trends/', project.views.trends, name='trends'),
    path('test/', project.views.test, name='test'),
    path('bench/<str:selected_ticker>', project.views.bench, name='bench')
    
]
