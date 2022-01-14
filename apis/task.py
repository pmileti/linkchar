from celery import shared_task
import requests
from .serializers import EntriesSerializer


@shared_task
def my_task():
	url='https://api.publicapis.org/entries'
	data=requests.get(url)
	json=data.json()
	entries=json['entries']
	for x in entries:
		serializer = EntriesSerializer(data=x)
		if serializer.is_valid():
			serializer.save()
