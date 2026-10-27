from django.shortcuts import render

def index(request):
    return render(request, 'helloweb/index.html')

def news(request):
    return render(request, 'helloweb/news.html')

def management(request):
    return render(request, 'helloweb/management.html')

def facts(request):
    return render(request, 'helloweb/facts.html')

def contacts(request):
    return render(request, 'helloweb/contacts.html')

def history(request):
    return render(request, 'helloweb/history.html')

def history_people(request):
    return render(request, 'helloweb/history_people.html')

def history_photos(request):
    return render(request, 'helloweb/history_photos.html')