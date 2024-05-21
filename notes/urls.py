from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name="notes.list"),
    path('<int:pk>/', views.NotesDetailView.as_view(), name="notes.detail"),
    path('new/', views.NotesCreateView.as_view(), name="notes.new"),
    path('<int:pk>/delete/', views.NotesDeleteView.as_view(), name="notes.delete"),
    path("<int:pk>/edit/", views.NotesUpdateView.as_view(), name="notes.update")

]

