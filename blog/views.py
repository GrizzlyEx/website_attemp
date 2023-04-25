from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})
# Create your views here.


def misha(request):
    return render(request, 'misha/comparison_phone.html', {})

def rishat(request):
    return render(request, 'rishat/test.html', {})

def zametki(request):
    return render(request, 'zametki/zametki.html', {})