# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    context = {
        "date": strftime("%B %d, %Y"),
        "time": strftime("%I:%M %p"),
    }
    return render(request, 'time_display/index.html', context)
