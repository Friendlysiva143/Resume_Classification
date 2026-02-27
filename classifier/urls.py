from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.upload_resume, name='upload_resume'),
]