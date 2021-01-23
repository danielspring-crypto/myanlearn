
from django.shortcuts import render
from rest_framework import generics
from courses.models import Course
from .serializers import NewCourseSerializer


class NewCourseAPIView(generics.ListCreateAPIView):
	queryset = Course.objects.all()
	serializer_class = NewCourseSerializer