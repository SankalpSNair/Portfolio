from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('messages/', views.MessageListView.as_view(), name='messages'),
]
