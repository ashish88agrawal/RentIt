from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django import forms
from django.template import RequestContext


def login(request):
		return render(request, 'seller/login_full.html')
