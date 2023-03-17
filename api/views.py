import requests
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, View, DetailView, TemplateView

from .models import TechnicalPath, Field

class HomePage(TemplateView):
    template_name = 'home.html'

class ImportData(View):
    def get(self, request, *args, **kwargs):
        field_id = 'cbf7bb1d-c5b1-4dfa-83d2-5800f78ffb8d'
        url = f'https://mocki.io/v1/{field_id}'
        response = requests.get(url)

        if response.status_code != 200:
            messages.add_message(request, messages.ERROR, 'Failed to import data!')
            return redirect('home-page')

        field = Field(id=field_id)
        field.save()
        data = response.json()
        for item in data['values']:
            technical_path = TechnicalPath(
                id=item['id'],
                name=item['name'],
                last_modified_time=item['lastModifiedTime'],
                archived=item['archived'],
                heading=item['heading'],
                a_lat=item['aPoint']['lat'],
                a_lon=item['aPoint']['lon'],
                b_lat=item['bPoint']['lat'],
                b_lon=item['bPoint']['lon'],
                field_id=field_id
            )
            technical_path.save()

        messages.add_message(request, messages.INFO, 'Data imported!')
        return redirect('home-page')


class PathView(ListView):
    model = TechnicalPath
    template_name = 'technical_path_list.html'


class FieldListView(ListView):
    model = Field
    template_name = 'fields_list.html'


class FieldDetailsView(DetailView):
    model = Field
    template_name = 'field_details.html'
