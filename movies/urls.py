from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('now-showing/', views.now_showing, name='now_showing'),
    path('details/', views.details, name='details'),
    path('login/', views.login_view, name='login'),
    path('theatres/', views.theatres, name='theatres'),
]