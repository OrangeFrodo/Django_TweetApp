import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

def home_view(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    print(request.user or None)
    return render(request, "pages/home.html", context={"username": username}, status=200)

def tweets_list_view(request, *args, **kwargs):
    return render(request, "News/list.html")

def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "News/detail.html", context={"tweet_id": tweet_id})
