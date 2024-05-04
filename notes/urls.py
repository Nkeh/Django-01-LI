from django.urls import path
from . import views

urlpatterns = [
    path('', views.noteList),
    path('<int:pk>/', views.noteDetail)
]

