from django.shortcuts import render, redirect, get_object_or_404
import pandas as pd
import re
from Bench.models import Employee
# Create your views here.
import os
import pandas as pd 
import numpy as np
from datetime import datetime




# def bench_emp(request):
#     if request.method == 'GET':
#         # df=pd.read_csv(r'D:\twilight\python\Bench_mgnt\Bench\vasanth_sir_team.csv')
#         # df.where(pd.notnull(df), None)
#         # df['Team Leader Name']='Mr.Vasanth'
#         # df1 = df.replace(np.nan, '', regex=True)
#         # for i in df1.to_dict('records'):
#         #     print(i)
#         #     Employee.objects.create(
#         #         name=i['Team Members'],
#         #         team_leader=i['Team Leader Name'],
#         #         designation=i['Designation'] or None,
#         #         experience=i['Experience']or None,
#         #         stack=i['Stack']or None,
#         #         skills=i['Skills']or None,
#         #         resource_status=i['Resource Status']or None,
#         #         date_of_joining=i['Date Of Joining']or None,
                
#         #     )
#         employes = Employee.objects.all()
#         context = {'employes': employes}
#         return render(request, 'benchrows.html', context)
#     elif request.method == 'POST':
#         employes = Employee.objects.filter(primary_skills=request.POST['search']).order_by(
#             "-experience") | Employee.objects.filter(secondary_skills=request.POST['search']).order_by("-experience")
#         context = {"employes": employes, 'form_data': request.POST['search']}
#         return render(request, 'benchrows.html', context)


def manage_emp(request):
    if request.method == 'GET':
        employes = Employee.objects.all()
        team_leader= Employee.objects.order_by().values('team_leader').distinct()
        designation= Employee.objects.order_by().values('designation').distinct()
        stack= Employee.objects.order_by().values('stack').distinct()
        
        print(designation)
        
        resource_status= Employee.objects.order_by().values('resource_status').distinct()
        context = {'employes': employes,'stack':stack,'team_leader':team_leader,'designation':designation,'resource_status':resource_status}
        return render(request, 'employes.html', context)


def create_emp(request):
    if request.method == 'GET':
        return render(request, 'create_emp.html')
    elif request.method == 'POST':
        emp = Employee()
        emp.name = request.POST['name']
        emp.experience = request.POST['experience']
        emp.team_leader = request.POST['team_leader']
        emp.designation = request.POST['designation']
        emp.date_of_joining=datetime.strptime(request.POST['date_of_joining'], "%Y-%m-%d")
        emp.resource_status = request.POST['resource_status']
        emp.skills = request.POST['skills']
        emp.profile_link = request.POST['profile_link']
        emp.save()
        return redirect('Bench:manage_emp')


def delete_emp(request, id):
    get_object_or_404(Employee, id=id).delete()
    return redirect('Bench:manage_emp')

    # msg=messages.error(request, 'This  has been deleted.')


def edit_emp(request, id):
    if request.method == 'GET':
        emp = Employee.objects.get(id=id)
        return render(request, 'create_emp.html',context = {'emp':emp})
    elif request.method == 'POST':
        # print(request.POST['name'])
        Employee.objects.filter(id=id).update(
        name = request.POST['name'],
        experience = request.POST['experience'],
        team_leader = request.POST['team_leader'],
        designation = request.POST['designation'],
        date_of_joining=datetime.strptime(request.POST['date_of_joining'], "%Y-%m-%d"),
        resource_status = request.POST['resource_status'],
        skills = request.POST['skills'],
        profile_link = request.POST['profile_link'],
        )
        return redirect('Bench:manage_emp')
