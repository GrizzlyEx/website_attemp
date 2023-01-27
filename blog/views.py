from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})
# Create your views here.


def misha(request):
    return render(request, 'misha/comparison_phone.html', {})

def kirill_besish(request):
    return render(request, 'kirill_besish/ostatki_nelikvid.html', {})