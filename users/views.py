from django.shortcuts import render
from django.contrib import messages
from . models import Usersdata,AboutEvents,Teamreg
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .sereializer import TeamregSerializer,AboutEventsSerializer,UsersdataSerializer
@csrf_exempt
@api_view(['POST'])
def register(request):
	s=UsersdataSerializer(data=request.data)
	if s.is_valid():
		s.save()
		return Response(s.data)
	return Response({"msg":"Already registered"})
@csrf_exempt
@api_view(['POST'])
def login(request):
	try:
		s=Usersdata.objects.get(email=request.data['email'])
		ser=UsersdataSerializer(s,many=False)
		if ser.data["password"]==request.data['password'] and ser.data['email']==request.data['email']:
			return Response(ser.data)
		return JsonResponse({"msg":"Username or password is incorrect"})
	except:
		return JsonResponse({"msg":"Username or password is incorrect"})

			
@csrf_exempt
@api_view(['POST'])
def aboutevent(request):
	#AboutEvents(registerenddate="17/4/2020",description="dgsrgaargasrgagrcwgw wctwq4tcqwctwqtcwtcwtcwctatvw4tvaw4tvaw4vtawtvaw4tvawtvawvtavw vw4tcawvt",currentseats=232,avilseats=250,firstprice="100000",secondprice="50000",thirdprice="5",rules="1.just dont kill your self 2.dont act oversmart",shedule="12/5/2020",teams="1.alpha 2.bravo 3.gaama 4.beta",watchnow="https://www.youtube.com").save()
	return Response({"details":"done"})
@csrf_exempt
@api_view(['POST'])
def teamreg(request):
	s=TeamregSerializer(data=request.data)
	if s.is_valid():
		s.save()
		return Response({"msg":"Registration Done"})
	return Response({"msg":"Already registered"})
		
@csrf_exempt
@api_view(['POST'])
def checkemail(request):
	email=request.data['email']
	try:
		s=Usersdata.objects.get(email=email)
		ser=UsersdataSerializer(s,many=False)
		return JsonResponse({"registered":"true"})
	except:
		return JsonResponse({"registered":"false"})
	
@csrf_exempt
@api_view(['POST'])
def payment(request):
	#yha pr insta mojo link hoga
	return JsonResponse({"msg":"this is instamojo part"})
	








