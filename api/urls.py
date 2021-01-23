from .views import NewCourseAPIView
from django.urls import path

urlpatterns = [
	path('new-courses/', NewCourseAPIView.as_view()),
]