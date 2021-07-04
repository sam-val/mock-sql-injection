from django.http.response import HttpResponse, HttpResponseRedirect
import requests, urllib
from django.shortcuts import redirect, render

import sys 


def csrf_attack(r):
    return render(r,"csrf_attack.html")


    
