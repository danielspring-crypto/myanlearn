
from django.urls import path

from recommend import views

urlpatterns = [
    path('', views.HistoryList.as_view(), name='history'),
]