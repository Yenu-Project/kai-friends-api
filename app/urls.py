from django.urls import path, include
from rest_framework.routers import DefaultRouter

import app.views.user
from app import views

# create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'users', app.views.user.UserViewSet)

# the API URLs are now determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls))
]
