from django.db import models
from django.db.models.fields import CharField, DateField
from django import forms
from datetime import date
# Create your models here.

this_year = date.today().year
CHOICES = [(this_year-x,this_year-x) for x in range(100)]

class Movie(models.Model):
    name = CharField(max_length=255, null=False, blank=False) 
    director = CharField(max_length=50, null=True, blank=True)
    year_released = CharField(max_length=4,null=True,blank=True)

    def __str__(self):
        return f"{self.name} ({self.year_released})"


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year_released']
        widgets = {
            "year_released" : forms.Select(choices=CHOICES),
            "name": forms.TextInput(attrs={'size':30})
        }
    
