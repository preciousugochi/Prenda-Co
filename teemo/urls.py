from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('static', views.static, name= 'static'),
    path('register', views.register, name='register'),
    path('login', views.login, name= 'login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
]