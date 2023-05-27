from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# projectList = [
#                 {
#                     'id':'1',
#                     'title':"Ecommerce Website",
#                     'description':'Fully functional ecommerce website'
#                 },
#                 {
#                     'id':'2',
#                     'title':"Portfolio Website",
#                     'description':'This is a project where I built out my portfolio'
#                 },
#                 {
#                     'id':'3',
#                     'title':"Social Network",
#                     'description':'Awesome open source project I am still working'
#                 }

# ]

def projects(request):
    mess = 'This is message from phani challa'
    number = 10
    projectList = Project.objects.all()
    context = {'message': mess, 'num':number,'projects':projectList}
    
    return render(request,'projects/projects.html',context)

# def project(request,pk):
#     return HttpResponse('SINGLE PROJECT'+'  '+str(pk))

def project(request,pk):
    # projectObj = None
    # for i in projectList:
    #     if i['id'] == pk:
    #         projectObj = i
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()

    return render(request, 'projects/single-project.html',{'project':projectObj})


def create_Project(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        #print(request.POST)
        form = ProjectForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request,"projects/project_form.html",context)


def update_Project(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        #print(request.POST)
        form = ProjectForm(request.POST,request.FILES,instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request,"projects/project_form.html",context)

def delete_Project(request,pk):
    
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()

        return redirect('projects')
    context={'object':project}
    return render(request, 'projects/delete_object.html',context)



