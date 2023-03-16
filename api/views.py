import requests
from django.shortcuts import HttpResponse

from .models import TechnicalPath, Field


def import_technical_paths(request):
    field_id = 'cbf7bb1d-c5b1-4dfa-83d2-5800f78ffb8d'
    url = f'https://mocki.io/v1/{field_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data['values']:
            id = item['id']
            name = item['name']
            heading = item['heading']
            last_modified_time = item['lastModifiedTime']
            archived = item['archived']
            a_lat = item['aPoint']['lat']
            a_lon = item['aPoint']['lon']
            b_lat = item['bPoint']['lat']
            b_lon = item['bPoint']['lon']
            field = Field(id=field_id)
            field.save()
            technical_path = TechnicalPath(id=id, name=name, last_modified_time=last_modified_time, archived=archived,
                                           heading=heading, a_lat=a_lat, a_lon=a_lon, b_lat=b_lat, b_lon=b_lon, field_id=field_id)
            technical_path.save()
        return HttpResponse('Data imported successfully')
    else:
        return HttpResponse('Error importing data')
