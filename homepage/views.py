from django.shortcuts import render

def index(request):
    name = '<i>Grizzly</i>'
    lname = '<strong><i>Exception</i></strong>'
    context = {
        'name': name,
        'lname': lname,
    }
    return render(request, 'homepage/index.html', context)
