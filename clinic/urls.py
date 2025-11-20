from django.urls import path
from . import views

app_name = 'clinic'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('pet/<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('pet/<int:pet_id>/appointment/', views.book_appointment, name='book_appointment'),
]
