# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Main page with form
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'surveys/index.html')

# Processes form submission
def process(request):
    request.session['counter'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

# Renders the submitted information
def result(request):
    return render(request, 'surveys/result.html')

# Resets the session counter
def reset(request):
    request.session['counter'] = 0
    return redirect('/')