from django.urls import path
from . import views

app_name='inject'

urlpatterns = [
   path('',views.index, name='index'), 
   path('inject/', views.inject, name='inject'),
   path('regenerate/', views.regenerate_table, name='regenerate'),
]