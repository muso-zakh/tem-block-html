from .views import home, infos
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('infos/<int:pk>/', infos, name='info')
]