from django.urls import path
from rango import views
from django.conf.urls import url

app_name = 'rango'

urlpatterns = [
    path('/', views.index, name= 'index'),
    path('/about/', views.about, name='about'),
]

