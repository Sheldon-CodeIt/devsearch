from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projectsLst = [
    {
        'id': '1',
        'title': 'PhishFind',
        'description': 'AI enabled phishing URLs detection using Machine Learning',
        'topRated': True

    }, 
    {
        'id': '2',
        'title': 'Ecommerce Website',
        'description': 'Fully funcitonal ecommerce website',
        'topRated': False

    }, 
    {
        'id': '3',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display achievements/ projects',
        'topRated': False

    }, 
]

def projects(request):
    context = {'projects': projectsLst}
    return render(request, 'projects/projects.html', context)



def project(request, pk):

    projectObject = None

    for i in projectsLst:
        if i['id'] == str(pk):
            projectObject = i

    return render(request, 'projects/single-project.html', {"project": projectObject})

