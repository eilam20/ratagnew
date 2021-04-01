from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import *
from .forms import *
import urllib.request, json 
from django.contrib.gis.geos import Polygon
from django.shortcuts import redirect
from django.core.serializers import serialize


# Create your views here.


class Sites_list(ListView):
    model = Site
    template_name = 'gisapp/sites_list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.objects.all()

class Site_detail(DetailView):
    model = Site
    template_name = 'gisapp/site_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['geojson'] = self.object.Polygon.geojson
        context['Hazards'] = serialize('geojson',  Hazard.objects.filter(point__intersects=self.object.Polygon),
          geometry_field='point',
          fields=('title','created_time'))
        
        
        return context


class Hazard_detail(DetailView):

    model = Hazard
    template_name = 'gisapp/hazard_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.filter(Polygon__contains=self.object.point)  

        print(context['sites'])
        return context




class Create_Hazard(CreateView):
    model = Hazard
    form_class = NewHazard
    template_name = 'gisapp/create_hazard.html'



def load_sites(self):
    with urllib.request.urlopen("https://gist.githubusercontent.com/ekeydar/60fb52013bee62f0ed66b4bdfbd1bfa0/raw/a7ae162fbfb0202cb3040e977aab62f15df44ac1/sites.json") as url:
        data = json.loads(url.read().decode())
        for poly in data:
            title= poly['title']
            poly = Polygon( poly['points'])

            new_site = Site(title=title, Polygon=poly)
            new_site.save()
    return redirect('gisapp:Sites_list')

        


