from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import Entries
from .serializers import EntriesSerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from .task import my_task


#endpoint /populate-apis 
@api_view(['GET', 'POST'])
def populate_apis(request):
    if request.method == 'POST':
    	my_task.delay()
    	return JsonResponse({'Info': 'Tarea realizandose, puede continuar haciendo uso del resto de los endpoints mientras.'}, status=status.HTTP_201_CREATED)    		

    elif request.method == 'GET':
    	raise Http404
        


#endpoint /keyword
@api_view(['GET', 'POST'])
def keyword(request):
    if request.method == 'GET':
    	raise Http404
        
    elif request.method == 'POST':
        if "keyword" in request.data:
        	value=request.data['keyword']
        	entries = Entries.objects.filter(API__startswith=value)
        	entries_serializer = EntriesSerializer(entries, many=True)
        	return JsonResponse(entries_serializer.data, safe=False)
        else:
        	raise Http404

#endpoint /category
@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
    	raise Http404
        
    elif request.method == 'POST':
        if "category" in request.data:
        	value=request.data['category']
        	entries = Entries.objects.filter(Category=value)
        	entries_serializer = EntriesSerializer(entries, many=True)
        	return JsonResponse(entries_serializer.data, safe=False)
        else:
        	raise Http404

#endpoint /ordered-list
@api_view(['GET', 'POST'])
def ordered_list(request):
    if request.method == 'POST':
        entries = Entries.objects.all().order_by('id')
        entries_serializer = EntriesSerializer(entries, many=True)
        return JsonResponse(entries_serializer.data, safe=False)
 
    elif request.method == 'GET':
    	raise Http404    


#endpoint /item 
@api_view(['GET', 'POST'])
def item(request):
    if request.method == 'POST':
        if "pk" in request.data:
        	value=request.data['pk']
        	try: 
        		entries = Entries.objects.get(id=value)
        		entries_serializer = EntriesSerializer(entries) 
        		return JsonResponse(entries_serializer.data) 
  
        	except Entries.DoesNotExist: 
        		return JsonResponse({'Error': 'Ese item no existe'}, status=status.HTTP_404_NOT_FOUND) 

    elif request.method == 'GET':
    	raise Http404
        
