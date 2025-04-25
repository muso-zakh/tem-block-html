from django.urls import path
from .views import home, history, frem, libraries, Documentation


urlpatterns = [
    path('', home, name='home'),
    path('py_history', history, name='history'),
    path('py_frem', frem, name='frem'),
    path('py_lib', libraries, name='lib'),
    path('py_doc', Documentation, name='doc'),
] 