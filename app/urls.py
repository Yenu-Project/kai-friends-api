from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from app import views

urlpatterns = [
    path('userprofiles/', views.UserProfileList.as_view()),
    path('userprofiles/<int:pk>/', views.UserProfileDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
