"""
URL configuration for mercadona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from django.views.defaults import server_error
from .views import vue_de_test
from .views import index
from .views import profile

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', index, name = "index"),
    path('admuser/', include("admuser.urls")),
    path('index.html', index, name = "index2"),
  # path('login.html', login, name = "login"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/profile/', profile),
 #   path('pgadmin4/', views.pgadmin4),
    path('error/',server_error),
    path('test/',vue_de_test)
    ]
