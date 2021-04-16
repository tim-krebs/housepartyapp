from django.urls import path
from .views import AuthURL

urlpatterns = [
    path('get-auth', AuthURL.as_view()),
]
