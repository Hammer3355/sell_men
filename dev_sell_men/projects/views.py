from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


def projects(request):
    pr = Project.objects.all()
    context = {'projects': pr}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    # pr = Project.objects.get(id=pk)
    context = {'project': project_obj}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)
