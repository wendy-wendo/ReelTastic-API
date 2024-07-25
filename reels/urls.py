from django.urls import path
from . import views

app_name = 'reels'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.reelsList, name='reelsList'),
    path('create/', views.reelCreate, name='reelCreate'),
    path('update/<str:pk>/', views.reelUpdate, name='reelUpdate'),
]
