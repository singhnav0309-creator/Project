from django.urls import path
from User.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('User/', UserListCreateAPIView.as_view()),
    path('User/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
]