"""django_intro URL Configuration

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
from pages import views
urlpatterns = [
    path('num/pull/',views.num_pull),
    path('num/push/', views.num_push),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/',views.throw),
    path('lotto/', views.lotto),
    path('pal/<word>/', views.pal),
    path('isbirth/',views.isbirth),
    path('hello/<str:name>/<int:age>', views.hello),
    path('admin/', admin.site.urls),
    path('myself/<str:name>/<int:age>',views.myself),
    path('mul/<int:num1>/<int:num2>',views.mul),
    path('circle/<int:r>',views.circle),
    path('template_language/',views.template_language),
]
