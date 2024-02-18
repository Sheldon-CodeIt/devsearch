from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)



def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    tags = projectObject.tags.all()
    reviews = projectObject.review_set.all()
    context = {
        "project": projectObject,
        "tags": tags,
        "reviews": reviews
    }
    return render(request, 'projects/single-project.html', context)



def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }
    return render(request, 'projects/project-form.html', context) 