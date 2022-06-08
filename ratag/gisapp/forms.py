from django.contrib.gis import forms
from .models import Hazard


class NewHazard(forms.ModelForm):

    class Meta:
        model = Hazard
        fields = '__all__'

        widgets = {
            'point': forms.OSMWidget(attrs={'default_lat': 32, 'default_lon': 35, 'map_width': 800, 'map_height': 500}),
            'created_time': forms.SelectDateWidget()
        }
