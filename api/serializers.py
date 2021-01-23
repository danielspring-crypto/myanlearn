from rest_framework import serializers
from courses.models import Course
class NewCourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course		
		fields = ['subject','title','owner',]