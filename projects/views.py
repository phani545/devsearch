from django.shortcuts import render
from django.http import HttpResponse


projectList = [
                {
                    'id':'1',
                    'title':"Ecommerce Website",
                    'description':'Fully functional ecommerce website'
                },
                {
                    'id':'2',
                    'title':"Portfolio Website",
                    'description':'This is a project where I built out my portfolio'
                },
                {
                    'id':'3',
                    'title':"Social Network",
                    'description':'Awesome open source project I am still working'
                }

]

def projects(request):
    mess = 'This is message from phani challa'
    number = 10
    context = {'message': mess, 'num':number,'projects':projectList}
    return render(request,'projects/projects.html',context)

# def project(request,pk):
#     return HttpResponse('SINGLE PROJECT'+'  '+str(pk))

def project(request,pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html',{'project':projectObj})



