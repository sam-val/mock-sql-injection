from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Movie, MovieForm
from django.db import connection
import sqlite3
from django.db.utils import OperationalError
import subprocess
import html, sys, traceback
# Create your views here.
def index(r):
    form = MovieForm()
    movies = Movie.objects.all()
    try:
        return render(r, 'inject/index.html', {'movies':movies, "form": form})
    except OperationalError as e:
        movies = None
        return render(r, 'inject/index.html', {'movies':movies, "form": form, "gone":True})

    
def inject(r):
    name = r.POST['name']
    year = r.POST['year_released']
    # cursor = connection.cursor()
    query = "INSERT INTO sqlinject_movie(name,year_released) values('%s', '%s');" % (name, year)
    # query = html.unescape(query)

    try:
        db = sqlite3.connect('db.sqlite3')
        cursor = db.cursor()
        cursor.executescript(query)
        db.commit()
        db.close()
    except Exception as e:
        traceback.print_exc()

    return HttpResponseRedirect(reverse('inject:index'))

def regenerate_table(r):
    # run in the command-line:
    subprocess.run(['./manage.py', 'reset_db', '--noinput', '--close-sessions']) # reset db using the django_extensions module; it destroys the whole db
    subprocess.run(['./manage.py','migrate']) # apply all migrations 

    queries = "Movie.objects.create(name='Inception', year_released='2010')"
    queries += "\nMovie.objects.create(name='Interstellar', year_released='2014')"
    queries += "\nMovie.objects.create(name='Memento', year_released='2000')"
    
    subprocess.run(['./manage.py','shell_plus', '--quiet-load','-c', queries])
    # p.stdin.write(queries)
    # p.communicate()
    
    return HttpResponseRedirect(reverse('inject:index'))

