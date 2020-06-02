from django.shortcuts import render
from . models import Post,PostSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def home(request):
	data=Post.objects.all()
	books = Post.objects.filter(title="test")
	serializer = PostSerializer(books, many=True)
	#Post(title="test",content="lorem ipsum ...........",date_posted="12/05/2020").save()
	#print("Stored in databse")
	return JsonResponse({"data":serializer.data})

@csrf_exempt
def about(request):
	return render(request, 'blog/about.html')


  