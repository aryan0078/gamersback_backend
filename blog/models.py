from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.TextField()
	



	def __str__(self):
		return self.title


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted']
