from django.urls import path, include

from app.views import router

urlpatterns = [
    path('api/', include(router.urls))
]
