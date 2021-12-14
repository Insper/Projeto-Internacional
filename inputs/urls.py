from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('timetables', views.telaVisualizacao, name='timetables'),
]