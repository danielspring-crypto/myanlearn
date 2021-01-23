from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import History

class HistoryList(ListView):
    def get_queryset(self):
        user_history = History.objects.all()
        return user_history