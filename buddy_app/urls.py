from django.urls import path
from .views import PetCreateView, PetListView, PetDetailView, PetUpdateView, PetDestroyView

urlpatterns = [
    path('', PetListView.as_view()),
    path('create/', PetCreateView.as_view()),
    path('<int:pk>/', PetDetailView.as_view()),
    path('<int:pk>/update/', PetUpdateView.as_view()),
    path('<int:pk>/delete/', PetDestroyView.as_view()),
]
