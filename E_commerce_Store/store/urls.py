from django.urls import path

from . import views
from .views import HomeView

urlpatterns = [

    # path('', views.home, name='home'),  # Home page

    path('', HomeView.as_view(), name='home'),  # Home page using class-based view
]